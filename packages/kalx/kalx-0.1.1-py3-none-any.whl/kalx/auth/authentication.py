# kalx/auth/authentication.py
"""
Handles user authentication using Firebase Authentication.
"""

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import getpass
import os
from kalx.utils.logger import get_logger
from kalx.utils.config import get_config
from kalx.auth.user import UserManager  # Import UserManager
from kalx.auth.user import User, UserStatus  # Import User and UserStatus
from kalx.auth.validation import is_valid_email
from kalx.auth.firebase_auth import verify_password
from kalx.auth.firebase_auth import refresh_user_token
from datetime import datetime
from typing import Tuple, Optional

logger = get_logger(__name__)

class Authentication:
    """Manages user authentication with Firebase."""
    
    def __init__(self):
        """Initialize the authentication service."""
        self.initialized = False
        config = get_config()
        try:
            # Initialize Firebase
            cred_path = config.get('firebase', 'credentials_path')
            if not os.path.exists(cred_path):
                logger.error(f"Firebase credentials not found in package: {cred_path}")
                raise FileNotFoundError(f"Firebase credentials missing from package")
                
            cred = credentials.Certificate(cred_path)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            self.initialized = True
            logger.info("Firebase authentication initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Firebase: {str(e)}")
            raise
        
        self.user_manager = UserManager()  # Use UserManager for user operations

    def _check_initialized(self):
        """Check if Firebase is initialized."""
        if not self.initialized:
            raise RuntimeError("Firebase authentication not initialized. Run 'kalx --setup' first.")

    def register(self, email: str, password: str = None) -> Tuple[bool, Optional[dict]]:
        """Register a new user."""
        self._check_initialized()
        try:
            if not is_valid_email(email):
                raise ValueError("Invalid email format")

            if password is None:
                password = getpass.getpass("Enter password: ")
                confirm_password = getpass.getpass("Confirm password: ")
                if password != confirm_password:
                    raise ValueError("Passwords do not match")
                if len(password) < 6:
                    raise ValueError("Password must be at least 6 characters long")

            try:
                # Check if user already exists
                existing_user = auth.get_user_by_email(email)
                if existing_user:
                    return False, "An account with this email already exists"
            except auth.UserNotFoundError:
                pass  # This is what we want - user doesn't exist yet

            # Create user in Firebase Auth
            firebase_user = auth.create_user(
                email=email,
                password=password
            )
            logger.info(f"Created new user: {firebase_user.uid}")

            # Create user document using UserManager
            display_name = email.split('@')[0]
            user = User(
                user_id=firebase_user.uid,  # Use the UID from Firebase
                username=display_name,
                email=email,
                status=UserStatus.ONLINE
            )
            self.user_manager.create_user(user)
            logger.info(f"Created user document for {firebase_user.uid}")

            user_data = self.user_manager.get_user(firebase_user.uid)
            if user_data:
                # Save user data to JSON
                self.user_manager._save_to_json(user_data)
                return True, user_data

        except ValueError as e:
            return False, str(e)
        except Exception as e:
            logger.error(f"Failed to register user: {str(e)}")
            return False, "Registration failed. Please try again later."

    def login(self, email: str, password: str = None) -> Tuple[bool, Optional[dict]]:
        """
        Authenticate a user and get auth token.
        
        Args:
            email: User's email
            password: User's password
            
        Returns:
            Tuple[bool, Optional[dict]]: Success status and user data if successful
        """
        self._check_initialized()
        try:
            if not is_valid_email(email):
                return False, "Invalid email format"

            if password is None:
                password = getpass.getpass("Enter password: ")

            success, auth_data = verify_password(email, password)
            if not success or not auth_data:
                return False, "Invalid credentials"

            # Get user from Firebase Admin SDK
            try:
                firebase_user = auth.get_user_by_email(email)
            except auth.UserNotFoundError:
                return False, "No account found with this email"

            logger.info(f"User logged in: {firebase_user.uid}")

            # Get or create user using UserManager
            user_data = self.user_manager.get_user(firebase_user.uid)
            if not user_data:
                display_name = email.split('@')[0]
                user = User(
                    user_id=firebase_user.uid,  # Use the UID from Firebase
                    username=display_name,
                    email=email,
                    status=UserStatus.ONLINE
                )
                self.user_manager.create_user(user)
                logger.info(f"Created new user document for {firebase_user.uid}")
                user_data = self.user_manager.get_user(firebase_user.uid)
            else:
                # Update existing user status
                self.user_manager.update_status(user_data["user_id"], UserStatus.ONLINE)

            # Ensure the returned user data includes the correct user_id
            user_data["user_id"] = firebase_user.uid

            if user_data:
                # Save user data to JSON
                self.user_manager._save_to_json(user_data)
                return True, user_data

        except ValueError as e:
            return False, str(e)
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False, "Login failed. Please try again."
        
    def logout(self, user_id):
        """Log out the current user by using their user_id and updating their status to offline."""
        self._check_initialized()
        try:
            # Perform any additional logout logic using user_id if needed
            logger.info(f"Processing logout for user: {user_id}")

            # Update the user's status to offline
            self.user_manager.update_status(user_id, UserStatus.OFFLINE)
            logger.info(f"User logged out: {user_id}")
            return True, "Logged out successfully"
        except Exception as e:
            logger.error(f"Logout failed: {str(e)}")
            return False, str(e)
    
    def change_password(self, user_id, new_password):
        """Change the user's password."""
        self._check_initialized()
        try:
            auth.update_user(
                user_id,
                password=new_password
            )
            logger.info(f"Password changed for user: {user_id}")
            return True, "Password changed successfully"
        except Exception as e:
            logger.error(f"Password change failed: {str(e)}")
            return False, str(e)
    
    def delete_account(self, user_id):
        """Delete a user account."""
        self._check_initialized()
        try:
            auth.delete_user(user_id)
            logger.info(f"Account deleted: {user_id}")
            return True, "Account deleted successfully"
        except Exception as e:
            logger.error(f"Account deletion failed: {str(e)}")
            return False, str(e)
    
    def get_user_info(self, user_id):
        """Get user details by user ID."""
        self._check_initialized()
        try:
            user = auth.get_user(user_id)
            return True, user
        except Exception as e:
            logger.error(f"Failed to get user info: {str(e)}")
            return False, str(e)

    def refresh_token(self, user_id: str) -> None:
        """
        Refresh the authentication token for the user.

        Args:
            user_id: The ID of the user whose token needs to be refreshed.

        Raises:
            Exception: If the token refresh fails.
        """
        try:
            # Call the refresh_user_token function directly
            refreshed = refresh_user_token(user_id)
            if not refreshed:
                raise Exception("Token refresh failed.")
        except Exception as e:
            logger.error(f"Failed to refresh token for user {user_id}: {e}")
            raise