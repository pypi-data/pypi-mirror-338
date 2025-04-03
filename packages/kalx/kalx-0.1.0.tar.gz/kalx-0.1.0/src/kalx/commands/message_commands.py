"""
Command handlers for message-related commands.
"""

from typing import List, Any, Tuple, Optional
from kalx.chat.message import MessageManager, Message
from kalx.chat.private import PrivateChat
from kalx.chat.group import GroupManager
from kalx.auth.user import UserManager
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

def handle_msg(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Send a private message to a user.
    Usage: /msg [user] [message]
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()
    sender_id = user_data.get("user_id")  # Use user_id from klx.json

    if len(args) < 2:
        return False, "Usage: /msg [user] [message]"
        
    recipient = args[0]
    message = ' '.join(args[1:])
    
    # Prevent sending messages to oneself
    if recipient == sender_id:
        return False, "Invalid Operation!"
    
    # Check if recipient exists
    recipient_user = user_manager.get_user(recipient)
    if not recipient_user:
        return False, f"User '{recipient}' not found"
    
    recipient_id = recipient_user.get("user_id", recipient)
    recipient_name = recipient_user.get("username", recipient)
    
    # Send message - PrivateChat will handle blocked users internally
    private_chat = PrivateChat(sender_id)
    success, result = private_chat.send_message(recipient_id, message)
    
    if success:
        return True, f"Message sent to {recipient_name}"
    else:
        return False, result

def handle_gmsg(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Send a message to a group.
    Usage: /gmsg [group] [message]
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()
    sender_id = user_data.get("user_id")  # Use user_id from klx.json

    if len(args) < 2:
        return False, "Usage: /gmsg [group] [message]"
        
    group_id = args[0]
    message = ' '.join(args[1:])
    
    # Check if group exists and user is a member
    group_manager = GroupManager()
    group = group_manager.get_group(group_id)
    
    if not group:
        return False, f"Group '{group_id}' not found"
        
    if sender_id not in group.members:
        return False, "You are not a member of this group"
    
    # Create and send message
    success, result = group_manager.send_message(sender_id, group_id, message)
    
    if success:
        return True, f"Message sent to {group.name}"
    else:
        return False, "Failed to send message"

def handle_reply(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Reply to a specific message.
    Usage: /reply [message_id] [message]
    """
    if len(args) < 2:
        return False, "Usage: /reply [message_id] [message]"
        
    message_id = args[0]
    content = ' '.join(args[1:])
    
    # Check if original message exists
    message_manager = MessageManager()
    original = message_manager.get_message(message_id)
    
    if not original:
        return False, f"Message '{message_id}' not found"
    
    # Determine recipient or group based on the original message
    if original.group_id:
        # Group message reply
        group_manager = GroupManager()
        group = group_manager.get_group(original.group_id)
        
        if not group:
            return False, "Original message's group no longer exists"
            
        if user_id not in group.members:
            return False, "You are not a member of this group"
            
        reply = Message.create_reply(
            sender_id=user_id,
            content=content,
            reply_to=message_id,
            group_id=original.group_id
        )
        
        success = message_manager.send_message(reply)
        if success:
            return True, f"Reply sent to group {group.name}"
        else:
            return False, "Failed to send reply"
    else:
        # Private message reply
        recipient_id = original.sender_id if original.sender_id != user_id else original.recipient_id
        
        if not recipient_id:
            return False, "Cannot determine message recipient"
            
        private_chat = PrivateChat(user_id)
        success, result = private_chat.reply_to_message(recipient_id, content, message_id)
        
        if success:
            return True, "Reply sent"
        else:
            return False, result

def handle_editmsg(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Edit a sent message.
    Usage: /editmsg [message_id] [new_message]
    """
    if len(args) < 2:
        return False, "Usage: /editmsg [message_id] [new_message]"
        
    message_id = args[0]
    new_content = ' '.join(args[1:])
    
    # Check if message exists and belongs to user
    message_manager = MessageManager()
    msg = message_manager.get_message(message_id)
    
    if not msg:
        return False, f"Message '{message_id}' not found"
        
    if msg.sender_id != user_id:
        return False, "You can only edit your own messages"
        
    # Edit message
    success = message_manager.edit_message(message_id, new_content)
    
    if success:
        return True, "Message edited successfully"
    else:
        return False, "Failed to edit message"

def handle_delete(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Delete a specific message.
    Usage: /delete [message_id]
    """
    if not args:
        return False, "Usage: /delete [message_id]"
        
    message_id = args[0]
    
    # Check if message exists and belongs to user
    message_manager = MessageManager()
    msg = message_manager.get_message(message_id)
    
    if not msg:
        return False, f"Message '{message_id}' not found"
        
    # Allow deletion for message sender or group admin
    if msg.sender_id != user_id:
        # Check if in a group and user is admin
        if msg.group_id:
            group_manager = GroupManager()
            group = group_manager.get_group(msg.group_id)
            
            if not group or user_id not in group.members or group.members[user_id].value not in ["admin", "owner"]:
                return False, "You can only delete your own messages or messages in groups where you're an admin"
        else:
            return False, "You can only delete your own messages"
    
    # Delete message
    success = message_manager.delete_message(message_id)
    
    if success:
        return True, "Message deleted successfully"
    else:
        return False, "Failed to delete message"

def handle_clear(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Clear the chat screen.
    Usage: /clear
    """
    # This is just a client-side operation
    context.clear_screen()
    return True, "Screen cleared"

def handle_history(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    View chat history with a user or group.
    Usage: /history [user/group] [limit]
    """
    if not args:
        return False, "Usage: /history [user/group] [limit]"
        
    target = args[0]
    limit = 20
    if len(args) > 1 and args[1].isdigit():
        limit = int(args[1])
    
    message_manager = MessageManager()
    
    # Determine if this is a user or group
    group_manager = GroupManager()
    group = group_manager.get_group(target)
    
    if group:
        # It's a group
        if user_id not in group.members:
            return False, "You are not a member of this group"
            
        messages = message_manager.get_group_chat_history(target, limit)
        context.display_messages(messages, f"History for group: {group.name}")
        return True, f"Showing last {len(messages)} messages from group {group.name}"
    else:
        # Try as a user
        user_manager = UserManager()
        target_user = None
        
        # Try to get by ID first
        target_user = user_manager.get_user(target)
        
        # If not found, try by username
        if not target_user:
            users = user_manager.get_all_users()
            matching_users = [u for u in users if u.username == target]
            if matching_users:
                target_user = matching_users[0]
                
        if not target_user:
            return False, f"User or group '{target}' not found"
            
        private_chat = PrivateChat(user_id)
        messages = private_chat.get_chat_history(target_user.user_id, limit)
        context.display_messages(messages, f"History with: {target_user.display_name}")
        return True, f"Showing last {len(messages)} messages with {target_user.display_name}"

def handle_search(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Search for a specific message.
    Usage: /search [keyword]
    """
    if not args:
        return False, "Usage: /search [keyword]"
        
    keyword = ' '.join(args)
    
    message_manager = MessageManager()
    messages = message_manager.search_messages(keyword)
    
    if not messages:
        return False, f"No messages found containing '{keyword}'"
    
    context.display_messages(messages, f"Search results for: {keyword}")
    return True, f"Found {len(messages)} messages containing '{keyword}'"

def handle_pin(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Pin a message in the chat.
    Usage: /pin [message_id]
    """
    if not args:
        return False, "Usage: /pin [message_id]"
        
    message_id = args[0]
    
    message_manager = MessageManager()
    msg = message_manager.get_message(message_id)
    
    if not msg:
        return False, f"Message '{message_id}' not found"
    
    # For group messages, check if user has admin rights
    if msg.group_id:
        group_manager = GroupManager()
        group = group_manager.get_group(msg.group_id)
        
        if not group or user_id not in group.members or group.members[user_id].value not in ["admin", "owner"]:
            return False, "You need to be a group admin to pin messages"
    elif msg.sender_id != user_id and msg.recipient_id != user_id:
        return False, "You can only pin messages in your conversations"
    
    # Pin message
    success = message_manager.pin_message(message_id, True)
    
    if success:
        # Create a system notification about the pin
        if msg.group_id:
            notification = Message.create_notification(
                content=f"Message pinned by {context.current_user.username}",
                group_id=msg.group_id
            )
            message_manager.send_message(notification)
            
        return True, "Message pinned successfully"
    else:
        return False, "Failed to pin message"

def handle_unpin(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Unpin a message in the chat.
    Usage: /unpin [message_id]
    """
    if not args:
        return False, "Usage: /unpin [message_id]"
        
    message_id = args[0]
    
    message_manager = MessageManager()
    msg = message_manager.get_message(message_id)
    
    if not msg:
        return False, f"Message '{message_id}' not found"
        
    if not msg.is_pinned:
        return False, "This message is not pinned"
    
    # For group messages, check if user has admin rights
    if msg.group_id:
        group_manager = GroupManager()
        group = group_manager.get_group(msg.group_id)
        
        if not group or user_id not in group.members or group.members[user_id].value not in ["admin", "owner"]:
            return False, "You need to be a group admin to unpin messages"
    elif msg.sender_id != user_id and msg.recipient_id != user_id:
        return False, "You can only unpin messages in your conversations"
    
    # Unpin message
    success = message_manager.pin_message(message_id, False)
    
    if success:
        # Create a system notification about the unpin for groups
        if msg.group_id:
            notification = Message.create_notification(
                content=f"Message unpinned by {context.current_user.username}",
                group_id=msg.group_id
            )
            message_manager.send_message(notification)
            
        return True, "Message unpinned successfully"
    else:
        return False, "Failed to unpin message"

# Register all message commands
MESSAGE_COMMANDS = {
    "msg": handle_msg,
    "gmsg": handle_gmsg,
    "reply": handle_reply,
    "editmsg": handle_editmsg,
    "delete": handle_delete,
    "clear": handle_clear,
    "history": handle_history,
    "search": handle_search,
    "pin": handle_pin,
    "unpin": handle_unpin
}