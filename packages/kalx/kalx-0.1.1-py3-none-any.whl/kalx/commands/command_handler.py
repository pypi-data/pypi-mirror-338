"""
Main command handler that routes commands to specific handlers.
"""

from typing import Dict, Callable, Tuple, Any, List
import shlex
from kalx.utils.logger import get_logger
from kalx.commands.admin_commands import AdminCommands

logger = get_logger(__name__)

# Define command groups
COMMAND_GROUPS = {
    "User": {
        "login": "Login to account",
        "register": "Create new account",
        "logout": "Logout from current session",
        "whoami": "Show current user info",
        "setname": "Change display name",
        "setstatus": "Set online status",
        "changepassword": "Change password",
        "deleteaccount": "Delete account",
        "acceptfriend": "Accept friend request",
        "rejectfriend": "Reject friend request"
    },
    "Chat": {
        "msg": "Send private message",
        "gmsg": "Send group message",
        "reply": "Reply to message",
        "editmsg": "Edit sent message",
        "delete": "Delete message",
        "clear": "Clear chat screen",
        "history": "View chat history",
        "search": "Search messages"
    },
    "Groups": {
        "creategroup": "Create new group",
        "joingroup": "Join existing group",
        "leavegroup": "Leave group",
        "invite": "Invite user to group",
        "kick": "Remove user from group",
        "setadmin": "Set user as admin",
        "listgroups": "List your groups"
    },
    "Social": {
        "friend": "Add friend",
        "unfriend": "Remove friend",
        "block": "Block user",
        "unblock": "Unblock user",
        "listfriends": "List friends",
        "onlist": "Show online users",
        "offlist": "Show offline users"
    },
    "System": {
        "help": "Show this help",
        "version": "Show version",
        "uptime": "Show uptime",
        "settings": "Show/edit settings",
        "export": "Export chat history",
        "import": "Import chat history",
        "exit": "Exit application"
    }
}

class CommandContext:
    """Context object passed to command handlers."""
    
    def __init__(self, user_id=None, session=None):
        """Initialize command context."""
        self.current_user = user_id
        self.session = session
        self.current_chat = None
        self.current_group = None
        self.console = None

