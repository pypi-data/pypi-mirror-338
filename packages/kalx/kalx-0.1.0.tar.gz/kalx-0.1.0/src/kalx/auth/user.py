"""
User model and profile management with JSON file backup.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Union
from enum import Enum
from datetime import datetime
import json
import os
from pathlib import Path
from kalx.db.firebase_client import FirestoreClient
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

class UserStatus(Enum):
    """User status enum."""
    ONLINE = "online"
    AWAY = "away"
    BUSY = "busy"
    OFFLINE = "offline"

@dataclass
class User:
    """User model containing profile information."""
    user_id: str
    username: str
    email: str
    status: UserStatus = UserStatus.OFFLINE
    display_name: Optional[str] = None
    created_at: datetime = datetime.now()
    last_active: datetime = datetime.now()
    blocked_users: List[str] = None
    friends: List[str] = None
    groups: List[str] = None
    settings: Dict = None
    pending_requests: List[str] = None
    notifications: List[str] = None
    
    def __post_init__(self):
        """Initialize default values for optional fields."""
        if self.blocked_users is None:
            self.blocked_users = []
        if self.friends is None:
            self.friends = []
        if self.groups is None:
            self.groups = []
        if self.settings is None:
            self.settings = {
                "theme": "dark",
                "font": "default",
                "color": "green",
                "notifications": True,
                "sound": True,
                "autoscroll": True
            }
        if self.display_name is None:
            self.display_name = self.username
        if self.pending_requests is None:
            self.pending_requests = []
        if self.notifications is None:
            self.notifications = []

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class UserManager:
    """Manages user data in Firestore and local JSON files."""
    
    def __init__(self, json_dir=None):
        """Initialize the user manager.
        
        Args:
            json_dir: Directory to store JSON user data files
        """
        self.db = FirestoreClient()
        # Use .kalx directory for storing user data
        self.json_dir = json_dir or os.path.join(Path.home(), ".kalx")
        os.makedirs(self.json_dir, exist_ok=True)
        self.json_file = os.path.join(self.json_dir, "klx.json")

    def _save_to_json(self, user_data: Dict) -> bool:
        """Save user data to a JSON file."""
        try:
            # Save all user data to klx.json
            with open(self.json_file, 'w') as f:
                json.dump(user_data, f, cls=DateTimeEncoder, indent=4)
            logger.info(f"User data saved to {self.json_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to save user data to JSON: {str(e)}")
            return False

    def _load_from_json(self) -> Optional[Dict]:
        """Load user data from the JSON file."""
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            logger.error(f"Failed to load user data from JSON: {str(e)}")
            return None

    def get_user(self, user_id: str) -> Optional[Dict]:
        """Get user data by ID."""
        # Always try to load from JSON first to get current user
        local_data = self._load_from_json()
        
        # Get the current user's ID from local data
        current_user_id = local_data.get("user_id") if local_data else None
        if not current_user_id:
            logger.error("No authenticated user found in local data")
            return None
            
        # Now use Firestore with current user's authentication
        try:
            user_data = self.db.get_document('users', user_id)
            if not user_data:
                # Try getting by email if UID fails
                users = self.db.query_documents('users', [("email", "==", user_id)])
                if users:
                    user_data = users[0]
            return user_data
        except Exception as e:
            logger.error(f"Failed to get user {user_id}: {str(e)}")
            return None

    def update_user(self, user_id_or_data: Union[str, Dict], data: Dict = None) -> bool:
        """Update user data and the corresponding JSON file."""
        try:
            # Handle both user_id and direct data update cases
            if isinstance(user_id_or_data, str):
                user_id = user_id_or_data
                update_data = data
            else:
                user_id = user_id_or_data.get('user_id')
                update_data = user_id_or_data

            if not user_id:
                logger.error("No user ID provided for update")
                return False

            # Get existing user data first
            existing_user = self.get_user(user_id)
            if not existing_user:
                logger.error(f"User {user_id} not found")
                return False

            # Merge existing data with updates
            merged_data = {**existing_user, **(update_data or {})}
                
            # Update in Firestore
            success = self.db.update_document('users', user_id, merged_data)
            
            if success:
                # Save to JSON if it's the current user
                current_user = self._load_from_json()
                if current_user and current_user.get('user_id') == user_id:
                    self._save_to_json(merged_data)
                    
            return success
        except Exception as e:
            logger.error(f"Failed to update user {user_id}: {str(e)}")
            return False

    def create_user(self, user: User) -> bool:
        """Create a new user profile in Firestore and save to JSON."""
        user_data = {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "status": user.status.value,
            "display_name": user.display_name,
            "created_at": user.created_at,
            "last_active": user.last_active,
            "blocked_users": user.blocked_users,
            "friends": user.friends,
            "groups": user.groups,
            "settings": user.settings,
            "pending_requests": user.pending_requests,
            "notifications": user.notifications
        }
        
        # Create user in Firestore
        success = self.db.add_document("users", user.user_id, user_data)
        
        if success:
            # Save to JSON file
            self._save_to_json(user_data)
            
        return success
    
    def update_status(self, user_id: str, status: UserStatus) -> bool:
        """Update user's status."""
        return self.update_user(user_id, {
            "status": status.value,
            "last_active": datetime.now()
        })
    
    def update_settings(self, user_id: str, settings: Dict) -> bool:
        """Update user's settings."""
        return self.update_user(user_id, {
            "settings": settings
        })
    
    def add_friend(self, user_id: str, friend_id: str) -> bool:
        """Add another user as a friend."""
        user_data = self.get_user(user_id)
        if not user_data:
            return False
            
        friends = user_data.get("friends", [])
        if friend_id not in friends:
            friends.append(friend_id)
            return self.update_user(user_id, {"friends": friends})
        return True
    
    def remove_friend(self, user_id: str, friend_id: str) -> bool:
        """Remove a user from friends list."""
        user_data = self.get_user(user_id)
        if not user_data:
            return False
            
        friends = user_data.get("friends", [])
        if friend_id in friends:
            friends.remove(friend_id)
            return self.update_user(user_id, {"friends": friends})
        return True
    
    def block_user(self, user_id: str, blocked_id: str) -> bool:
        """Block another user."""
        user_data = self.get_user(user_id)
        if not user_data:
            return False
            
        blocked_users = user_data.get("blocked_users", [])
        if blocked_id not in blocked_users:
            blocked_users.append(blocked_id)
            return self.update_user(user_id, {"blocked_users": blocked_users})
        return True
    
    def unblock_user(self, user_id: str, blocked_id: str) -> bool:
        """Unblock a previously blocked user."""
        user_data = self.get_user(user_id)
        if not user_data:
            return False
            
        blocked_users = user_data.get("blocked_users", [])
        if blocked_id in blocked_users:
            blocked_users.remove(blocked_id)
            return self.update_user(user_id, {"blocked_users": blocked_users})
        return True
    
    def get_users_by_status(self, status: UserStatus) -> List[Dict]:
        """Get all users with a specific status."""
        users = self.db.query_documents("users", filter=("status", "==", status.value))
        return users
    
    def get_all_users(self) -> List[Dict]:
        """Get all registered users."""
        users = self.db.get_all_documents("users")
        return users
    
    def delete_user(self, user_id: str) -> bool:
        """Delete a user profile and its JSON file."""
        # Try to delete the JSON file
        try:
            if os.path.exists(self.json_file):
                os.remove(self.json_file)
                logger.info(f"Deleted user JSON file: {self.json_file}")
        except Exception as e:
            logger.error(f"Failed to delete user JSON file: {str(e)}")
            
        # Delete from Firestore
        return self.db.delete_document("users", user_id)