# kalx/chat/group.py
"""
Handles group chat functionality.
"""

from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime
from uuid import uuid4
from kalx.chat.message import Message, MessageManager
from kalx.auth.user import UserManager
from kalx.ui.notifications import Notification, NotificationManager
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

class MemberRole(Enum):
    """Possible roles for group members."""
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"

class Group:
    """Group chat model."""
    
    def __init__(self, 
                 group_id: str,
                 name: str,
                 owner_id: str,
                 created_at: datetime = None,
                 members: Dict[str, MemberRole] = None,
                 description: str = ""):
        """
        Initialize a group.
        
        Args:
            group_id: Unique identifier for the group
            name: Group name
            owner_id: User ID of the group owner
            created_at: Group creation timestamp
            members: Dictionary of member IDs to roles
            description: Group description
        """
        self.group_id = group_id
        self.name = name
        self.owner_id = owner_id
        self.created_at = created_at or datetime.now()
        self.members = members or {owner_id: MemberRole.OWNER}
        self.description = description
    
    @classmethod
    def create_group(cls, name: str, owner_id: str, description: str = ""):
        """Create a new group."""
        # Generate 6-character group ID
        group_id = str(uuid4())[:6].upper()
        return cls(
            group_id=group_id,
            name=name,
            owner_id=owner_id,
            description=description,
            created_at=datetime.now()
        )

