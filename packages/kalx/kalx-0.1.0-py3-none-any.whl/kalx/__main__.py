# kalx/__main__.py
"""
Main entry point for kalX chat application.
Enhanced with cyberpunk aesthetic using rich library.
"""

import sys
import os
import time
import argparse
import getpass
import random
import threading  # Add threading for the key listener
from pynput import keyboard  # Add pynput for cross-platform key listening
from typing import Dict, Any, Optional

# Rich library imports for cyberpunk styling
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.layout import Layout
from rich.live import Live

# Existing imports
from kalx.ui.console import ConsoleUI
from kalx.auth.authentication import Authentication
from kalx.utils.logger import get_logger
from kalx.auth.validation import is_valid_email
from kalx.ui.menu import display_menu
from kalx.auth.user import UserManager
from kalx.utils.plugins import PluginManager  # Plugin system support

# Import updated cyberpunk module
from kalx.ui.cyberpunk import (
    MatrixRain, TerminalGlitch, CyberpunkLogos, CyberpunkAnimations,
    MATRIX_GREEN, MATRIX_DARK_GREEN, MATRIX_LIGHT_GREEN,
    NEON_BLUE, NEON_PINK, NEON_PURPLE, CYBER_YELLOW, CYBER_RED
)

logger = get_logger(__name__)

# Rich console setup
rich_console = Console()

terminate_event = threading.Event()  # Event to signal termination

def listen_for_terminate():
    """Listen for CTRL + Q to terminate the process."""
    def on_press(key):
        try:
            if key == keyboard.Key.ctrl_l and keyboard.KeyCode.from_char('q'):
                terminate_event.set()  # Signal termination
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start the key listener in a separate thread
listener_thread = threading.Thread(target=listen_for_terminate, daemon=True)
listener_thread.start()

def handle_exit_signal():
    """Handle termination when CTRL + Q is pressed."""
    rich_console.print(f"\n[{CYBER_RED}]NEURAL CONNECTION TERMINATED BY USER.[/{CYBER_RED}]")
    sys.exit(0)

def ignore_interrupt_signal(signum, frame):
    """Ignore CTRL + C signal to allow copying and pasting."""
    pass

def cyberpunk_system_check():
    """Run a quick system diagnostic with animation."""
    CyberpunkAnimations.system_check()

