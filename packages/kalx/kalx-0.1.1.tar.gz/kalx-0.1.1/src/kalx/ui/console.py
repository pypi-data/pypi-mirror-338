# kalx/ui/console.py
"""
Main console interface for kalX - Enhanced with cyberpunk hacker aesthetics.
"""

import os
import sys
import threading
import time
import subprocess
import platform
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
import random
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.syntax import Syntax
from rich.layout import Layout
from rich.live import Live
from rich.box import Box, HEAVY, DOUBLE, ROUNDED
from rich.style import Style
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
from rich import box

from kalx.commands.command_handler import CommandHandler
from kalx.auth.authentication import Authentication
from kalx.auth.user import UserManager, User, UserStatus
from kalx.ui.themes import get_theme
from kalx.ui.notifications import NotificationManager
from kalx.utils.logger import get_logger
from kalx.utils.config import get_config
from kalx.chat.private import PrivateChat
from kalx.chat.group import GroupManager
from kalx.commands.command_descriptions import BASIC_COMMANDS, COMMAND_DESCRIPTIONS
from kalx.ui.cyberpunk import (
    CyberpunkAnimations, CyberpunkLogos,
    MATRIX_GREEN, MATRIX_DARK_GREEN, MATRIX_LIGHT_GREEN,
    NEON_BLUE, NEON_PINK, NEON_PURPLE, CYBER_YELLOW, CYBER_RED
)

logger = get_logger(__name__)

# Custom box style for a more cyberpunk feel
CYBER_BOX = HEAVY

