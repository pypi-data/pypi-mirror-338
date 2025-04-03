"""
System-level commands for the kalX hacker console chat.
"""

import os
import sys
import json
import csv
import time
import datetime
import platform
from typing import Tuple, Dict, List, Any
import subprocess
import shutil
from pathlib import Path

from kalx.utils.logger import get_logger
from kalx.utils.config import get_config
from kalx.chat.message import MessageManager
from kalx.ui.console import ConsoleUI
from kalx.commands.command_handler import COMMAND_GROUPS

logger = get_logger(__name__)

class SystemCommands:
    """
    Implements system-level commands for kalX chat application.
    """
    
    def __init__(self, console: ConsoleUI, user_id: str = None):
        """
        Initialize the system commands handler.
        
        Args:
            console: Reference to the console UI
            user_id: ID of the current user (if logged in)
        """
        self.console = console
        self.user_id = user_id
        self.message_manager = MessageManager()
        self.start_time = time.time()
        self.config = get_config()
        self.data_dir = self._get_data_directory()
        
    def _get_data_directory(self) -> Path:
        """Get or create the app data directory."""
        home = Path.home()
        data_dir = home / ".kalx"
        if not data_dir.exists():
            data_dir.mkdir(parents=True)
        return data_dir
        
    def handle_help(self, args: List[str]) -> Tuple[bool, str]:
        """Show help information for available commands."""
        if len(args) > 0:
            command = args[0].lower().strip('/')
            
            # Search in all command groups
            for group_name, commands in COMMAND_GROUPS.items():
                if command in commands:
                    handler = self.commands.get(f"/{command}")
                    if handler and handler.__doc__:
                        return True, f"\n[bold cyan]Command: /{command}[/bold cyan]\n[Group: {group_name}]\n\n{handler.__doc__.strip()}"
                    return True, f"\n[bold cyan]Command: /{command}[/bold cyan]\n[Group: {group_name}]\n\n{commands[command]}"
            
            return False, f"Command '/{command}' not found. Type /help for a list of all commands."

        # Show all available commands with enhanced styling
        help_text = """
╭──────────────────────────────────────────╮
│     [bold green]kalX Command Reference Guide[/bold green]     │
╰──────────────────────────────────────────╯
"""
        for group_name, commands in COMMAND_GROUPS.items():
            help_text += f"\n[bold green]╭─ {group_name} Commands ──────────────────────╮[/bold green]\n"
            for cmd_name, desc in commands.items():
                help_text += f"[bold green]│[/bold green] [cyan]/{cmd_name:<15}[/cyan] {desc}\n"
            help_text += "[bold green]╰────────────────────────────────────────╯[/bold green]\n"
        
        help_text += """
[bold yellow]Tips:[/bold yellow]
[green]>>[/green] Use [cyan]/help <command>[/cyan] for detailed information
[green]>>[/green] Commands are case-insensitive
[green]>>[/green] Use [cyan]Tab[/cyan] for command completion
"""
        return True, help_text
        
    def handle_version(self, args: List[str]) -> Tuple[bool, str]:
        """
        Show the current version of kalX.
        
        Usage: /version
        
        Args:
            args: Command arguments
            
        Returns:
            Tuple[bool, str]: Success status and version information
        """
        from kalx import __version__
        
        python_version = platform.python_version()
        system_info = f"{platform.system()} {platform.release()}"
        
        version_info = (
            f"\n[bold green]kalX Hacker Console Chat v{__version__}[/bold green]\n\n"
            f"Python: {python_version}\n"
            f"System: {system_info}\n"
            f"Build date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
        )
        
        return True, version_info
        
    def handle_uptime(self, args: List[str]) -> Tuple[bool, str]:
        """
        Show how long the chat application has been running.
        
        Usage: /uptime
        
        Args:
            args: Command arguments
            
        Returns:
            Tuple[bool, str]: Success status and uptime information
        """
        uptime_seconds = int(time.time() - self.start_time)
        
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        uptime_str = f"\n[bold green]System Uptime:[/bold green] "
        
        if days > 0:
            uptime_str += f"{days} days, "
        if hours > 0 or days > 0:
            uptime_str += f"{hours} hours, "
            
        uptime_str += f"{minutes} minutes, {seconds} seconds\n"
        
        return True, uptime_str
        
    def handle_debug(self, args: List[str]) -> Tuple[bool, str]:
        """
        Display system logs for debugging.
        
        Usage: /debug [lines=50]
        
        Args:
            args: Command arguments with optional line count
            
        Returns:
            Tuple[bool, str]: Success status and debug information
        """
        if not self.user_id:
            return False, "You must be logged in to use this command."
            
        # Check if the user has admin rights in the config
        admin_users = self.config.get("admin", "users", fallback="").split(",")
        if self.user_id not in admin_users:
            return False, "This command requires administrator privileges."
            
        # Get log file path
        log_file = self.config.get("logging", "file_path", fallback=str(self.data_dir / "kalx.log"))
        
        # Determine number of lines to show
        lines = 50
        if len(args) > 0:
            try:
                lines = int(args[0])
            except ValueError:
                return False, f"Invalid line count: {args[0]}, must be a number."
                
        # Read the log file
        try:
            if not os.path.exists(log_file):
                return False, f"Log file not found: {log_file}"
                
            with open(log_file, 'r') as f:
                log_lines = f.readlines()
                
            # Get the last N lines
            last_lines = log_lines[-lines:] if len(log_lines) > lines else log_lines
            
            debug_info = "\n[bold green]System Log (last {lines} lines):[/bold green]\n\n"
            for line in last_lines:
                # Highlight errors and warnings
                if "ERROR" in line:
                    debug_info += f"[bold red]{line}[/bold red]"
                elif "WARNING" in line:
                    debug_info += f"[bold yellow]{line}[/bold yellow]"
                else:
                    debug_info += line
                    
            return True, debug_info
            
        except Exception as e:
            logger.error(f"Error reading log file: {str(e)}")
            return False, f"Error reading log file: {str(e)}"
            
    def handle_backup(self, args: List[str]) -> Tuple[bool, str]:
        """
        Backup chat history and user data.
        
        Usage: /backup [destination]
        
        Args:
            args: Command arguments with optional destination path
            
        Returns:
            Tuple[bool, str]: Success status and backup information
        """
        if not self.user_id:
            return False, "You must be logged in to use this command."
            
        # Determine backup location
        backup_dir = self.data_dir / "backups"
        if len(args) > 0:
            backup_dir = Path(args[0])
            
        # Create the backup directory if it doesn't exist
        try:
            backup_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return False, f"Failed to create backup directory: {str(e)}"
            
        # Generate a timestamp for the backup
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"kalx_backup_{timestamp}.json"
        
        try:
            # TODO: In a real implementation, we would use Firebase Admin SDK to export data
            # For this example, we'll simulate a backup with a placeholder
            
            # Get user data
            from kalx.auth.user import UserManager
            user_manager = UserManager()
            user = user_manager.get_user(self.user_id)
            
            # Get chat history
            messages = self.message_manager.get_private_chat_history(self.user_id, None, limit=1000)
            
            # Create backup data
            backup_data = {
                "user": {
                    "user_id": user.user_id,
                    "username": user.username,
                    "settings": user.settings
                },
                "messages": [
                    {
                        "id": msg.id,
                        "content": msg.content,
                        "timestamp": msg.timestamp.isoformat(),
                        "sender_id": msg.sender_id,
                        "recipient_id": msg.recipient_id,
                        "group_id": msg.group_id
                    }
                    for msg in messages if not msg.is_deleted
                ],
                "backup_date": timestamp
            }
            
            # Write backup to file
            with open(backup_file, 'w') as f:
                json.dump(backup_data, f, indent=2)
                
            return True, f"Backup created successfully at: {backup_file}"
            
        except Exception as e:
            logger.error(f"Backup failed: {str(e)}")
            return False, f"Backup failed: {str(e)}"
            
    def handle_restore(self, args: List[str]) -> Tuple[bool, str]:
        """
        Restore chat history from a backup.
        
        Usage: /restore <backup_file>
        
        Args:
            args: Command arguments with backup file path
            
        Returns:
            Tuple[bool, str]: Success status and restore information
        """
        if not self.user_id:
            return False, "You must be logged in to use this command."
            
        if len(args) == 0:
            return False, "Missing backup file. Usage: /restore <backup_file>"
            
        backup_file = Path(args[0])
        if not backup_file.exists():
            # Check if it might be in the default backup directory
            default_backup = self.data_dir / "backups" / args[0]
            if default_backup.exists():
                backup_file = default_backup
            else:
                return False, f"Backup file not found: {backup_file}"
                
        try:
            # Load backup data
            with open(backup_file, 'r') as f:
                backup_data = json.load(f)
                
            # TODO: In a real implementation, we would restore the data to Firebase
            # For this example, we'll simulate a restore with a placeholder
            
            message_count = len(backup_data.get("messages", []))
            
            return True, f"Restored {message_count} messages from backup: {backup_file}"
            
        except Exception as e:
            logger.error(f"Restore failed: {str(e)}")
            return False, f"Restore failed: {str(e)}"
            
    def handle_export(self, args: List[str]) -> Tuple[bool, str]:
        """
        Export chat logs to a file in JSON, TXT, or CSV format.
        
        Usage: /export [format=json] [destination]
        
        Args:
            args: Command arguments with optional format and destination
            
        Returns:
            Tuple[bool, str]: Success status and export information
        """
        if not self.user_id:
            return False, "You must be logged in to use this command."
            
        # Parse arguments
        export_format = "json"
        export_path = None
        
        if len(args) > 0:
            if args[0].lower() in ["json", "txt", "csv"]:
                export_format = args[0].lower()
                if len(args) > 1:
                    export_path = args[1]
            else:
                export_path = args[0]
                
        if not export_path:
            # Generate a default export path
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            export_path = self.data_dir / "exports" / f"kalx_export_{timestamp}.{export_format}"
            
        export_path = Path(export_path)
        
        # Create the export directory if it doesn't exist
        export_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Get chat history
            all_messages = []
            
            # Get private messages
            from kalx.auth.user import UserManager
            user_manager = UserManager()
            user = user_manager.get_user(self.user_id)
            
            # For each friend or user you've chatted with
            for friend_id in user.friends:
                messages = self.message_manager.get_private_chat_history(self.user_id, friend_id)
                all_messages.extend(messages)
                
            # Get group messages
            for group_id in user.groups:
                group_messages = self.message_manager.get_group_chat_history(group_id)
                all_messages.extend(group_messages)
                
            # Sort messages by timestamp
            all_messages.sort(key=lambda msg: msg.timestamp)
            
            # Format messages for export
            formatted_messages = []
            for msg in all_messages:
                if msg.is_deleted:
                    continue
                    
                sender = user_manager.get_user(msg.sender_id)
                sender_name = sender.display_name if sender else msg.sender_id
                
                formatted_msg = {
                    "timestamp": msg.timestamp.isoformat(),
                    "sender": sender_name,
                    "content": msg.content,
                    "type": msg.message_type.value
                }
                
                if msg.group_id:
                    from kalx.chat.group import GroupManager
                    group_manager = GroupManager()
                    group = group_manager.get_group(msg.group_id)
                    formatted_msg["channel"] = f"group:{group.name}" if group else f"group:{msg.group_id}"
                elif msg.recipient_id:
                    recipient = user_manager.get_user(msg.recipient_id)
                    recipient_name = recipient.display_name if recipient else msg.recipient_id
                    formatted_msg["channel"] = f"private:{recipient_name}"
                    
                formatted_messages.append(formatted_msg)
                
            # Write messages to file in the specified format
            if export_format == "json":
                with open(export_path, 'w') as f:
                    json.dump(formatted_messages, f, indent=2)
                    
            elif export_format == "txt":
                with open(export_path, 'w') as f:
                    for msg in formatted_messages:
                        channel = msg.get("channel", "")
                        timestamp = datetime.datetime.fromisoformat(msg["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"[{timestamp}] [{channel}] {msg['sender']}: {msg['content']}\n")
                        
            elif export_format == "csv":
                with open(export_path, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=["timestamp", "channel", "sender", "type", "content"])
                    writer.writeheader()
                    writer.writerows(formatted_messages)
                    
            return True, f"Exported {len(formatted_messages)} messages to {export_path}"
            
        except Exception as e:
            logger.error(f"Export failed: {str(e)}")
            return False, f"Export failed: {str(e)}"
            
    def handle_import(self, args: List[str]) -> Tuple[bool, str]:
        """
        Import chat logs from a file.
        
        Usage: /import <file>
        
        Args:
            args: Command arguments with file path
            
        Returns:
            Tuple[bool, str]: Success status and import information
        """
        if not self.user_id:
            return False, "You must be logged in to use this command."
            
        if len(args) == 0:
            return False, "Missing file path. Usage: /import <file>"
            
        import_file = Path(args[0])
        if not import_file.exists():
            return False, f"File not found: {import_file}"
            
        try:
            # Determine the file format
            file_extension = import_file.suffix.lower()[1:]
            
            # Load the data
            imported_messages = []
            
            if file_extension == "json":
                with open(import_file, 'r') as f:
                    imported_messages = json.load(f)
                    
            elif file_extension == "csv":
                with open(import_file, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    imported_messages = list(reader)
                    
            elif file_extension == "txt":
                # Assume a simple format: [timestamp] [channel] sender: content
                with open(import_file, 'r') as f:
                    for line in f:
                        parts = line.strip().split("] [")
                        if len(parts) >= 3:
                            timestamp = parts[0][1:]
                            channel = parts[1]
                            sender_content = "] ".join(parts[2:])
                            sender, content = sender_content.split(": ", 1)
                            
                            imported_messages.append({
                                "timestamp": timestamp,
                                "channel": channel,
                                "sender": sender,
                                "content": content,
                                "type": "text"
                            })
            else:
                return False, f"Unsupported file format: {file_extension}. Supported formats: json, csv, txt"
                
            # TODO: In a real implementation, we would import the messages to Firebase
            # For this example, we'll simulate an import with a placeholder
            
            return True, f"Imported {len(imported_messages)} messages from {import_file}"
            
        except Exception as e:
            logger.error(f"Import failed: {str(e)}")
            return False, f"Import failed: {str(e)}"
            
    def handle_exit(self, args: List[str]) -> Tuple[bool, str]:
        """
        Exit the chat application.
        
        Usage: /exit
        
        Args:
            args: Command arguments
            
        Returns:
            Tuple[bool, str]: Success status and exit message
        """
        self.console.shutdown()
        return True, "Exiting kalX. Goodbye!"
        
    def handle_clear(self, args: List[str]) -> Tuple[bool, str]:
        """
        Clear the chat screen.
        
        Usage: /clear
        
        Args:
            args: Command arguments
            
        Returns:
            Tuple[bool, str]: Success status and clear message
        """
        self.console.clear_screen()
        return True, "Screen cleared"

# Create standalone functions that wrap the SystemCommands class methods
def create_system_handler(method_name: str) -> callable:
    def handler(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
        # Initialize with console from context if available
        console = getattr(context, 'console', None)
        system = SystemCommands(console, user_id)
        method = getattr(system, method_name)
        return method(args)
    return handler

# Export standalone function versions
handle_help = create_system_handler("handle_help")
handle_version = create_system_handler("handle_version")
handle_uptime = create_system_handler("handle_uptime")
handle_debug = create_system_handler("handle_debug")
handle_backup = create_system_handler("handle_backup")
handle_restore = create_system_handler("handle_restore")
handle_export = create_system_handler("handle_export")
handle_import = create_system_handler("handle_import")
handle_exit = create_system_handler("handle_exit")
handle_settings = create_system_handler("handle_settings")
handle_settheme = create_system_handler("handle_settheme")
handle_setfont = create_system_handler("handle_setfont")
handle_setcolor = create_system_handler("handle_setcolor")
handle_setnotif = create_system_handler("handle_setnotif")
handle_setpeep = create_system_handler("handle_setpeep")
handle_setautoscroll = create_system_handler("handle_setautoscroll")