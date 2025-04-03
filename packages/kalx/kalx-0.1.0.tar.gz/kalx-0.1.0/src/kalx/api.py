"""
Public API for kalX scripting.
"""

from typing import Optional, Dict, List
from datetime import datetime
import json
from kalx.auth.authentication import Authentication
from kalx.chat.message import MessageManager
from kalx.chat.group import GroupManager
from kalx.auth.user import UserManager

class KalXClient:
    """Client for kalX API."""
    
    def __init__(self):
        self.auth = Authentication()
        self.message_manager = MessageManager()
        self.group_manager = GroupManager()
        self.user_manager = UserManager()
        self.user_data = None

    def connect(self, username: str, password: str) -> bool:
        """Connect to kalX with credentials."""
        success, result = self.auth.login(username, password)
        if success:
            self.user_data = result
            return True
        return False

    def send_message(self, recipient: str, message: str) -> bool:
        """Send a message to user or group."""
        if not self.user_data:
            raise RuntimeError("Not connected. Call connect() first")
            
        if recipient.startswith("#"):  # Group message
            group_id = recipient[1:]
            success, _ = self.group_manager.send_message(
                self.user_data["user_id"], 
                group_id, 
                message
            )
        else:  # Private message
            from kalx.chat.private import PrivateChat
            private = PrivateChat(self.user_data["user_id"])
            success, _ = private.send_message(recipient, message)
        return success

    def schedule_message(self, recipient: str, message: str, schedule: str) -> bool:
        """Schedule a message to be sent."""
        from kalx.utils.scheduler import schedule_task
        return schedule_task(
            task_type="message",
            recipient=recipient,
            content=message, 
            schedule=schedule,
            user_id=self.user_data["user_id"] if self.user_data else None
        )

def connect(username: str = None, password: str = None) -> KalXClient:
    """
    Connect to kalX and return a client instance.
    
    Example:
        >>> from kalx import api
        >>> client = api.connect("user@email.com", "password")
        >>> client.send_message("friend", "Hello!")
        >>> client.schedule_message("#team", "Meeting time!", "0 9 * * *")
    """
    client = KalXClient()
    if username and password:
        if not client.connect(username, password):
            raise ConnectionError("Failed to authenticate")
    return client