class GroupManager:
    """Manages group chats in Firestore."""
    
    def __init__(self):
        """Initialize the group manager."""
        from kalx.db.firebase_client import FirestoreClient
        self.db = FirestoreClient()
        self.collection = "groups"
        self.message_manager = MessageManager()
        self.user_manager = UserManager()
    
    def _get_current_user_data(self, user_id: str) -> Optional[Dict]:
        """
        Retrieve the current user data from klx.json.
        
        Args:
            user_id: The ID of the current user
            
        Returns:
            Optional[Dict]: The current user data
        """
        return self.user_manager._load_from_json()

    def create_group(self, name: str, owner_id: str, description: str = "") -> Tuple[bool, str]:
        """Create a new group."""
        try:
            group = Group.create_group(name, owner_id, description)
            
            # Create initial group data
            group_data = {
                "group_id": group.group_id,
                "name": group.name,
                "owner_id": group.owner_id,
                "created_at": group.created_at.isoformat(),
                "members": {owner_id: MemberRole.OWNER.value},
                "description": group.description,
                "groups": []  # Initialize empty groups list
            }
            
            # Add to Firestore
            success = self.db.add_document(self.collection, group.group_id, group_data)
            
            if success:
                # Update owner's profile with the new group
                owner = self.user_manager.get_user(owner_id)
                if owner:
                    if not owner.get('groups'):
                        owner['groups'] = []
                    owner['groups'].append(group.group_id)
                    self.user_manager.update_user(owner_id, owner)
                    
                # Create system message
                system_msg = Message.create_system_message(f"Group '{name}' created by {owner_id}")
                system_msg.group_id = group.group_id
                self.message_manager.send_message(system_msg)
                
                return True, group.group_id
            return False, "Failed to add group to database"
        except Exception as e:
            logger.error(f"Error in create_group: {str(e)}")
            return False, str(e)

    def get_group(self, group_id: str) -> Optional[Group]:
        """Get a group by ID."""
        doc = self.db.get_document(self.collection, group_id)
        if not doc:
            return None
            
        # Convert member roles from strings back to enum values
        members = {}
        for member_id, role in doc.get("members", {}).items():
            members[member_id] = MemberRole(role)
            
        return Group(
            group_id=doc.get("group_id"),
            name=doc.get("name"),
            owner_id=doc.get("owner_id"),
            created_at=doc.get("created_at"),
            members=members,
            description=doc.get("description", "")
        )
    
    def update_group(self, group: Group) -> bool:
        """Update group information."""
        # Convert member roles from enum values to strings
        members_data = {}
        for member_id, role in group.members.items():
            members_data[member_id] = role.value
            
        group_data = {
            "name": group.name,
            "owner_id": group.owner_id,
            "members": members_data,
            "description": group.description
        }
        
        return self.db.update_document(self.collection, group.group_id, group_data)
    
    def delete_group(self, group_id: str) -> bool:
        """Delete a group."""
        group = self.get_group(group_id)
        if not group:
            return False
            
        # Remove group from all members' group lists
        for member_id in group.members:
            user = self.user_manager.get_user(member_id)
            if user and group_id in user.groups:
                user.groups.remove(group_id)
                self.user_manager.update_user(user)
                
        # Delete the group from Firestore
        return self.db.delete_document(self.collection, group_id)
    
    def add_member(self, group_id: str, user_id: str, role: MemberRole = MemberRole.MEMBER) -> bool:
        """
        Add a user to a group.
        
        Args:
            group_id: The ID of the group
            user_id: The ID of the user to add
            role: The role to assign to the user
            
        Returns:
            bool: Whether the addition was successful
        """
        user_data = self._get_current_user_data(user_id)
        group = self.get_group(group_id)
        if not group:
            return False, "Group not found"
            
        if user_id in group.members:
            return False, "User is already a member of this group"
            
        # Add member to group
        group.members[user_id] = role
        success = self.update_group(group)
        
        if success:
            # Add group to user's groups
            user = self.user_manager.get_user(user_id)
            if user and group_id not in user.groups:
                user.groups.append(group_id)
                self.user_manager.update_user(user)
                
            # Create system message for member addition
            system_msg = Message.create_system_message(f"User {user_id} joined the group")
            system_msg.group_id = group_id
            self.message_manager.send_message(system_msg)
            
            return True, "Member added to group"
        return False, "Failed to add member to group"
    
    def remove_member(self, group_id: str, user_id: str, actor_id: str) -> Tuple[bool, str]:
        """
        Remove a user from a group.
        
        Args:
            group_id: The ID of the group
            user_id: The ID of the user to remove
            actor_id: The ID of the user performing the action
            
        Returns:
            Tuple[bool, str]: Success status and message
        """
        user_data = self._get_current_user_data(actor_id)
        group = self.get_group(group_id)
        if not group:
            return False, "Group not found"
            
        if user_id not in group.members:
            return False, "User is not a member of this group"
            
        # Check permissions
        if actor_id != group.owner_id and (actor_id != user_id and 
                                           group.members.get(actor_id) != MemberRole.ADMIN):
            return False, "You don't have permission to remove this user"
            
        # Cannot remove the owner
        if user_id == group.owner_id:
            return False, "Cannot remove the group owner"
            
        # Remove member from group
        del group.members[user_id]
        success = self.update_group(group)
        
        if success:
            # Remove group from user's groups
            user = self.user_manager.get_user(user_id)
            if user and group_id in user.groups:
                user.groups.remove(group_id)
                self.user_manager.update_user(user)
                
            # Create system message for member removal
            if actor_id == user_id:
                system_msg = Message.create_system_message(f"User {user_id} left the group")
            else:
                system_msg = Message.create_system_message(f"User {user_id} was removed from the group by {actor_id}")
            system_msg.group_id = group_id
            self.message_manager.send_message(system_msg)
            
            return True, "Member removed from group"
        return False, "Failed to remove member from group"
    
    def change_member_role(self, group_id: str, user_id: str, new_role: MemberRole, actor_id: str) -> Tuple[bool, str]:
        """
        Change a member's role in a group.
        
        Args:
            group_id: The ID of the group
            user_id: The ID of the user whose role is changing
            new_role: The new role to assign
            actor_id: The ID of the user performing the action
            
        Returns:
            Tuple[bool, str]: Success status and message
        """
        group = self.get_group(group_id)
        if not group:
            return False, "Group not found"
            
        if user_id not in group.members:
            return False, "User is not a member of this group"
            
        # Only the owner can change roles
        if actor_id != group.owner_id:
            return False, "Only the group owner can change roles"
            
        # Cannot change the owner's role
        if user_id == group.owner_id and new_role != MemberRole.OWNER:
            return False, "Cannot change the owner's role"
            
        # Update role
        group.members[user_id] = new_role
        success = self.update_group(group)
        
        if success:
            # Create system message for role change
            system_msg = Message.create_system_message(f"User {user_id}'s role changed to {new_role.value}")
            system_msg.group_id = group_id
            self.message_manager.send_message(system_msg)
            
            return True, f"Role changed to {new_role.value}"
        return False, "Failed to change role"
    
    def get_user_groups(self, user_id: str) -> List[Group]:
        """
        Get all groups a user belongs to.
        
        Args:
            user_id: The ID of the user
            
        Returns:
            List[Group]: The groups the user belongs to
        """
        user = self.user_manager.get_user(user_id)
        if not user:
            return []
            
        return [self.get_group(group_id) for group_id in user.groups]
    
    def send_message(self, user_id: str, group_id: str, content: str) -> Tuple[bool, str]:
        """
        Send a message to a group.
        
        Args:
            user_id: The ID of the sender
            group_id: The ID of the group
            content: The message content
            
        Returns:
            Tuple[bool, str]: Success status and message ID or error message
        """
        user_data = self._get_current_user_data(user_id)
        sender_id = user_data.get("user_id")  # Use user_id from klx.json
        
        group = self.get_group(group_id)
        if not group:
            return False, "Group not found"
            
        if user_id not in group.members:
            return False, "You are not a member of this group"
            
        # Create and send group message (must include group_id)
        message = Message.create_text_message(
            sender_id=sender_id,
            content=content,
            group_id=group_id  # Ensure group_id is set for group messages
        )
        
        success = self.message_manager.send_message(message)
        
        if success:
            # Notify all group members except the sender with sender_id
            notification_manager = NotificationManager()
            for member_id in group.members:
                if member_id != user_id:
                    notification = Notification(
                        user_id=member_id,
                        sender_id=sender_id,  # Include sender_id
                        content=f"New message in group '{group.name}' from {user_id}: {content}",
                        play_sound=True
                    )
                    notification_manager.add_notification(notification)
        
        return (success, message.id) if success else (False, "Failed to send message")
    
    def get_chat_history(self, group_id: str, limit: int = 50) -> List[Message]:
        """
        Get chat history for a group.
        
        Args:
            group_id: The ID of the group
            limit: Maximum number of messages to retrieve
            
        Returns:
            List[Message]: The chat history
        """
        return self.message_manager.get_group_chat_history(group_id, limit)