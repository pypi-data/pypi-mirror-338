# kalx/notifications/notification_manager.py
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
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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
        self.console = Console()

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
        Display all unread notifications for a user with individual panels.
        
        Args:
            user_id: The ID of the user
        """
        notifications = self.get_notifications(user_id, unread_only=True)
        if not notifications:
            self.console.print("[bold green]No new notifications.[/bold green]")
            return

        from kalx.auth.user import UserManager
        user_manager = UserManager()

        # Sort notifications by timestamp, newest first
        notifications.sort(key=lambda x: x.timestamp, reverse=True)

        # Display each notification in its own panel
        for notif in notifications:
            # Get sender info
            sender_info = user_manager.get_user(notif.sender_id)
            sender_name = sender_info.get('username', 'Unknown') if sender_info else 'Unknown'
            
            # Format timestamp
            timestamp = notif.timestamp.strftime("%H:%M:%S")
            
            # Build notification content
            notification_content = Text()
            notification_content.append(f"From: [bold cyan]{notif.sender_id}[/bold cyan]\n")
            notification_content.append(f"{notif.content}\n\n")
            notification_content.append(f"[dim]{timestamp}[/dim]")

            # Display notification in panel with sender's name as title
            self.console.print(Panel(
                notification_content,
                title=f"[bold yellow]{sender_name}[/bold yellow]",
                border_style="bright_magenta",
                width=60
            ))
            
            # Add small spacing between notifications
            self.console.print("")