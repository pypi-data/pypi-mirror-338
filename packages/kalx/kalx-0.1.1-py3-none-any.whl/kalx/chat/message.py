# kalx/chat/message.py
"""
Message models and utilities.
"""

from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from enum import Enum
from uuid import uuid4

class MessageType(Enum):
    """Types of messages."""
    TEXT = "text"
    SYSTEM = "system"
    NOTIFICATION = "notification"
    COMMAND = "command"
    REPLY = "reply"

@dataclass
class Message:
    """Message model for chat messages."""
    id: str
    sender_id: str
    content: str
    timestamp: datetime
    message_type: MessageType = MessageType.TEXT
    recipient_id: Optional[str] = None
    group_id: Optional[str] = None
    reply_to: Optional[str] = None
    is_edited: bool = False
    is_deleted: bool = False
    is_pinned: bool = False
    
    @classmethod
    def create_text_message(cls, sender_id: str, content: str, recipient_id: Optional[str] = None, group_id: Optional[str] = None):
        """
        Create a text message.
        
        Args:
            sender_id: The ID of the sender
            content: The message content
            recipient_id: The ID of the recipient (for private messages)
            group_id: The ID of the group (for group messages)
            
        Returns:
            Message: The created message object
        """
        if recipient_id and group_id:
            raise ValueError("A message cannot have both recipient_id and group_id")
        
        return cls(
            id=str(uuid4()),
            sender_id=sender_id,
            content=content,
            timestamp=datetime.now(),
            message_type=MessageType.TEXT,
            recipient_id=recipient_id,
            group_id=group_id
        )
    
    @classmethod
    def create_reply(cls, sender_id: str, content: str, reply_to: str, recipient_id: Optional[str] = None, group_id: Optional[str] = None):
        """
        Create a reply message.
        
        Args:
            sender_id: The ID of the sender
            content: The reply content
            reply_to: The ID of the message being replied to
            recipient_id: The ID of the recipient (for private replies)
            group_id: The ID of the group (for group replies)
            
        Returns:
            Message: The created reply message object
        """
        if recipient_id and group_id:
            raise ValueError("A reply cannot have both recipient_id and group_id")
        
        return cls(
            id=str(uuid4()),
            sender_id=sender_id,
            content=content,
            timestamp=datetime.now(),
            message_type=MessageType.REPLY,
            recipient_id=recipient_id,
            group_id=group_id,
            reply_to=reply_to
        )
    
    @classmethod
    def create_system_message(cls, content):
        """Create a system message."""
        return cls(
            id=str(uuid4()),
            sender_id="system",
            content=content,
            timestamp=datetime.now(),
            message_type=MessageType.SYSTEM
        )
    
    @classmethod
    def create_notification(cls, content, recipient_id=None, group_id=None):
        """Create a notification message."""
        return cls(
            id=str(uuid4()),
            sender_id="system",
            content=content,
            timestamp=datetime.now(),
            message_type=MessageType.NOTIFICATION,
            recipient_id=recipient_id,
            group_id=group_id
        )

class MessageManager:
    """Manages chat messages in Firebase Firestore."""
    
    def __init__(self):
        """Initialize the message manager."""
        from kalx.db.firebase_client import FirestoreClient
        self.db = FirestoreClient()
        self.collection = "messages"
    
    def send_message(self, message: Message) -> bool:
        """Send a message by storing it in Firestore."""
        message_data = {
            "id": message.id,
            "sender_id": message.sender_id,
            "content": message.content,
            "timestamp": message.timestamp,
            "message_type": message.message_type.value,
            "recipient_id": message.recipient_id,
            "group_id": message.group_id,
            "reply_to": message.reply_to,
            "is_edited": message.is_edited,
            "is_deleted": message.is_deleted,
            "is_pinned": message.is_pinned
        }
        
        return self.db.add_document(self.collection, message.id, message_data)
    
    def get_message(self, message_id: str) -> Optional[Message]:
        """Get a message by ID."""
        doc = self.db.get_document(self.collection, message_id)
        if not doc:
            return None
            
        return Message(
            id=doc.get("id"),
            sender_id=doc.get("sender_id"),
            content=doc.get("content"),
            timestamp=doc.get("timestamp"),
            message_type=MessageType(doc.get("message_type")),
            recipient_id=doc.get("recipient_id"),
            group_id=doc.get("group_id"),
            reply_to=doc.get("reply_to"),
            is_edited=doc.get("is_edited", False),
            is_deleted=doc.get("is_deleted", False),
            is_pinned=doc.get("is_pinned", False)
        )
    
    def edit_message(self, message_id: str, new_content: str) -> bool:
        """Edit a message's content."""
        return self.db.update_document(self.collection, message_id, {
            "content": new_content,
            "is_edited": True
        })
    
    def delete_message(self, message_id: str) -> bool:
        """Mark a message as deleted."""
        return self.db.update_document(self.collection, message_id, {
            "is_deleted": True
        })
    
    def pin_message(self, message_id: str, pin: bool = True) -> bool:
        """Pin or unpin a message."""
        return self.db.update_document(self.collection, message_id, {
            "is_pinned": pin
        })
    
    def get_private_chat_history(self, user1_id: str, user2_id: str, limit: int = 50) -> List[Message]:
        """Get the chat history between two users."""
        # Query messages where either user is sender and the other is recipient
        query1 = self.db.query_documents(
            self.collection, 
            [("sender_id", "==", user1_id), ("recipient_id", "==", user2_id)]
        )
        
        query2 = self.db.query_documents(
            self.collection, 
            [("sender_id", "==", user2_id), ("recipient_id", "==", user1_id)]
        )
        
        # Combine and sort by timestamp
        messages = query1 + query2
        messages.sort(key=lambda x: x.get("timestamp"))
        
        # Convert to Message objects
        return [self.get_message(msg.get("id")) for msg in messages[-limit:]]
    
    def get_group_chat_history(self, group_id: str, limit: int = 50) -> List[Message]:
        """Get the chat history for a group."""
        messages = self.db.query_documents(self.collection, "group_id", "==", group_id)
        
        # Sort by timestamp
        messages.sort(key=lambda x: x.get("timestamp"))
        
        # Convert to Message objects
        return [self.get_message(msg.get("id")) for msg in messages[-limit:]]
    
    def search_messages(self, keyword: str, user_id: str = None) -> List[Message]:
        """Search for messages containing a specific keyword."""
        # Firebase doesn't support full-text search natively
        # For a real app, you might consider using Algolia or a similar service
        # This is a simplified version that retrieves messages and filters client-side
        if user_id:
            messages = self.db.query_documents(
                self.collection,
                [("sender_id", "==", user_id), ("is_deleted", "==", False)]
            )
        else:
            messages = self.db.query_documents(self.collection, "is_deleted", "==", False)
        
        # Filter messages containing the keyword
        filtered_messages = [
            self.get_message(msg.get("id"))
            for msg in messages
            if keyword.lower() in msg.get("content", "").lower()
        ]
        
        return filtered_messages