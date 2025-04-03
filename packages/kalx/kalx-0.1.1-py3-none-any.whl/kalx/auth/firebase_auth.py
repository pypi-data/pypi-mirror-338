"""
Firebase Authentication REST API client.
"""

import requests
from typing import Dict, Optional, Tuple
from kalx.utils.logger import get_logger

API_KEY = "AIzaSyD3SNCsNoozPFhC5AvEvo9bgUhm7nqtmpA"  # Your Firebase Web API Key
BASE_URL = "https://identitytoolkit.googleapis.com/v1"

logger = get_logger(__name__)

def verify_password(email: str, password: str) -> Tuple[bool, Optional[Dict]]:
    """
    Verify user credentials using Firebase Auth REST API.
    
    Args:
        email: User's email
        password: User's password
        
    Returns:
        Tuple[bool, Optional[Dict]]: Success status and user data if successful
    """
    endpoint = f"{BASE_URL}/accounts:signInWithPassword?key={API_KEY}"
    
    try:
        response = requests.post(endpoint, json={
            "email": email,
            "password": password,
            "returnSecureToken": True
        })
        
        if response.status_code == 200:
            return True, response.json()
            
        error_data = response.json()
        error_message = error_data.get('error', {}).get('message', 'Invalid credentials')
        
        if error_message == 'INVALID_PASSWORD':
            raise ValueError("Invalid password")
        elif error_message == 'EMAIL_NOT_FOUND':
            raise ValueError("No account found with this email")
        else:
            raise ValueError(error_message)
            
    except requests.RequestException as e:
        raise ValueError("Authentication service unavailable")

def refresh_user_token(refresh_token: str) -> Tuple[bool, Optional[Dict]]:
    """
    Refresh the user's authentication token using Firebase REST API.
    
    Args:
        refresh_token: The refresh token returned from the original authentication
        
    Returns:
        Tuple[bool, Optional[Dict]]: Success status and token data if successful
    """
    endpoint = f"https://securetoken.googleapis.com/v1/token?key={API_KEY}"
    
    try:
        response = requests.post(endpoint, json={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        })
        
        if response.status_code == 200:
            return True, response.json()
        
        error_data = response.json()
        error_message = error_data.get('error', {}).get('message', 'Token refresh failed')
        logger.error(f"Token refresh error: {error_message}")
        return False, None
            
    except requests.RequestException as e:
        logger.error(f"Error refreshing token: {e}")
        return False, None