class CommandHandler:
    """Main command handler for parsing and executing commands."""
    
    def __init__(self, console=None):
        """Initialize the command handler."""
        self.commands: Dict[str, Callable] = {}
        self.context = CommandContext()
        self.console = console
        self.context.console = console
        self.admin_commands = None  # Will be initialized when user is set
        self._register_commands()

    def _register_commands(self):
        """Register all available commands."""
        # User Management Commands
        from kalx.commands.user_commands import (
            handle_register, handle_login, handle_logout, handle_whoami,
            handle_setname, handle_setstatus, handle_changepassword,
            handle_deleteaccount, handle_block, handle_unblock,
            handle_friend, handle_unfriend, handle_listfriends,
            handle_onlist, handle_offlist, handle_alllist, handle_report,
            handle_accept_friend, handle_rejectfriend
        )
        # Message Commands
        from kalx.commands.message_commands import (
            handle_msg, handle_gmsg, handle_reply, handle_editmsg,
            handle_delete, handle_clear, handle_history, handle_search,
            handle_pin, handle_unpin
        )
        # Group Commands
        from kalx.commands.group_commands import (
            handle_creategroup, handle_joingroup, handle_leavegroup,
            handle_invite, handle_kick, handle_setadmin, handle_removeadmin,
            handle_setgroupname, handle_listgroups, handle_mute, handle_unmute
        )
        # System Commands - import the standalone functions
        from kalx.commands.system_commands import (
            handle_help, handle_version, handle_uptime, handle_debug,
            handle_backup, handle_restore, handle_export, handle_import,
            handle_exit, handle_settings, handle_settheme, handle_setfont,
            handle_setcolor, handle_setnotif, handle_setpeep, handle_setautoscroll
        )
        # User Management
        self.commands["/register"] = handle_register
        self.commands["/login"] = handle_login
        self.commands["/logout"] = handle_logout
        self.commands["/whoami"] = handle_whoami
        self.commands["/setname"] = handle_setname
        self.commands["/setstatus"] = handle_setstatus
        self.commands["/changepassword"] = handle_changepassword
        self.commands["/deleteaccount"] = handle_deleteaccount
        self.commands["/block"] = handle_block
        self.commands["/unblock"] = handle_unblock
        self.commands["/friend"] = handle_friend
        self.commands["/unfriend"] = handle_unfriend
        self.commands["/listfriends"] = handle_listfriends
        self.commands["/onlist"] = handle_onlist
        self.commands["/offlist"] = handle_offlist
        self.commands["/alllist"] = handle_alllist
        self.commands["/report"] = handle_report
        self.commands["/acceptfriend"] = handle_accept_friend
        self.commands["/rejectfriend"] = handle_rejectfriend
        
        # Messaging
        self.commands["/msg"] = handle_msg
        self.commands["/gmsg"] = handle_gmsg
        self.commands["/reply"] = handle_reply
        self.commands["/editmsg"] = handle_editmsg
        self.commands["/delete"] = handle_delete
        self.commands["/clear"] = handle_clear
        self.commands["/history"] = handle_history
        self.commands["/search"] = handle_search
        self.commands["/pin"] = handle_pin
        self.commands["/unpin"] = handle_unpin
        
        # Group
        self.commands["/creategroup"] = handle_creategroup
        self.commands["/joingroup"] = handle_joingroup
        self.commands["/leavegroup"] = handle_leavegroup
        self.commands["/invite"] = handle_invite
        self.commands["/kick"] = handle_kick
        self.commands["/setadmin"] = handle_setadmin
        self.commands["/removeadmin"] = handle_removeadmin
        self.commands["/setgroupname"] = handle_setgroupname
        self.commands["/listgroups"] = handle_listgroups
        self.commands["/mute"] = handle_mute
        self.commands["/unmute"] = handle_unmute
        
        # System
        self.commands["/help"] = handle_help
        self.commands["/version"] = handle_version
        self.commands["/uptime"] = handle_uptime
        self.commands["/debug"] = handle_debug
        self.commands["/backup"] = handle_backup
        self.commands["/restore"] = handle_restore
        self.commands["/export"] = handle_export
        self.commands["/import"] = handle_import
        self.commands["/exit"] = handle_exit
        self.commands["/settings"] = handle_settings
        self.commands["/settheme"] = handle_settheme
        self.commands["/setfont"] = handle_setfont
        self.commands["/setcolor"] = handle_setcolor
        self.commands["/setnotif"] = handle_setnotif
        self.commands["/setpeep"] = handle_setpeep
        self.commands["/setautoscroll"] = handle_setautoscroll

        # Register admin commands with wrapper functions
        def wrap_admin_command(method_name):
            def wrapper(user_id, args, context):
                if self.admin_commands is None:
                    self.admin_commands = AdminCommands(user_id)
                method = getattr(self.admin_commands, method_name)
                return method(args)
            return wrapper

        # Register admin commands
        self.commands["/ban"] = wrap_admin_command("handle_ban")
        self.commands["/unban"] = wrap_admin_command("handle_unban")
        self.commands["/muteuser"] = wrap_admin_command("handle_mute_user")
        self.commands["/unmuteuser"] = wrap_admin_command("handle_unmute_user")
        self.commands["/shutdown"] = wrap_admin_command("handle_shutdown")
        self.commands["/announce"] = wrap_admin_command("handle_announce")
    
    def is_command(self, text: str) -> bool:
        """Check if text is a command."""
        return text.startswith("/")
    
    def set_user(self, user_id):
        """Set the current user in the context."""
        self.context.current_user = user_id
        # Reinitialize admin commands with new user
        self.admin_commands = AdminCommands(user_id) if user_id else None
    
    def set_session(self, session):
        """Set the current session object in the context."""
        self.context.session = session
    
    def set_current_chat(self, user_id):
        """Set the current chat partner."""
        self.context.current_chat = user_id
    
    def set_current_group(self, group_id):
        """Set the current group."""
        self.context.current_group = group_id
    
    def handle_command(self, user_id: str, args: List[str], context: CommandContext) -> Tuple[bool, str]:
        """
        Parse and execute a command.

        Args:
            user_id: The ID of the user executing the command
            args: The command arguments
            context: The command context

        Returns:
            Tuple[bool, str]: Success status and command output
        """
        try:
            if not args:
                return False, "Empty command"

            command = args[0].lower()
            command_args = args[1:] if len(args) > 1 else []

            # Find the command handler
            handler = self.commands.get(f"/{command}")
            if not handler:
                return False, f"Unknown command: {command}"

            # Execute the command
            logger.debug(f"Executing command: {command} with args: {command_args}")
            return handler(user_id, command_args, context)

        except Exception as e:
            logger.error(f"Command execution error: {str(e)}")
            return False, f"Error executing command: {str(e)}"
    
    def get_all_commands(self) -> Dict[str, str]:
        """Get all available commands with descriptions."""
        all_commands = {}
        for group in COMMAND_GROUPS.values():
            all_commands.update(group)
        return all_commands
    
    def get_command_help(self, command: str) -> str:
        """Get detailed help for a specific command."""
        # Remove leading slash if present
        command = command.lstrip('/')
        
        # Search in all groups
        for group_name, commands in COMMAND_GROUPS.items():
            if command in commands:
                # Get the handler's docstring
                handler = self.commands.get(f"/{command}")
                if handler and handler.__doc__:
                    return f"[Group: {group_name}]\n{handler.__doc__.strip()}"
                return f"[Group: {group_name}]\n{commands[command]}"
                
        return f"No help available for unknown command: {command}"