def handle_auth_command(command: str, debug: bool = False) -> None:
    """Handle authentication commands with proper error handling and cyberpunk styling."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for a fresh start
        auth = Authentication()
        console = ConsoleUI(debug=debug)
        console.show_intro = False  # Don't show intro for direct commands
        user_manager = UserManager()  # Use UserManager for user operations

        if command == 'login':
            CyberpunkAnimations.display_logo(tagline="NEURAL INTERFACE v1.0.0")
            rich_console.print(Panel(
                "[bold]NEURAL AUTHENTICATION REQUIRED[/bold]",
                border_style=NEON_BLUE,
                title="ACCESS POINT",
                title_align="center"
            ))
            
            try:
                # Email input with validation
                while True:
                    email = Prompt.ask(f"[{NEON_BLUE}]Neural ID (email)[/{NEON_BLUE}]")
                    if not is_valid_email(email):
                        rich_console.print(f"[{CYBER_RED}]INVALID ID FORMAT. RETRY.[/{CYBER_RED}]")
                        continue
                    break
                
                # Password input
                password = getpass.getpass("Biometric Key (password): ")
                
                # Use connection animation from updated cyberpunk module
                CyberpunkAnimations.connection_animation("Authenticating neural signature", 1.5)
                
                # Perform actual login
                success, result = auth.login(email, password)
                if success:
                    user_data = user_manager.get_user(result['user_id'])
                    if user_data:
                        # Save user data to .kalx/klx.json
                        user_manager._save_to_json(user_data)
                    
                    rich_console.print(f"[{MATRIX_LIGHT_GREEN}]NEURAL SYNC COMPLETE[/{MATRIX_LIGHT_GREEN}]")
                    time.sleep(0.3)
                    
                    # Display user info in cyberpunk style
                    user_table = Table(show_header=False, box=box.SIMPLE_HEAD)
                    user_table.add_column("Property", style=NEON_BLUE)
                    user_table.add_column("Value", style=MATRIX_GREEN)
                    
                    user_table.add_row("USER", user_data.get('display_name', email))
                    user_table.add_row("STATUS", "CONNECTED")
                    user_table.add_row("ACCESS LEVEL", user_data.get('role', 'STANDARD'))
                    
                    rich_console.print(Panel(
                        user_table,
                        title="NEURAL PROFILE",
                        border_style=NEON_PURPLE,
                        title_align="center"
                    ))
                    
                    time.sleep(0.5)  # Reduced delay
                    
                    # Initialize console with user data
                    console.user_id = user_data.get('user_id')
                    console.user_data = user_data
                    console.running = True
                    console.start(user_data=user_data)
                else:
                    # Use cyberpunk error display
                    CyberpunkAnimations.display_logo(error_message=f"NEURAL SYNC FAILED: {result}")
            except KeyboardInterrupt:
                rich_console.print(f"\n[{CYBER_YELLOW}]NEURAL SYNC ABORTED.[/{CYBER_YELLOW}]")
                sys.exit(0)
                
        elif command == 'register':
            CyberpunkAnimations.display_logo(tagline="NEURAL INTERFACE v1.0.0")
            rich_console.print(Panel(
                "[bold]NEW NEURAL PROFILE REGISTRATION[/bold]",
                border_style=NEON_PINK,
                title="IDENTITY CREATION",
                title_align="center"
            ))
            
            try:
                # Email input with validation
                while True:
                    email = Prompt.ask(f"[{NEON_BLUE}]Neural ID (email)[/{NEON_BLUE}]")
                    if not is_valid_email(email):
                        rich_console.print(f"[{CYBER_RED}]INVALID ID FORMAT. RETRY.[/{CYBER_RED}]")
                        continue
                    break
                
                # Password input
                password = getpass.getpass("Create Biometric Key (password): ")
                confirm_password = getpass.getpass("Confirm Biometric Key: ")
                
                if password != confirm_password:
                    rich_console.print(f"[{CYBER_RED}]BIOMETRIC KEYS DO NOT MATCH. ABORTING.[/{CYBER_RED}]")
                    return
                
                # Use data stream effect during registration
                CyberpunkAnimations.data_stream_effect(duration=1.0)
                
                # Use the new TerminalGlitch effect to show progress
                TerminalGlitch.animate_glitch("Generating neural profile...", duration=1.0, intensity=0.3)
                
                # Perform actual registration
                success, result = auth.register(email, password)
                if success:
                    user_data = user_manager.get_user(result['user_id'])
                    if user_data:
                        # Save user data to .kalx/klx.json
                        user_manager._save_to_json(user_data)
                    
                    # Success message with decode text effect
                    CyberpunkAnimations.decode_text_effect("NEURAL PROFILE CREATED SUCCESSFULLY!", duration=1.0)
                    welcome_msg = f"Welcome to the grid, {user_data.get('display_name', email)}!"
                    CyberpunkAnimations.matrix_typing_effect(welcome_msg, speed=0.03)
                    CyberpunkAnimations.matrix_typing_effect("You can now login with your neural credentials.", speed=0.03)
                    
                    # Redirect to login
                    handle_auth_command("login", debug)
                else:
                    # Use cyberpunk error display
                    CyberpunkAnimations.display_logo(error_message=f"NEURAL PROFILE CREATION FAILED: {result}")
                    return
            except KeyboardInterrupt:
                rich_console.print(f"\n[{CYBER_YELLOW}]NEURAL PROFILE CREATION ABORTED.[/{CYBER_YELLOW}]")
                return
                
    except ValueError as e:
        CyberpunkAnimations.display_logo(error_message=f"ERROR: {str(e)}")
        sys.exit(1)
    except Exception as e:
        CyberpunkAnimations.display_logo(error_message="UNABLE TO COMPLETE NEURAL REQUEST. RETRY LATER.")
        if debug:
            rich_console.print(f"[dim]Debug info: {str(e)}[/dim]")
        logger.error(f"Command failed: {str(e)}")
        sys.exit(1)

def cyberpunk_menu(console_ui):
    """Display a cyberpunk-styled menu and process selection."""
    options = [
        ("Login", "Access your neural profile"),
        ("Register", "Create a new neural identity"),
        ("Quit", "Disconnect from the system")
    ]
    
    menu_table = Table(box=box.SIMPLE_HEAD, border_style=MATRIX_DARK_GREEN, show_header=False)
    menu_table.add_column("Option", style=CYBER_YELLOW)
    menu_table.add_column("Description", style=MATRIX_GREEN)
    
    for i, (option, desc) in enumerate(options, 1):
        menu_table.add_row(f"[{CYBER_YELLOW}]{i}.[/{CYBER_YELLOW}] {option}", desc)
    
    rich_console.print(Panel(
        menu_table,
        title="NEURAL COMMAND INTERFACE",
        border_style=NEON_PURPLE,
        title_align="center"
    ))
    
    # Get user choice
    while True:
        choice = Prompt.ask(f"[{MATRIX_LIGHT_GREEN}]Select neural command[/{MATRIX_LIGHT_GREEN}]", choices=["1", "2", "3"])
        
        if choice == "1":  # Login
            handle_auth_command("login", console_ui.debug)
            break
        elif choice == "2":  # Register
            handle_auth_command("register", console_ui.debug)
            break
        elif choice == "3":  # Quit
            CyberpunkAnimations.matrix_typing_effect("NEURAL CONNECTION TERMINATED.", speed=0.05)
            sys.exit(0)

def main():
    """Main entry point with cyberpunk styling."""
    try:
        # Parse arguments
        parser = argparse.ArgumentParser(description="kalX Hacker Console Chat")
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')
        parser.add_argument('--debug', action='store_true', help='Enable debug mode')
        parser.add_argument('--config', help='Path to config file')
        parser.add_argument('--server', help='Connect to alternative server (host:port)')
        parser.add_argument('command', nargs='?', choices=['login', 'register'], help='Direct command to execute')
        
        # Add diagnostics arguments
        diag_group = parser.add_argument_group('System Diagnostics')
        diag_group.add_argument('--diagnose', choices=['network', 'auth', 'storage'],
                               help='Run system diagnostics')
        
        # Add plugin arguments
        plugin_group = parser.add_argument_group('Plugin Management')
        plugin_group.add_argument('--plugins', action='store_true',
                                help='List installed plugins')
        plugin_group.add_argument('--plugin-install', metavar='URL',
                                help='Install plugin from URL')
        plugin_group.add_argument('--plugin-enable', metavar='NAME',
                                help='Enable a plugin')
        plugin_group.add_argument('--plugin-disable', metavar='NAME',
                                help='Disable a plugin')
        plugin_group.add_argument('--plugin-remove', metavar='NAME',
                                help='Remove an installed plugin')
        
        args = parser.parse_args()
        
        # Handle server connection first
        if args.server:
            try:
                host, port = args.server.split(':')
                port = int(port)
                
                # Test connection
                from kalx.utils.diagnostics import check_connection
                success, message = check_connection(host, port)
                
                if not success:
                    CyberpunkAnimations.display_logo(error_message=f"CONNECTION FAILED: {message}")
                    sys.exit(1)
                    
                # Update config with new server
                from kalx.utils.config import update_config
                update_config('network', 'server_host', host)
                update_config('network', 'server_port', str(port))
                
                CyberpunkAnimations.matrix_typing_effect(f"Connected to alternate server: {host}:{port}", speed=0.03)
                
            except ValueError:
                CyberpunkAnimations.display_logo(error_message="Invalid server format. Use host:port")
                sys.exit(1)
            except Exception as e:
                CyberpunkAnimations.display_logo(error_message=f"Server connection error: {str(e)}")
                sys.exit(1)
        
        # Handle diagnostics before other commands
        if args.diagnose:
            from kalx.utils.diagnostics import run_diagnostics
            success = run_diagnostics(args.diagnose)
            sys.exit(0 if success else 1)
        
        # Handle plugin commands before regular startup
        if any([args.plugins, args.plugin_install, args.plugin_enable, 
                args.plugin_disable, args.plugin_remove]):
            plugin_manager = PluginManager()
            
            if args.plugins:
                plugin_manager.list_plugins()
                return 0
            elif args.plugin_install:
                plugin_manager.install_plugin(args.plugin_install)
                return 0
            elif args.plugin_enable:
                plugin_manager.enable_plugin(args.plugin_enable)
                return 0
            elif args.plugin_disable:
                plugin_manager.disable_plugin(args.plugin_disable)
                return 0
            elif args.plugin_remove:
                plugin_manager.remove_plugin(args.plugin_remove)
                return 0

        # Handle direct commands
        if args.command:
            handle_auth_command(args.command, args.debug)
            return

        # If no arguments are provided, default to login
        if len(sys.argv) == 1:
            CyberpunkAnimations.matrix_typing_effect("[kalx]: Redirecting you to the login page....", speed=0.1)
            handle_auth_command("login", debug=False)
            return

        # Create the console UI object
        console_ui = ConsoleUI(debug=args.debug, config_path=args.config)
        console_ui.show_intro = False  # We're handling our own intro

        # Start console UI if no direct command
        while not terminate_event.is_set():  # Check for termination
            try:
                # Use the new matrix banner for intro
                CyberpunkAnimations.matrix_banner()
                
                intro_text = CyberpunkLogos.get_welcome_message()
                
                rich_console.print(Panel(
                    Text(intro_text, style=MATRIX_GREEN),
                    title="NEURAL LINK",
                    border_style=MATRIX_DARK_GREEN,
                    title_align="center"
                ))
                
                # Run system check with fixed animation
                cyberpunk_system_check()
                
                # Show our custom menu instead of directly starting console
                cyberpunk_menu(console_ui)
                
            except KeyboardInterrupt:
                pass  # Prevent termination on CTRL + C
    except Exception as e:
        error_msg = f"SYSTEM FAILURE: {str(e)}"
        CyberpunkAnimations.display_logo(error_message=error_msg)
        logger.error(f"Application error: {str(e)}")
        sys.exit(1)
    finally:
        if terminate_event.is_set():
            handle_exit_signal()

if __name__ == "__main__":
    sys.exit(main())