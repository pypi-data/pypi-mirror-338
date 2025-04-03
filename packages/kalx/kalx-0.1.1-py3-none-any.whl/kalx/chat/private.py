# kalx/chat/private.py
"""
Handles private chat functionality.
"""

from typing import List, Optional, Tuple, Dict
from kalx.chat.message import Message, MessageManager
from kalx.auth.user import UserManager
from kalx.notifications import NotificationManager, Notification

class PrivateChat:
    """
    Manages private chat sessions between two users.
    """
    
    def __init__(self, user_id: str):
        """
        Initialize a private chat handler for a user.
        
        Args:
            user_id: The ID of the current user
        """
        self.user_id = user_id
        self.message_manager = MessageManager()
        self.user_manager = UserManager()

    def _get_current_user_data(self) -> Optional[Dict]:
        """
        Retrieve the current user data from klx.json.
        
        Returns:
            Optional[Dict]: The current user data
        """
        return self.user_manager._load_from_json()

    def send_message(self, recipient_id: str, content: str) -> Tuple[bool, str]:
        """Send a private message to another user."""
        # First get local user data
        user_data = self._get_current_user_data()
        if not user_data or not user_data.get("user_id"):
            return False, "Not authenticated. Please login first."
        
        sender_id = user_data.get("user_id")
        
        # Get recipient data using authenticated user_id
        recipient = self.user_manager.get_user(recipient_id)
        if not recipient:
            return False, "Recipient not found"
        
        recipient_username = recipient.get('username', 'Unknown')
        
        # Prevent sending messages to oneself
        if recipient_id == sender_id:
            return False, "You cannot send messages to yourself"
        
        # Check if sender and recipient are friends
        sender_friends = user_data.get("friends", [])
        if recipient_id not in sender_friends:
            # Check if there's a pending friend request
            recipient_pending = recipient.get("pending_requests", [])
            if sender_id in recipient_pending:
                return False, f"Cannot send message to {recipient_username}. Friend request is still pending."
            return False, f"Cannot send message to {recipient_username}. You need to be friends first."
        
        # Check if the recipient has blocked the sender
        if sender_id in recipient.get("blocked_users", []):
            return False, f"Cannot send message. {recipient_username} has blocked you."
        
        # Check if the sender has blocked the recipient
        if recipient_id in user_data.get("blocked_users", []):
            return False, f"Cannot send message. You have blocked {recipient_username}."

        # Create and send private message
        message = Message.create_text_message(
            sender_id=sender_id,
            content=content,
            recipient_id=recipient_id,
            group_id=None
        )
        
        success = self.message_manager.send_message(message)
        if success:
            # Get sender's username for the notification
            sender = self.user_manager.get_user(sender_id)
            sender_name = sender.get('username', 'Unknown') if sender else 'Unknown'
            
            # Add notification for the recipient with sender info
            notification_manager = NotificationManager()
            notification = Notification(
                user_id=recipient_id,
                sender_id=sender_id,
                content=f"New message from {sender_name}: {content}",
                play_sound=True
            )
            notification_manager.add_notification(notification)
            return True, message.id
        return False, "Failed to send message"

    def reply_to_message(self, recipient_id: str, content: str, reply_to: str) -> Tuple[bool, str]:
        """
        Reply to a specific private message.
        
        Args:
            recipient_id: The ID of the recipient
            content: The message content
            reply_to: The ID of the message being replied to
            
        Returns:
            Tuple[bool, str]: Success status and message ID or error message
        """
        user_data = self._get_current_user_data()
        sender_id = user_data.get("user_id")  # Use user_id from klx.json
        
        # Check if the original message exists
        original = self.message_manager.get_message(reply_to)
        if not original or original.get("group_id") is not None:
            return False, "Original message is not a private message"
        
        # Create and send reply
        message = Message.create_reply(
            sender_id=sender_id,
            content=content,
            recipient_id=recipient_id,
            reply_to=reply_to,
            group_id=None  # Explicitly set group_id to None for private replies
        )
        
        success = self.message_manager.send_message(message)
        return (success, message.id) if success else (False, "Failed to send reply")

    def edit_message(self, message_id: str, new_content: str) -> Tuple[bool, str]:
        """
        Edit a previously sent message.
        
        Args:
            message_id: The ID of the message to edit
            new_content: The new message content
            
        Returns:
            Tuple[bool, str]: Success status and result message
        """
        user_data = self._get_current_user_data()
        sender_id = user_data.get("user_id")  # Use user_id from klx.json
        
        # Check if the message exists and belongs to the user
        message = self.message_manager.get_message(message_id)
        if not message:
            return False, "Message not found"
        
        if message.sender_id != sender_id:
            return False, "You can only edit your own messages"
        
        success = self.message_manager.edit_message(message_id, new_content)
        return (success, "Message edited") if success else (False, "Failed to edit message")

    def delete_message(self, message_id: str) -> Tuple[bool, str]:
        """
        Delete a message.
        
        Args:
            message_id: The ID of the message to delete
            
        Returns:
            Tuple[bool, str]: Success status and result message
        """
        user_data = self._get_current_user_data()
        sender_id = user_data.get("user_id")  # Use user_id from klx.json
        
        # Check if the message exists and belongs to the user
        message = self.message_manager.get_message(message_id)
        if not message:
            return False, "Message not found"
        
        if message.sender_id != sender_id:
            return False, "You can only delete your own messages"
        
        success = self.message_manager.delete_message(message_id)
        return (success, "Message deleted") if success else (False, "Failed to delete message")

    def get_chat_history(self, other_user_id: str, limit: int = 50) -> List[Message]:
        """
        Get chat history with another user.
        
        Args:
            other_user_id: The ID of the other user
            limit: Maximum number of messages to retrieve
            
        Returns:
            List[Message]: The chat history
        """
        user_data = self._get_current_user_data()
        return self.message_manager.get_private_chat_history(self.user_id, other_user_id, limit)
