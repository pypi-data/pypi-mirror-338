"""
Command handlers for group chat operations.
"""

from typing import List, Tuple
from datetime import datetime
from kalx.chat.group import GroupManager, MemberRole
from kalx.chat.message import MessageManager, Message
from kalx.auth.user import UserManager
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

# Initialize shared managers
group_manager = GroupManager()
message_manager = MessageManager()
user_manager = UserManager()

def handle_creategroup(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Create a new group chat."""
    if not args:
        return False, "Usage: /creategroup [group_name] [group_description]\nExample: /creategroup MyGroup Welcome to my group!"
    
    # Get current user_id from klx.json
    current_user = user_manager._load_from_json()
    if not current_user or not current_user.get("user_id"):
        return False, "User not authenticated"
    
    owner_id = current_user.get("user_id")
    
    # Parse name and optional description
    group_name = args[0]
    description = " ".join(args[1:]) if len(args) > 1 else "You are in the right place"
    
    if not group_name or not isinstance(group_name, str):
        return False, "Invalid group name"

    try:
        # Create and validate owner user if doesn't exist
        owner_data = user_manager.get_user(owner_id)
        if not owner_data:
            return False, "Failed to get user data"

        # Initialize groups list if not exists
        if "groups" not in owner_data:
            owner_data["groups"] = []
            user_manager.update_user(owner_id, owner_data)

        success, group_id = group_manager.create_group(
            name=group_name,
            owner_id=owner_id,
            description=description
        )
        
        if success:
            return True, f"Group '{group_name}' created successfully with ID: {group_id}"
        return False, f"Failed to create group: {group_id}"
    except Exception as e:
        logger.error(f"Error creating group: {str(e)}")
        return False, f"Failed to create group: {str(e)}"

def handle_joingroup(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """
    Handle the /joingroup command to join an existing group.

    Args:
        user_id: The ID of the user attempting to join the group.
        args: Command arguments, where the first argument is the group ID.
        context: Additional context for the command.

    Returns:
        Tuple[bool, str]: Success status and a message.
    """
    if not args or len(args) < 1:
        return False, "Usage: /joingroup [group_id]"

    group_id = args[0]
    group_manager = context.get("group_manager")

    if not group_manager:
        return False, "Group manager not initialized."

    try:
        group = group_manager.get_group(group_id)
        if not group:
            return False, f"Group with ID {group_id} does not exist."

        # Ensure group attributes are valid before comparison
        if group.name is None or group.owner_id is None:
            return False, "Group data is incomplete or corrupted."

        success = group_manager.add_user_to_group(user_id, group_id)
        if success:
            return True, f"Successfully joined group '{group.name}'."
        else:
            return False, "Failed to join group."
    except Exception as e:
        logger.error(f"Error in handle_joingroup: {e}")
        return False, f"An error occurred: {str(e)}"

def handle_leavegroup(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Leave a group chat."""
    if not args or len(args) != 1:
        return False, "Usage: /leavegroup [group_id]"
    
    group_id = args[0]
    group = group_manager.get_group(group_id)
    
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    if user_id not in group.members:
        return False, "You are not a member of this group"
    
    if group.owner_id == user_id:
        return False, "As the owner, you cannot leave the group. Transfer ownership first or delete the group."
    
    # Remove user from group
    del group.members[user_id]
    success = group_manager.update_group(group)
    
    if success:
        # Remove group from user's groups
        user = user_manager.get_user(user_id)
        if user and group_id in user.groups:
            user.groups.remove(group_id)
            user_manager.update_user(user)
            
        # Send notification
        user_info = user_manager.get_user(user_id)
        display_name = user_info.display_name if user_info else user_id
        
        notification = Message.create_notification(
            f"{display_name} has left the group",
            group_id=group_id
        )
        message_manager.send_message(notification)
        
        return True, f"Successfully left group '{group.name}'"
    return False, "Failed to leave group"

def handle_invite(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Invite a user to a group chat."""
    if not args or len(args) != 2:
        return False, "Usage: /invite [user] [group_id]"
    
    invited_user_id, group_id = args
    
    invited_user = user_manager.get_user(invited_user_id)
    if not invited_user:
        return False, f"User {invited_user_id} not found"
    
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    if user_id not in group.members:
        return False, "You are not a member of this group"
    
    if group.members[user_id] not in [MemberRole.OWNER, MemberRole.ADMIN]:
        return False, "You need to be an admin or owner to invite users"
    
    if invited_user_id in group.members:
        return False, f"User {invited_user_id} is already a member of this group"
    
    invitation_content = f"You've been invited to join group '{group.name}' (ID: {group_id}). To join, type /joingroup {group_id}"
    invitation = Message.create_notification(
        content=invitation_content,
        recipient_id=invited_user_id
    )
    message_manager.send_message(invitation)
    
    current_user = user_manager.get_user(user_id)
    current_display_name = current_user.display_name if current_user else user_id
    
    invited_display_name = invited_user.display_name if invited_user else invited_user_id
    
    notification = Message.create_notification(
        f"{current_display_name} has invited {invited_display_name} to the group",
        group_id=group_id
    )
    message_manager.send_message(notification)
    
    return True, f"Invitation sent to {invited_display_name}"

def handle_setgroupname(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Change a group's name."""
    if not args or len(args) < 2:
        return False, "Usage: /setgroupname [group_id] [new_name]"
    
    group_id = args[0]
    new_name = " ".join(args[1:])
    
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    if user_id not in group.members:
        return False, "You are not a member of this group"
    
    if group.members[user_id] not in [MemberRole.OWNER, MemberRole.ADMIN]:
        return False, "You need to be an admin or owner to change the group name"
    
    old_name = group.name
    group.name = new_name
    success = group_manager.update_group(group)
    
    if success:
        user_info = user_manager.get_user(user_id)
        display_name = user_info.display_name if user_info else user_id
        
        notification = Message.create_notification(
            f"Group name changed from '{old_name}' to '{new_name}' by {display_name}",
            group_id=group_id
        )
        message_manager.send_message(notification)
        
        return True, f"Group name successfully changed to '{new_name}'"
    return False, "Failed to change group name"

def handle_listgroups(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Show a list of all groups the user belongs to."""
    user = user_manager.get_user(user_id)
    if not user:
        return False, "Failed to get user information"
    
    if not user.groups:
        return True, "You are not a member of any groups"
    
    groups_info = []
    for group_id in user.groups:
        group = group_manager.get_group(group_id)
        if group:
            role = group.members.get(user_id, MemberRole.MEMBER).value.capitalize()
            groups_info.append(f"- {group.name} (ID: {group.group_id}) - Role: {role}")
    
    if not groups_info:
        return True, "You are not a member of any groups"
    
    response = "Your groups:\n" + "\n".join(groups_info)
    return True, response

def handle_mute(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Mute notifications for a group chat."""
    if not args or len(args) != 1:
        return False, "Usage: /mute [group_id]"
    
    group_id = args[0]
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    if user_id not in group.members:
        return False, "You are not a member of this group"
    
    user = user_manager.get_user(user_id)
    if not user:
        return False, "Failed to get user information"
    
    if "muted_groups" not in user.settings:
        user.settings["muted_groups"] = []
    
    if group_id in user.settings["muted_groups"]:
        return False, f"Group '{group.name}' is already muted"
    
    user.settings["muted_groups"].append(group_id)
    success = user_manager.update_user(user)
    
    if success:
        return True, f"Notifications for group '{group.name}' have been muted"
    return False, "Failed to mute group"

def handle_unmute(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Unmute notifications for a group chat."""
    if not args or len(args) != 1:
        return False, "Usage: /unmute [group_id]"
    
    group_id = args[0]
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    user = user_manager.get_user(user_id)
    if not user:
        return False, "Failed to get user information"
    
    if "muted_groups" not in user.settings or group_id not in user.settings["muted_groups"]:
        return False, f"Group '{group.name}' is not muted"
    
    user.settings["muted_groups"].remove(group_id)
    success = user_manager.update_user(user)
    
    if success:
        return True, f"Notifications for group '{group.name}' have been unmuted"
    return False, "Failed to unmute group"

def handle_gmsg(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """Send a message to a group chat."""
    if not args or len(args) < 2:
        return False, "Usage: /gmsg [group_id] [message]"
    
    group_id = args[0]
    content = " ".join(args[1:])
    
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    if user_id not in group.members:
        return False, "You are not a member of this group"
    
    message = Message.create_text_message(
        sender_id=user_id,
        content=content,
        group_id=group_id
    )
    
    success = message_manager.send_message(message)
    
    if success:
        return True, "Message sent to group"
    return False, "Failed to send message to group"

def handle_kick(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """
    Remove a user from a group chat.
    Usage: /kick [user] [group_id]
    """
    if not args or len(args) != 2:
        return False, "Usage: /kick [user] [group_id]"
    
    target_user_id, group_id = args
    
    # Get group info
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    # Check permissions
    if user_id not in group.members:
        return False, "You are not a member of this group"
        
    if group.members[user_id] not in [MemberRole.OWNER, MemberRole.ADMIN]:
        return False, "You need to be an admin or owner to kick users"
    
    # Check target user
    target_user = user_manager.get_user(target_user_id)
    if not target_user:
        return False, f"User {target_user_id} not found"
    
    if target_user_id not in group.members:
        return False, f"User {target_user_id} is not a member of this group"
    
    if target_user_id == group.owner_id:
        return False, "Cannot kick the group owner"
    
    # If admin trying to kick admin
    if (group.members[user_id] == MemberRole.ADMIN and 
        group.members[target_user_id] == MemberRole.ADMIN):
        return False, "Admins cannot kick other admins"
    
    # Remove member from group
    success, result = group_manager.remove_member(group_id, target_user_id, user_id)
    
    if success:
        # Get display names
        user_info = user_manager.get_user(user_id)
        target_info = user_manager.get_user(target_user_id)
        kicker_name = user_info.display_name if user_info else user_id
        target_name = target_info.display_name if target_info else target_user_id
        
        # Send group notification
        notification = Message.create_notification(
            f"{target_name} was kicked from the group by {kicker_name}",
            group_id=group_id
        )
        message_manager.send_message(notification)
        
        # Send private notification to kicked user
        private_notification = Message.create_notification(
            f"You were removed from group '{group.name}' by {kicker_name}",
            recipient_id=target_user_id
        )
        message_manager.send_message(private_notification)
        
        return True, f"Successfully kicked {target_name} from the group"
    return False, "Failed to kick user from group"

def handle_setadmin(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """
    Promote a user to admin in a group.
    Usage: /setadmin [user] [group_id]
    """
    if not args or len(args) != 2:
        return False, "Usage: /setadmin [user] [group_id]"
    
    target_user_id, group_id = args
    
    # Get group info
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    # Check permissions
    if user_id not in group.members:
        return False, "You are not a member of this group"
        
    if user_id != group.owner_id:
        return False, "Only the group owner can promote members to admin"
    
    # Check target user
    if target_user_id not in group.members:
        return False, f"User {target_user_id} is not a member of this group"
    
    if target_user_id == group.owner_id:
        return False, "The owner is already an admin"
    
    if group.members[target_user_id] == MemberRole.ADMIN:
        return False, "This user is already an admin"
    
    # Change role to admin
    success, result = group_manager.change_member_role(group_id, target_user_id, MemberRole.ADMIN, user_id)
    
    if success:
        # Get display names
        user_info = user_manager.get_user(target_user_id)
        display_name = user_info.display_name if user_info else target_user_id
        
        # Send notification
        notification = Message.create_notification(
            f"{display_name} has been promoted to admin",
            group_id=group_id
        )
        message_manager.send_message(notification)
        
        return True, f"Successfully promoted {display_name} to admin"
    return False, "Failed to promote user to admin"

def handle_removeadmin(user_id: str, args: List[str], context) -> Tuple[bool, str]:
    """
    Remove admin role from a user in a group.
    Usage: /removeadmin [user] [group_id]
    """
    if not args or len(args) != 2:
        return False, "Usage: /removeadmin [user] [group_id]"
    
    target_user_id, group_id = args
    
    # Get group info
    group = group_manager.get_group(group_id)
    if not group:
        return False, f"Group with ID {group_id} not found"
    
    # Check permissions
    if user_id not in group.members:
        return False, "You are not a member of this group"
        
    if user_id != group.owner_id:
        return False, "Only the group owner can demote admins"
    
    # Check target user
    if target_user_id not in group.members:
        return False, f"User {target_user_id} is not a member of this group"
    
    if target_user_id == group.owner_id:
        return False, "Cannot demote the group owner"
    
    if group.members[target_user_id] != MemberRole.ADMIN:
        return False, "This user is not an admin"
    
    # Change role to member
    success, result = group_manager.change_member_role(group_id, target_user_id, MemberRole.MEMBER, user_id)
    
    if success:
        # Get display names
        user_info = user_manager.get_user(target_user_id)
        display_name = user_info.display_name if user_info else target_user_id
        
        # Send notification
        notification = Message.create_notification(
            f"{display_name} has been demoted from admin",
            group_id=group_id
        )
        message_manager.send_message(notification)
        
        return True, f"Successfully removed admin role from {display_name}"
    return False, "Failed to remove admin role"