"""
Interactive menu system for kalX.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Dict
from kalx.auth.user import UserManager, UserStatus
from kalx.chat.group import GroupManager

console = Console()

def display_welcome(user_data: Dict) -> None:
    """Display welcome message and user info."""
    display_name = user_data.get('display_name', user_data.get('email').split('@')[0])
    status = user_data.get('status', 'online')
    
    console.print(f"\n[bold green]Welcome to kalX, {display_name}![/bold green]")
    console.print(f"Status: [cyan]{status}[/cyan]\n")

def display_stats(user_data: Dict) -> None:
    """Display user statistics."""
    user_manager = UserManager()
    group_manager = GroupManager()
    
    # Get counts
    friend_count = len(user_data.get('friends', []))
    group_count = len(user_data.get('groups', []))
    online_users = len(user_manager.get_users_by_status(UserStatus.ONLINE))
    
    # Create stats table
    table = Table(title="Your Stats", box=None)
    table.add_column("Category", style="cyan")
    table.add_column("Count", justify="right", style="green")
    
    table.add_row("Friends", str(friend_count))
    table.add_row("Groups", str(group_count))
    table.add_row("Users Online", str(online_users))
    
    console.print(table)

def display_quick_help() -> None:
    """Display quick help panel."""
    help_text = (
        "[cyan]Available Commands:[/cyan]\n"
        "/msg [user] [message] - Send private message\n"
        "/gmsg [group] [message] - Send group message\n"
        "/friend [username] - Add friend\n"
        "/creategroup [name] - Create new group\n"
        "/help - Show all commands"
    )
    console.print(Panel(help_text, title="Quick Help"))

def display_menu(user_data: Dict) -> None:
    """Display the main menu."""
    console.clear()
    display_welcome(user_data)
    display_stats(user_data)
    
    # Show recent activity if any
    if user_data.get('groups'):
        console.print("\n[bold]Your Groups:[/bold]")
        group_manager = GroupManager()
        for group_id in user_data['groups']:
            group = group_manager.get_group(group_id)
            if group:
                console.print(f"- {group.name} ({len(group.members)} members)")
    else:
        console.print("\n[yellow]You haven't joined any groups yet. Use /creategroup to create one![/yellow]")
    
    if user_data.get('friends'):
        console.print("\n[bold]Online Friends:[/bold]")
        user_manager = UserManager()
        online_friends = []
        for friend_id in user_data['friends']:
            friend = user_manager.get_user(friend_id)
            if friend and friend.get('status') == 'online':
                online_friends.append(friend.get('display_name', friend.get('email')))
        
        if online_friends:
            for friend in online_friends:
                console.print(f"- {friend}")
        else:
            console.print("[yellow]No friends online right now[/yellow]")
    else:
        console.print("\n[yellow]You haven't added any friends yet. Use /friend to add friends![/yellow]")
    
    display_quick_help()
