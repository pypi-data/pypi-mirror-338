# kalx/ui/notifications.py
"""
Notification management for kalX.
"""

import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from kalx.chat.message import Message
from uuid import uuid4

@dataclass
class Notification:
    """Notification model."""
    user_id: str  # recipient's ID
    sender_id: str  # sender's ID
    message: Optional[Message] = None
    content: str = ""
    timestamp: datetime = None
    play_sound: bool = True
    read: bool = False
    
    def __post_init__(self):
        """Initialize default values."""
        if self.timestamp is None:
            self.timestamp = datetime.now()

class NotificationManager:
    """Manages notifications for users."""
    
    def __init__(self):
        """Initialize the notification manager."""
        from kalx.db.firebase_client import FirestoreClient
        self.db = FirestoreClient()
        self.collection = "notifications"

    def add_notification(self, notification: Notification) -> bool:
        """
        Add a notification for a user and persist it in Firestore.
        
        Args:
            notification: The notification to add
            
        Returns:
            bool: Whether the notification was added successfully
        """
        notification_data = {
            "user_id": notification.user_id,
            "sender_id": notification.sender_id,
            "content": notification.content,
            "timestamp": notification.timestamp.isoformat(),
            "read": notification.read
        }
        return self.db.add_document(self.collection, str(uuid4()), notification_data)

    def get_notifications(self, user_id: str, unread_only: bool = True) -> List[Notification]:
        """
        Get notifications for a user from Firestore.
        
        Args:
            user_id: The ID of the user
            unread_only: Whether to get only unread notifications
            
        Returns:
            List[Notification]: The user's notifications
        """
        filters = [("user_id", "==", user_id)]
        if unread_only:
            filters.append(("read", "==", False))
        
        docs = self.db.query_documents(self.collection, filters)
        notifications = [
            Notification(
                user_id=doc["user_id"],
                sender_id=doc["sender_id"],
                content=doc["content"],
                timestamp=datetime.fromisoformat(doc["timestamp"]),
                read=doc["read"]
            )
            for doc in docs
        ]
        
        # Mark notifications as read
        for doc in docs:
            if "id" in doc:  # Ensure the document has an ID
                self.db.update_document(self.collection, doc["id"], {"read": True})
        
        return notifications

    def clear_notifications(self, user_id: str) -> bool:
        """
        Clear all notifications for a user.
        
        Args:
            user_id: The ID of the user
            
        Returns:
            bool: Whether the notifications were cleared successfully
        """
        filters = [("user_id", "==", user_id)]
        docs = self.db.query_documents(self.collection, filters)
        for doc in docs:
            self.db.delete_document(self.collection, doc["id"])
        return True

    def display_notifications(self, user_id: str) -> None:
        """
        Display all unread notifications for a user in a professional hacker console style.
        
        Args:
            user_id: The ID of the user
        """
        notifications = self.get_notifications(user_id, unread_only=True)
        if not notifications:
            print("[bold green]No new notifications.[/bold green]")
            return

        from kalx.auth.user import UserManager
        user_manager = UserManager()

        print("[bold yellow]>> You have new notifications:[/bold yellow]\n")
        for notification in notifications:
            # Fetch user info for the notification header
            sender_info = user_manager.get_user(notification.sender_id)
            sender_name = sender_info.get("username", "Unknown") if sender_info else "Unknown"
            header = f"[bold cyan]New private message[/bold cyan]" if not notification.group_id else f"[bold cyan]New group message[/bold cyan]"

            # Format the notification content
            timestamp = notification.timestamp.strftime("%B %d, %Y %I:%M:%S %p")
            content = notification.content

            # Display the notification in a styled box
            print(f"{header} from [bold green]{sender_name}[/bold green]")
            print(f"[bold yellow]{timestamp}[/bold yellow]: {content}\n")