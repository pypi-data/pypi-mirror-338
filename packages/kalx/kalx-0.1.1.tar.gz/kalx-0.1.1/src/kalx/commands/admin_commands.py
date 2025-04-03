"""
Admin-level commands for the kalX hacker console chat.
"""

from typing import List, Tuple, Any
from datetime import datetime, timedelta
from kalx.auth.user import UserManager, UserStatus
from kalx.utils.config import get_config
from kalx.chat.message import Message, MessageManager
from kalx.utils.logger import get_logger

logger = get_logger(__name__)

class AdminCommands:
    """Handles administrative commands."""
    
    def __init__(self, user_id: str):
        """Initialize admin commands handler."""
        self.user_id = user_id
        self.user_manager = UserManager()
        self.message_manager = MessageManager()
        self.config = get_config()
        
    def _is_admin(self) -> bool:
        """Check if current user is an admin."""
        admin_users = self.config.get("admin", "users", fallback="").split(",")
        return self.user_id in admin_users
        
    def handle_ban(self, args: List[str]) -> Tuple[bool, str]:
        """
        Ban a user from the chat.
        Usage: /ban [user_id] [reason]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        if len(args) < 2:
            return False, "Usage: /ban [user_id] [reason]"
            
        target_id = args[0]
        reason = " ".join(args[1:])
        
        user = self.user_manager.get_user(target_id)
        if not user:
            return False, f"User {target_id} not found"
            
        # Add to banned users in config
        banned_users = self.config.get("admin", "banned_users", fallback="").split(",")
        if target_id not in banned_users:
            banned_users.append(target_id)
            self.config.set("admin", "banned_users", ",".join(banned_users))
            
        # Update user status
        self.user_manager.update_status(target_id, UserStatus.OFFLINE)
        
        # Log the ban
        logger.warning(f"User {target_id} banned by {self.user_id} for: {reason}")
        
        return True, f"User {user.username} has been banned"
        
    def handle_unban(self, args: List[str]) -> Tuple[bool, str]:
        """
        Unban a previously banned user.
        Usage: /unban [user_id]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        if not args:
            return False, "Usage: /unban [user_id]"
            
        target_id = args[0]
        
        # Remove from banned users in config
        banned_users = self.config.get("admin", "banned_users", fallback="").split(",")
        if target_id in banned_users:
            banned_users.remove(target_id)
            self.config.set("admin", "banned_users", ",".join(banned_users))
            
        logger.info(f"User {target_id} unbanned by {self.user_id}")
        return True, f"User {target_id} has been unbanned"
        
    def handle_mute_user(self, args: List[str]) -> Tuple[bool, str]:
        """
        Temporarily mute a user.
        Usage: /muteuser [user_id] [duration_minutes] [reason]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        if len(args) < 3:
            return False, "Usage: /muteuser [user_id] [duration_minutes] [reason]"
            
        target_id = args[0]
        try:
            duration = int(args[1])
        except ValueError:
            return False, "Duration must be a number of minutes"
            
        reason = " ".join(args[2:])
        
        user = self.user_manager.get_user(target_id)
        if not user:
            return False, f"User {target_id} not found"
            
        # Set mute expiry in user's settings
        mute_until = datetime.now() + timedelta(minutes=duration)
        user.settings["muted_until"] = mute_until.isoformat()
        user.settings["mute_reason"] = reason
        
        self.user_manager.update_user(user)
        logger.warning(f"User {target_id} muted by {self.user_id} for {duration} minutes")
        
        return True, f"User {user.username} has been muted for {duration} minutes"
        
    def handle_unmute_user(self, args: List[str]) -> Tuple[bool, str]:
        """
        Unmute a previously muted user.
        Usage: /unmuteuser [user_id]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        if not args:
            return False, "Usage: /unmuteuser [user_id]"
            
        target_id = args[0]
        user = self.user_manager.get_user(target_id)
        if not user:
            return False, f"User {target_id} not found"
            
        if "muted_until" in user.settings:
            del user.settings["muted_until"]
            del user.settings["mute_reason"]
            self.user_manager.update_user(user)
            
        logger.info(f"User {target_id} unmuted by {self.user_id}")
        return True, f"User {user.username} has been unmuted"
        
    def handle_announce(self, args: List[str]) -> Tuple[bool, str]:
        """
        Broadcast an announcement to all users.
        Usage: /announce [message]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        if not args:
            return False, "Usage: /announce [message]"
            
        announcement = " ".join(args)
        
        # Create system message
        msg = Message.create_system_message(f"[ANNOUNCEMENT] {announcement}")
        self.message_manager.send_message(msg)
        
        logger.info(f"Announcement sent by {self.user_id}: {announcement}")
        return True, "Announcement broadcast to all users"
        
    def handle_shutdown(self, args: List[str]) -> Tuple[bool, str]:
        """
        Shut down the chat server.
        Usage: /shutdown [reason]
        """
        if not self._is_admin():
            return False, "This command requires administrator privileges"
            
        reason = " ".join(args) if args else "Server maintenance"
        
        # Send shutdown warning to all users
        warning = Message.create_system_message(
            f"[SYSTEM] Server shutting down in 60 seconds. Reason: {reason}"
        )
        self.message_manager.send_message(warning)
        
        logger.warning(f"Server shutdown initiated by {self.user_id}")
        return True, "Server shutdown sequence initiated"

# Create standalone functions that wrap the AdminCommands class
def create_admin_handler(method_name: str) -> callable:
    def handler(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
        admin = AdminCommands(user_id)
        method = getattr(admin, method_name)
        return method(args)
    return handler

# Export standalone function versions
handle_ban = create_admin_handler("handle_ban")
handle_unban = create_admin_handler("handle_unban")
handle_mute_user = create_admin_handler("handle_mute_user")
handle_unmute_user = create_admin_handler("handle_unmute_user")
handle_shutdown = create_admin_handler("handle_shutdown")
handle_announce = create_admin_handler("handle_announce")