class ConsoleUI:
    """Enhanced cyberpunk console interface for the kalX chat application."""

    THEMES = {
        "matrix": {
            "primary": "bright_green",
            "secondary": "green",
            "accent": "white",
            "alert": "red",
            "highlight": "bright_white",
            "box": box.HEAVY
        },
        "neon": {
            "primary": "bright_cyan",
            "secondary": "cyan",
            "accent": "bright_magenta",
            "alert": "bright_red",
            "highlight": "bright_yellow",
            "box": box.DOUBLE
        },
        "shadow": {
            "primary": "bright_blue",
            "secondary": "blue",
            "accent": "bright_white",
            "alert": "bright_red",
            "highlight": "bright_cyan",
            "box": CYBER_BOX
        }
    }

    def __init__(self, debug: bool = False, config_path: Optional[str] = None):
        """
        Initialize the console UI.

        Args:
            debug: Whether to enable debug mode
            config_path: Path to a custom config file
        """
        self.debug = debug
        self.config_path = config_path

        # Initialize rich console with full color support
        self.console = Console(
            color_system="truecolor",
            force_terminal=True,
            highlight=True,
            markup=True,
            width=None  # Adjust to terminal width
        )

        # Load config and theme first
        self.config = get_config(config_path)
        self.ui_theme_name = self.config.get('ui', 'theme', fallback='shadow')
        self.ui_theme = self.THEMES.get(self.ui_theme_name, self.THEMES["shadow"])
        self.theme = get_theme(self.config.get('ui', 'theme', fallback='dark'))

        # State variables
        self.running = False
        self.user_id = None
        self.current_chat = None
        self.is_group_chat = False
        self.chat_history = []
        self.input_history = []
        self.input_index = 0
        self.user_data = None
        self.error_state = False
        self.last_activity = datetime.now()
        self.terminal_width = os.get_terminal_size().columns
        self.terminal_height = os.get_terminal_size().lines

        # Initialize services - do this after config is loaded
        self.auth = Authentication()
        self.user_manager = UserManager()
        self.notification_manager = NotificationManager()
        self.command_handler = CommandHandler(self)

        # Lazily initialized services
        self._private_chat = None
        self._group_manager = None

    @property
    def private_chat(self) -> PrivateChat:
        """Lazy initialization of PrivateChat."""
        if not self._private_chat and self.user_id:
            self._private_chat = PrivateChat(self.user_id)
        return self._private_chat

    @property
    def group_manager(self) -> GroupManager:
        """Lazy initialization of GroupManager."""
        if not self._group_manager:
            self._group_manager = GroupManager()
        return self._group_manager

    def print(self, message: str, style: str = "") -> None:
        """
        Print a message to the console.

        Args:
            message: The message to display
            style: Rich text style to apply
        """
        self.console.print(message, style=style or self.ui_theme["primary"])

    def _simulate_typing(self, text: str, speed: float = 0.005) -> None:
        """
        Simulate typing effect for text output.

        Args:
            text: The text to display
            speed: Delay between characters in seconds
        """
        for char in text:
            self.console.print(char, end="", style=self.ui_theme["primary"])
            time.sleep(speed)
        self.console.print()

    def _show_loading_animation(self, message: str, duration: float = 1.0) -> None:
        """
        Display a loading animation.

        Args:
            message: Message to display during loading
            duration: Duration in seconds
        """
        with Progress(
            TextColumn("[bold green]{task.description}"),
            BarColumn(bar_width=None, style=self.ui_theme["primary"], complete_style=self.ui_theme["accent"]),
            TimeElapsedColumn(),
            console=self.console,
            transient=True
        ) as progress:
            task = progress.add_task(f"[{self.ui_theme['primary']}]{message}[/{self.ui_theme['primary']}]", total=100)
            chunk = 100 / (duration * 10)
            for _ in range(10):
                time.sleep(duration / 10)
                progress.update(task, advance=chunk)

    def _log_debug_info(self, message: str) -> None:
        """
        Log debug information to a file.

        Args:
            message: The debug message to log.
        """
        try:
            # Get the user's Documents directory
            documents_dir = Path.home() / "Documents/kalx/debug/"
            debug_file_path = documents_dir / "debug.txt"

            # Ensure the Documents directory exists
            documents_dir.mkdir(parents=True, exist_ok=True)

            with open(debug_file_path, "a") as debug_file:
                debug_file.write(f"{datetime.now().isoformat()} - {message}\n")
        except Exception as e:
            logger.error(f"Failed to write to {debug_file_path}: {e}")

    def start(self, user_data: Optional[Dict[str, Any]] = None) -> None:
        """
        Start the console UI.

        Args:
            user_data: Optional pre-authenticated user data
        """
        self.running = True
        self.user_data = user_data

        try:
            # Display startup animation
            self.clear_screen()
            self._display_startup_sequence()

            # Start notification polling thread
            self.notification_thread = threading.Thread(target=self._poll_notifications)
            self.notification_thread.daemon = True
            self.notification_thread.start()

            # Skip authentication if we have user data
            if user_data:
                self.user_id = user_data.get('uid')
                self.user_data = user_data
                # Log user data for debugging
                self._log_debug_info(f"User data initialized: {json.dumps(self.user_data, default=str)}")

                self._display_menu(user_data)
                self._check_notifications()
                self._main_loop()
            else:
                # Regular authentication flow
                if not self._authenticate():
                    return

                self._display_menu({
                    'display_name': self.user_data.get('display_name',
                                                       self.user_data.get('email', 'User')).split('@')[0]
                })
                self._check_notifications()
                self._main_loop()

        except KeyboardInterrupt:
            logger.info("Application terminated by user")
            self._display_shutdown_sequence()
        except Exception as e:
            self.error_state = True
            error_msg = f"Console error: {str(e)}"
            logger.error(error_msg, exc_info=True)

            if self.debug:
                import traceback
                self.console.print("\n[bold red]SYSTEM FAILURE[/bold red]")
                self.console.print(f"[{self.ui_theme['alert']}]{error_msg}[/{self.ui_theme['alert']}]")
                self.console.print("\n[bold yellow]TRACE DUMP:[/bold yellow]")
                self.console.print(traceback.format_exc())
            else:
                self.console.print("\n[bold red]CRITICAL ERROR DETECTED[/bold red]")
                self.console.print(f"[{self.ui_theme['alert']}]Error: {str(e)}[/{self.ui_theme['alert']}]")
                self.console.print("\nCheck logs at ~/.kalx/logs/kalx.log for details")
        finally:
            self.shutdown()

    def _display_startup_sequence(self) -> None:
        """Display a cool startup animation sequence."""
        self.console.print()
        CyberpunkAnimations.display_logo(tagline="SYSTEM STARTUP")

        self.console.print("\n[bold]INITIALIZING SECURE COMMUNICATION SYSTEM[/bold]")

        # Simulate system initialization
        startup_modules = [
            "Loading encryption protocols",
            "Establishing secure channels",
            "Initializing authentication systems",
            "Scanning for secure endpoints",
            "Loading user interface modules"
        ]

        for module in startup_modules:
            self._show_loading_animation(module, 0.5)

        self.console.print(f"\n[bold {self.ui_theme['accent']}]SYSTEM READY[/bold {self.ui_theme['accent']}]")
        time.sleep(0.5)

    def _display_shutdown_sequence(self) -> None:
        """Display a cool shutdown animation sequence."""
        self.console.print("\n[bold]TERMINATING SESSION[/bold]")

        # Simulate shutdown
        shutdown_modules = [
            "Closing secure channels",
            "Encrypting logs",
            "Clearing volatile memory",
            "Terminating processes"
        ]

        for module in shutdown_modules:
            self._show_loading_animation(module, 0.4)

        self.console.print(f"\n[bold {self.ui_theme['alert']}]CONNECTION TERMINATED[/bold {self.ui_theme['alert']}]")
        time.sleep(0.5)

    def _poll_notifications(self):
        """Periodically check for new notifications."""
        while self.running:
            self._check_notifications()
            time.sleep(10)  # Check every 10 seconds

    def _check_pending_requests(self) -> None:
        """
        Check for pending friend requests and display them to the user.
        """
        user_manager = UserManager()
        user_data = user_manager._load_from_json()  # Load user data from JSON

        if not user_data or not user_data.get("user_id"):
            self.console.print(f"[bold {self.ui_theme['alert']}]ERROR: User ID not found in saved data. Cannot verify pending connection requests.[/bold {self.ui_theme['alert']}]")
            return

        user_id = user_data["user_id"]
        pending_requests = user_data.get("pending_requests", [])
        if not pending_requests:
            self.console.print(f"[bold {self.ui_theme['secondary']}]No pending connection requests detected.[/bold {self.ui_theme['secondary']}]")
            return

        self.console.print(f"[bold {self.ui_theme['highlight']}]INCOMING CONNECTION REQUESTS DETECTED:[/bold {self.ui_theme['highlight']}]")
        for idx, requester_id in enumerate(pending_requests, start=1):
            requester = user_manager.get_user(requester_id)
            requester_name = requester.get("username", "Unknown") if requester else "Unknown"
            self.console.print(f"{idx}. [{self.ui_theme['accent']}]{requester_name}[/{self.ui_theme['accent']}] (ID: {requester_id})")

        self.console.print(f"\n[bold {self.ui_theme['primary']}]AVAILABLE COMMANDS:[/bold {self.ui_theme['primary']}]")
        self.console.print(f"[{self.ui_theme['accent']}]/acceptfriend [user_id][/{self.ui_theme['accent']}] - Accept connection request")
        self.console.print(f"[{self.ui_theme['accent']}]/rejectfriend [user_id][/{self.ui_theme['accent']}] - Reject connection request")

    def shutdown(self) -> None:
        """Safely shutdown the application."""
        # Only attempt these operations if we were successfully running
        if self.running and self.user_id:
            try:
                # Ensure user_id is valid before updating status
                self.user_manager.update_status(self.user_id, UserStatus.OFFLINE)
            except Exception as e:
                logger.error(f"Error updating user status during shutdown: {e}")

        # Clear screen on normal exit
        if not self.error_state:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.console.print(f"[bold {self.ui_theme['primary']}]CONNECTION TERMINATED. STAY SAFE IN THE NETWORK.[/bold {self.ui_theme['primary']}]")
            except Exception as e:
                logger.error(f"Error during clean exit: {e}")
        else:
            self.console.print(f"\n[bold {self.ui_theme['alert']}]SESSION TERMINATED ABNORMALLY[/bold {self.ui_theme['alert']}]")
            self.console.print(f"[{self.ui_theme['alert']}]SYSTEM LOGS MAY CONTAIN SENSITIVE DATA[/{self.ui_theme['alert']}]")

    def _authenticate(self) -> bool:
        """
        Handle user authentication.

        Returns:
            bool: True if authentication was successful, False otherwise
        """
        max_attempts = 3
        attempts = 0

        auth_panel = Panel(
            "",
            title=f"[{self.ui_theme['primary']}]SECURE AUTHENTICATION PROTOCOL[/{self.ui_theme['primary']}]",
            border_style=self.ui_theme["primary"],
            box=self.ui_theme["box"]
        )

        while attempts < max_attempts:
            options_text = Text()
            options_text.append("\n[SYSTEM OPTIONS]\n\n", style=f"bold {self.ui_theme['highlight']}")
            options_text.append("1. ", style=self.ui_theme["secondary"])
            options_text.append("Login to existing account\n", style=self.ui_theme["primary"])
            options_text.append("2. ", style=self.ui_theme["secondary"])
            options_text.append("Register new identity\n", style=self.ui_theme["primary"])
            options_text.append("3. ", style=self.ui_theme["secondary"])
            options_text.append("Terminate connection\n", style=self.ui_theme["primary"])

            auth_panel.renderable = options_text
            self.console.print(auth_panel)

            choice = Prompt.ask(
                f"[{self.ui_theme['secondary']}]SELECT OPERATION[/{self.ui_theme['secondary']}]",
                choices=["1", "2", "3"],
                default="1"
            )

            if choice == "1":
                email = Prompt.ask(f"[{self.ui_theme['secondary']}]IDENTITY[/{self.ui_theme['secondary']}]")
                password = Prompt.ask(f"[{self.ui_theme['secondary']}]ACCESS KEY[/{self.ui_theme['secondary']}]", password=True)

                self._show_loading_animation("Verifying credentials", 1.0)

                success, result = self.auth.login(email, password)
                if success:
                    self.user_id = result.get('uid')  # Ensure user_id is set
                    self.user_data = result

                    # Check if user has a profile, create one if not
                    user_profile = self.user_manager.get_user(self.user_id)
                    if not user_profile:
                        username = Prompt.ask(f"[{self.ui_theme['secondary']}]SET HANDLE[/{self.ui_theme['secondary']}]")
                        new_user = User(
                            user_id=self.user_id,
                            username=username,
                            email=email,
                            status=UserStatus.ONLINE
                        )
                        self.user_manager.create_user(new_user)
                    else:
                        # Update status to online
                        self.user_manager.update_status(self.user_id, UserStatus.ONLINE)

                    self.console.print(f"[bold {self.ui_theme['accent']}]AUTHENTICATION SUCCESSFUL. SECURE CHANNEL ESTABLISHED.[/bold {self.ui_theme['accent']}]")
                    return True
                else:
                    attempts += 1
                    remaining = max_attempts - attempts
                    self.console.print(f"[bold {self.ui_theme['alert']}]ACCESS DENIED: {result} ({remaining} attempts remaining before lockout)[/bold {self.ui_theme['alert']}]")

            elif choice == "2":
                email = Prompt.ask(f"[{self.ui_theme['secondary']}]NEW IDENTITY[/{self.ui_theme['secondary']}]")
                password = Prompt.ask(f"[{self.ui_theme['secondary']}]SET ACCESS KEY[/{self.ui_theme['secondary']}]", password=True)
                confirm = Prompt.ask(f"[{self.ui_theme['secondary']}]CONFIRM ACCESS KEY[/{self.ui_theme['secondary']}]", password=True)

                if password != confirm:
                    self.console.print(f"[bold {self.ui_theme['alert']}]ERROR: ACCESS KEYS DO NOT MATCH[/bold {self.ui_theme['alert']}]")
                    continue

                self._show_loading_animation("Creating secure identity", 1.5)

                success, result = self.auth.register(email, password)
                if success:
                    self.console.print(f"[bold {self.ui_theme['accent']}]IDENTITY CREATED SUCCESSFULLY. PROCEED TO LOGIN.[/bold {self.ui_theme['accent']}]")
                else:
                    self.console.print(f"[bold {self.ui_theme['alert']}]IDENTITY CREATION FAILED: {result}[/bold {self.ui_theme['alert']}]")

            elif choice == "3":
                return False

        self.console.print(f"[bold {self.ui_theme['alert']}]CRITICAL: AUTHENTICATION FAILURE. ACCESS LOCKED.[/bold {self.ui_theme['alert']}]")
        return False

    def _handle_command(self, user_input: str) -> None:
        """
        Handle a command input from the user.

        Args:
            user_input: The full command string (starting with /)
        """
        # Log command for debugging
        self._log_debug_info(f"Processing command: {user_input}")

        # Simulate command processing
        self.console.print(f"[{self.ui_theme['secondary']}]EXECUTING COMMAND...[/{self.ui_theme['secondary']}]")

        # Parse command
        command_parts = user_input.split(' ', 1)
        command = command_parts[0][1:]  # Remove the / prefix
        args = command_parts[1] if len(command_parts) > 1 else ""

        if command == "help":
            self._show_help_prompt()
        elif command == "exit":
            self.running = False
            return
        else:
            # Show a brief processing animation for more complex commands
            complex_commands = ["creategroup", "joingroup", "backup", "restore", "export", "import"]
            if command in complex_commands:
                self._show_loading_animation(f"Processing '{command}'", 0.5)

            result = self.command_handler.handle_command(
                self.user_id, [command] + args.split(), self.command_handler.context
            )
            if result[1]:
                status_color = self.ui_theme["accent"] if result[0] else self.ui_theme["alert"]
                self.console.print(f"[{status_color}]{result[1]}[/{status_color}]")

    def _get_command_description(self, handler) -> str:
        """
        Extract a clean description from a command handler function.

        Args:
            handler: The command handler function

        Returns:
            A cleaned description string
        """
        if not handler.__doc__:
            return "No description available"

        # Clean up docstring: remove indentation and get first line
        lines = [line.strip() for line in handler.__doc__.split('\n')]
        clean_lines = [line for line in lines if line]

        if not clean_lines:
            return "No description available"

        # Return the first meaningful line
        return clean_lines[0]

    def _show_help_prompt(self) -> None:
        """Display all available commands with descriptions."""
        table = Table(
            title=f"[{self.ui_theme['primary']}]AVAILABLE SYSTEM COMMANDS[/{self.ui_theme['primary']}]",
            box=self.ui_theme["box"],
            border_style=self.ui_theme["primary"],
            header_style=f"bold {self.ui_theme['highlight']}"
        )
        table.add_column("Command", style=self.ui_theme["accent"])
        table.add_column("Description", style=self.ui_theme["primary"])
        table.add_column("Usage", style=self.ui_theme["secondary"])

        # Add basic commands first
        for cmd, (desc, usage) in BASIC_COMMANDS.items():
            table.add_row(f"/{cmd}", desc, usage)

        # Add categorized commands
        for category, commands in COMMAND_DESCRIPTIONS.items():
            table.add_row(f"[bold]{category} Commands[/bold]", "", "")
            for cmd, (desc, usage) in commands.items():
                if cmd in BASIC_COMMANDS:
                    continue  # Skip duplicates
                table.add_row(f"/{cmd}", desc, usage)

        self.console.print(table)

    def _check_notifications(self) -> None:
        """
        Check and display notifications for the current user.
        """
        if not self.user_id:
            return
        notification_manager = NotificationManager()
        notifications = notification_manager.get_notifications(self.user_id, unread_only=True)
        if notifications:
            # Clear any existing content on the current line
            print("\r" + " " * self.terminal_width, end="\r", flush=True)
        
            # Create notifications text with properly closed tags
            notifications_text = "\n".join([
                f"[{self.ui_theme['secondary']}]{notification.content}[/{self.ui_theme['secondary']}]\n"
                f"[{self.ui_theme['secondary']}]TRACE ID: {notification.sender_id}[/{self.ui_theme['secondary']}]\n"
                f"[{self.ui_theme['secondary']}]EPOCH: {notification.timestamp.strftime('%Y-%m-%d %H:%M:%S')}[/{self.ui_theme['secondary']}]\n"
                for notification in notifications
            ])
            # Create and display the panel
            notifications_panel = Panel(
                notifications_text,
                title=f"[{self.ui_theme['highlight']}]INTERCEPTED SIGNALS[/{self.ui_theme['highlight']}]",
                border_style=self.ui_theme["secondary"],
                box=self.ui_theme["box"]
            )
            # Move cursor to new line and print notification
            self.console.print()
            self.console.print(notifications_panel)
        
            # Print a new prompt on a fresh line
            self.console.print(self._generate_prompt(), end="")
        
            # Ensure cursor is visible and at the right position
            sys.stdout.flush()

    def _generate_prompt(self) -> str:
        """Generate a dynamic prompt."""
        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Check if in a chat
        chat_indicator = ""
        if self.current_chat:
            chat_type = "GROUP" if self.is_group_chat else "PRIVATE"
            chat_indicator = f" [{self.ui_theme['accent']}]{chat_type}:{self.current_chat}[/{self.ui_theme['accent']}]"

        # Build prompt
        prompt = f"[{self.ui_theme['secondary']}]{current_time}[/{self.ui_theme['secondary']}]{chat_indicator} "
        prompt += f"[bold {self.ui_theme['primary']}]>>>[/bold {self.ui_theme['primary']}] "

        return prompt

    def _main_loop(self) -> None:
        """Main UI loop for handling user input."""
        while self.running:
            try:
                # Check notifications periodically (only if enough time has passed)
                now = datetime.now()
                if (now - self.last_activity).seconds > 10:
                    self._check_notifications()
                    self.last_activity = now

                # Display the dynamic prompt
                self.console.print(self._generate_prompt(), end='')

                # Get user input
                user_input = self.console.input()
                if not user_input:
                    continue

                # Add to input history
                self.input_history.append(user_input)
                self.input_index = len(self.input_history)

                # Update last activity
                self.last_activity = datetime.now()

                # Process input with matrix-like typing effect for some outputs
                if user_input.startswith('/'):
                    self._handle_command(user_input)
                elif self.current_chat:
                    self._send_message(user_input)
                elif self.current_chat:
                    self._send_message(user_input)
                else:
                    self.console.print(f"[{self.ui_theme['alert']}]NETWORK DISCONNECTED: Not in active communication channel. Use /msg <handle> or /joingroup <channel> to establish secure link.[/{self.ui_theme['alert']}]")

                # Update chat history if active connection exists
                if self.current_chat:
                    self._update_chat_history()

            except Exception as e:
                logger.error(f"Error in main loop: {e}", exc_info=True)
                self.console.print(f"[bold {self.ui_theme['alert']}]SYSTEM FAULT: {str(e)}[/bold {self.ui_theme['alert']}]")

    def _send_message(self, user_input: str) -> None:
        """
        Send a message to the current chat.

        Args:
            user_input: The message to send
        """
        if not self.user_id or not self.current_chat:
            self.console.print(f"[{self.ui_theme['alert']}]ERROR: Secure channel not properly established.[/{self.ui_theme['alert']}]")
            return

        try:
            # Simulate encryption process
            self._simulate_typing(f"[{self.ui_theme['secondary']}]ENCRYPTING MESSAGE...[/{self.ui_theme['secondary']}]", speed=0.002)

            # Generate a fake encryption sequence animation
            encryption_key = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
            self.console.print(f"[{self.ui_theme['secondary']}]KEY: {encryption_key}[/{self.ui_theme['secondary']}]")

            if self.is_group_chat:
                success, msg_id = self.group_manager.send_message(
                    self.user_id, self.current_chat, user_input
                )
            else:
                success, msg_id = self.private_chat.send_message(
                    self.current_chat, user_input
                )

            if success:
                self.console.print(f"[{self.ui_theme['accent']}]TRANSMISSION COMPLETE: MSG_ID:{msg_id[:8]}[/{self.ui_theme['accent']}]")
            else:
                self.console.print(f"[{self.ui_theme['alert']}]TRANSMISSION FAILED: {msg_id}[/{self.ui_theme['alert']}]")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            self.console.print(f"[{self.ui_theme['alert']}]TRANSMISSION ERROR: {str(e)}[/{self.ui_theme['alert']}]")

    def _update_chat_history(self) -> None:
        """Update the chat history based on current chat."""
        if not self.current_chat:
            self.chat_history = []
            return

        try:
            self._show_loading_animation("RETRIEVING SECURE LOGS", 0.3)

            if self.is_group_chat:
                self.chat_history = self.group_manager.get_chat_history(self.current_chat)
            else:
                self.chat_history = self.private_chat.get_chat_history(self.current_chat)

            # Display new messages
            self._display_chat_history()
        except Exception as e:
            logger.error(f"Error updating chat history: {e}")
            self.console.print(f"[{self.ui_theme['alert']}]LOG RETRIEVAL FAILURE: {str(e)}[/{self.ui_theme['alert']}]")

    def _display_chat_history(self) -> None:
        """Display the current chat history with enhanced styling."""
        if not self.chat_history:
            return

        # Get terminal width for layout
        term_width = os.get_terminal_size().columns

        # Create a styled header
        chat_type = "SECURE GROUP CHANNEL" if self.is_group_chat else "PRIVATE ENCRYPTED LINK"
        chat_name = self.current_chat  # This could be improved to show actual name

        header = f"┌{'─' * (term_width - 2)}┐\n"
        header += f"│ {chat_type}: {chat_name}{' ' * (term_width - len(chat_type) - len(chat_name) - 4)}│\n"
        header += f"└{'─' * (term_width - 2)}┘"

        self.console.print(header, style=self.ui_theme["primary"])

        # Create a table for the chat with cyberpunk styling
        table = Table(
            box=self.ui_theme["box"],
            border_style=self.ui_theme["primary"],
            expand=True,
            width=term_width - 4
        )
        table.add_column("TIME", style=self.ui_theme["secondary"], width=10)
        table.add_column("HANDLE", style=self.ui_theme["accent"], width=15)
        table.add_column("TRANSMISSION", style=self.ui_theme["primary"])

        # Add chat messages (limiting to last 15 for performance and readability)
        for msg in self.chat_history[-15:]:
            # Format timestamp to match cyberpunk aesthetic
            if isinstance(msg.get('timestamp'), datetime):
                time_str = msg.get('timestamp').strftime("%H:%M:%S")
            else:
                time_str = datetime.now().strftime("%H:%M:%S")

            sender = msg.get('sender_name', 'UNKNOWN')
            content = msg.get('content', '[DATA CORRUPTED]')

            # Add some randomized hex data to sender names for style
            hex_suffix = ''.join(random.choice('0123456789ABCDEF') for _ in range(4))
            styled_sender = f"{sender}#{hex_suffix}"

            table.add_row(time_str, styled_sender, content)

        self.console.print(Panel(table, border_style=self.ui_theme["primary"], box=self.ui_theme["box"]))

    def set_current_chat(self, chat_id: str, is_group: bool = False) -> None:
        """
        Set the current active chat with enhanced visual feedback.

        Args:
            chat_id: The ID of the chat to set as active
            is_group: Whether this is a group chat
        """
        # Show cool "connecting" animation
        chat_type = "GROUP CHANNEL" if is_group else "PRIVATE LINK"
        self._show_loading_animation(f"ESTABLISHING SECURE CONNECTION TO {chat_type}: {chat_id}", 1.0)

        self.current_chat = chat_id
        self.is_group_chat = is_group

        # Show encryption simulation
        encryption_symbols = ["■", "□", "▣", "▨", "▩", "▦", "▧", "▥"]
        self.console.print(f"[{self.ui_theme['secondary']}]ENCRYPTION PROTOCOL INITIALIZED...[/{self.ui_theme['secondary']}]")

        encryption_line = ""
        for _ in range(os.get_terminal_size().columns // 2):
            encryption_line += random.choice(encryption_symbols)

        self.console.print(encryption_line, style=self.ui_theme["primary"])
        time.sleep(0.3)

        self._update_chat_history()

        # Show connection established message with random "port" and "protocol"
        port = random.randint(1000, 9999)
        protocols = ["AES256", "QUANTUM", "POLY1305", "CHACHA20", "BLOWFISH", "TWOFISH"]
        protocol = random.choice(protocols)

        self.console.print()
        self.console.print(f"[bold {self.ui_theme['accent']}]SECURE CHANNEL ESTABLISHED[/bold {self.ui_theme['accent']}]")
        self.console.print(f"[{self.ui_theme['primary']}]CONNECTION: {chat_id}[/{self.ui_theme['primary']}]")
        self.console.print(f"[{self.ui_theme['secondary']}]PORT: {port} | PROTOCOL: {protocol} | STATUS: ACTIVE[/{self.ui_theme['secondary']}]")
        self.console.print()

    def show_message(self, message: str, style: str = "") -> None:
        """
        Show a message to the user with enhanced styling.

        Args:
            message: The message to display
            style: Rich text style to apply
        """
        if not style:
            style = self.ui_theme["primary"]

        # Add cyberpunk prefix to system messages
        if "ERROR" not in message and "CRITICAL" not in message:
            message = f"[SYS.MSG] {message}"

        self.console.print(message, style=style)

    def prompt_for_input(self, prompt_text: str, password: bool = False) -> str:
        """
        Prompt the user for input with cyberpunk styling.

        Args:
            prompt_text: The text to display as prompt
            password: Whether to hide the input

        Returns:
            The user's input
        """
        # Add cyberpunk suffix to prompts
        if not prompt_text.endswith(":"):
            prompt_text = f"{prompt_text}:"

        styled_prompt = f"[{self.ui_theme['secondary']}]{prompt_text}[/{self.ui_theme['secondary']}]"

        return Prompt.ask(styled_prompt, password=password, console=self.console)

    def confirm(self, prompt_text: str) -> bool:
        """
        Prompt the user for confirmation with cyberpunk styling.

        Args:
            prompt_text: The text to display as prompt

        Returns:
            True if confirmed, False otherwise
        """
        # Add dramatic flair to confirmation prompts
        if not prompt_text.endswith("?"):
            prompt_text = f"{prompt_text}?"

        styled_prompt = f"[bold {self.ui_theme['alert']}]CONFIRM: {prompt_text}[/bold {self.ui_theme['alert']}]"

        return Confirm.ask(styled_prompt, console=self.console)

    def clear_screen(self, force: bool = True) -> None:
        """
        Clear the console screen with a matrix-like animation.

        Args:
            force: Whether to force clearing the screen even if there are errors.
        """
        if not self.error_state or force:
            # Matrix-style screen clearing animation
            if not force:  # Only show animation for normal clears
                for _ in range(5):  # Just enough lines to look cool
                    matrix_line = ""
                    for _ in range(os.get_terminal_size().columns // 2):
                        char = random.choice("01")
                        matrix_line += char + " "
                    self.console.print(matrix_line, style=self.ui_theme["primary"])
                    time.sleep(0.05)

            # Actually clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

    def _display_menu(self, user_data: Dict[str, Any]) -> None:
        """
        Display welcome menu based on user data with cyberpunk aesthetics.

        Args:
            user_data: User information dictionary
        """
        try:
            # Get display name and current time
            display_name = user_data.get('display_name', user_data.get('email', 'User')).split('@')[0]
            current_time = datetime.now().strftime("%H:%M:%S")
            system_id = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

            # Create cyberpunk header
            header_text = Text()
            header_text.append("\n")
            header_text.append(f"IDENTITY: ", style=f"bold {self.ui_theme['secondary']}")
            header_text.append(f"{display_name}\n", style=f"bold {self.ui_theme['accent']}")
            header_text.append(f"SESSION: ", style=f"bold {self.ui_theme['secondary']}")
            header_text.append(f"{current_time}\n", style=f"bold {self.ui_theme['primary']}")
            header_text.append(f"SYSTEM ID: ", style=f"bold {self.ui_theme['secondary']}")
            header_text.append(f"{system_id}\n", style=f"bold {self.ui_theme['accent']}")
            header_text.append(f"STATUS: ", style=f"bold {self.ui_theme['secondary']}")
            header_text.append(f"ONLINE - SECURE CHANNEL ACTIVE\n", style=f"bold {self.ui_theme['accent']}")

            header = Panel(
                header_text,
                title=f"[{self.ui_theme['primary']}]kalX SECURE COMMUNICATION SYSTEM[/{self.ui_theme['primary']}]",
                border_style=self.ui_theme["primary"],
                box=self.ui_theme["box"]
            )

            self.console.print(header)

            # Display system status with cyberpunk flair
            sys_panel = Panel(
                f"Type [{self.ui_theme['accent']}]/help[/{self.ui_theme['accent']}] to display available commands\n"
                f"Current network nodes: {random.randint(5, 20)}\n"
                f"Encryption level: {random.choice(['GAMMA', 'EPSILON', 'OMEGA', 'ALPHA'])}\n"
                f"Signal strength: {random.randint(85, 99)}%",
                title=f"[{self.ui_theme['primary']}]SYSTEM STATUS[/{self.ui_theme['primary']}]",
                border_style=self.ui_theme["secondary"],
                box=self.ui_theme["box"]
            )
            self.console.print(sys_panel)

            # Check and display pending connection requests with cyberpunk styling
            user_manager = UserManager()
            user_data = user_manager._load_from_json()  # Load user data from JSON

            if user_data:
                pending_requests = user_data.get("pending_requests", [])
                if pending_requests:
                    requests_panel = Panel(
                        "\n".join([
                            f"[{self.ui_theme['secondary']}]{idx}.[/{self.ui_theme['secondary']}] [{self.ui_theme['accent']}]{user_manager.get_user(requester_id).get('username', 'Unknown') if user_manager.get_user(requester_id) else 'Unknown'}[/{self.ui_theme['accent']}] (ID: {requester_id})"
                            for idx, requester_id in enumerate(pending_requests, start=1)
                        ]),
                        title=f"[{self.ui_theme['alert']}]INCOMING CONNECTION REQUESTS[/{self.ui_theme['alert']}]",
                        border_style=self.ui_theme["alert"],
                        box=self.ui_theme["box"]
                    )
                    self.console.print(requests_panel)

                    command_panel = Panel(
                        f"[{self.ui_theme['accent']}]/acceptfriend [user_id][/{self.ui_theme['accent']}] - Accept connection request\n"
                        f"[{self.ui_theme['accent']}]/rejectfriend [user_id][/{self.ui_theme['accent']}] - Reject connection request",
                        title=f"[{self.ui_theme['primary']}]AVAILABLE COMMANDS[/{self.ui_theme['primary']}]",
                        border_style=self.ui_theme["primary"],
                        box=self.ui_theme["box"]
                    )
                    self.console.print(command_panel)
        except Exception as e:
            self.error_state = True
            self.console.print(f"[bold {self.ui_theme['alert']}]CRITICAL SYSTEM ERROR: {str(e)}[/bold {self.ui_theme['alert']}]")
            logger.error(f"Error displaying menu: {str(e)}")
