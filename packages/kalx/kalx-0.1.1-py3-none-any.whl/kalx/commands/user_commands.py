# kalx/commands/user_commands.py
"""
Command handlers for user management.
"""

from typing import List, Tuple, Any, Dict
from kalx.auth.authentication import Authentication
from kalx.auth.user import UserManager, UserStatus, User
from kalx.notifications import NotificationManager, Notification
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import datetime

console = Console()

def handle_register(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Register a new account.
    Usage: /register [email] [password]
    """
    if len(args) < 2:
        return False, "[bold magenta]Usage: /register [email] [password][/bold magenta]"

    email = args[0]
    password = args[1]

    auth = Authentication()
    success, result = auth.register(email, password)

    if success:
        # Create user profile
        user_manager = UserManager()
        username = email.split('@')[0]  # Default username from email
        user = User(
            user_id=result,
            username=username,
            email=email
        )
        user_manager.create_user(user)
        console.print(Panel(f"[bold green]Account registered successfully. User ID: {result}[/bold green]", title="[bold cyan]REGISTRATION[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel(f"[bold red]Registration failed: {result}[/bold red]", title="[bold cyan]REGISTRATION[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_login(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Log into your account.
    Usage: /login [email] [password]
    """
    if len(args) < 2:
        return False, "[bold magenta]Usage: /login [email] [password][/bold magenta]"

    email = args[0]
    password = args[1]

    auth = Authentication()
    success, token = auth.login(email, password)

    if success:
        # Get user info
        user_manager = UserManager()
        user = user_manager.get_user(email)

        # Update user status to online
        user_manager.update_status(user.user_id, UserStatus.ONLINE)

        console.print(Panel(f"[bold green]Logged in successfully as {user.username}[/bold green]", title="[bold cyan]LOGIN[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel(f"[bold red]Login failed: {token}[/bold red]", title="[bold cyan]LOGIN[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_logout(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Log out of the chat session.
    Usage: /logout
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        console.print(Panel("[bold red]Logout failed: No user is currently logged in.[/bold red]", title="[bold cyan]LOGOUT[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    user_id = user_data["user_id"]

    # Update user status to offline
    success = user_manager.update_status(user_id, UserStatus.OFFLINE)
    if not success:
        console.print(Panel("[bold red]Failed to update user status to offline.[/bold red]", title="[bold cyan]LOGOUT[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Clear the screen and print a logout message
    console.clear()
    console.print(Panel("[bold green]Logged out successfully.[/bold green]", title="[bold cyan]LOGOUT[/bold cyan]", border_style="bright_magenta"))
    return True, ""

def handle_whoami(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Display your current username, status, and user ID.
    Usage: /whoami
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        console.print(Panel("[bold red]User information not found[/bold red]", title="[bold cyan]WHOAMI[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    user_id = user_data["user_id"]
    user = user_manager.get_user(user_id)

    if not user:
        console.print(Panel("[bold red]User information not found[/bold red]", title="[bold cyan]WHOAMI[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Format the last active date
    last_active = user.get('last_active', 'Unknown')
    if last_active != 'Unknown':
        try:
            last_active = datetime.fromisoformat(last_active).strftime("%B %d, %Y %I:%M:%S %p")
        except ValueError:
            pass  # Keep it as 'Unknown' if formatting fails

    # Prepare the user information text
    user_info = Text.from_markup(f"""
[bold cyan]User Information:[/bold cyan]
[bold]Username:[/bold] {user.get('username', 'Unknown')}
[bold]Display Name:[/bold] {user.get('display_name', 'Unknown')}
[bold]Email:[/bold] {user.get('email', 'Unknown')}
[bold]Status:[/bold] {user.get('status', 'offline')}
[bold]User ID:[/bold] {user.get('user_id', 'Unknown')}
[bold]Friends:[/bold] {len(user.get('friends', []))}
[bold]Groups:[/bold] {len(user.get('groups', []))}
[bold]Last Active:[/bold] {last_active}
""")

    # Display the information inside a styled box
    panel = Panel(user_info, title="[bold cyan]WHO AM I[/bold cyan]", border_style="bright_magenta", expand=False)
    console.print(panel)

    return True, ""

def handle_setname(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Change your display name.
    Usage: /setname [new_name]
    """
    if not args:
        return False, "[bold magenta]Usage: /setname [new_name][/bold magenta]"

    new_name = " ".join(args)  # Allow multi-word names

    user_manager = UserManager()
    user = user_manager.get_user(user_id)

    if not user:
        console.print(Panel("[bold red]User information not found[/bold red]", title="[bold cyan]SETNAME[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    user.display_name = new_name
    success = user_manager.update_user(user)

    if success:
        console.print(Panel(f"[bold green]Display name changed to '{new_name}'[/bold green]", title="[bold cyan]SETNAME[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel("[bold red]Failed to update display name[/bold red]", title="[bold cyan]SETNAME[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_setstatus(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Update your chat status.
    Usage: /setstatus [online/away/busy/offline]
    """
    if not args:
        return False, "[bold magenta]Usage: /setstatus [online/away/busy/offline][/bold magenta]"

    status_str = args[0].lower()

    try:
        status = UserStatus(status_str)
    except ValueError:
        return False, "[bold red]Invalid status. Choose from: online, away, busy, offline[/bold red]"

    user_manager = UserManager()
    success = user_manager.update_status(user_id, status)

    if success:
        console.print(Panel(f"[bold green]Status updated to {status.value}[/bold green]", title="[bold cyan]SETSTATUS[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel("[bold red]Failed to update status[/bold red]", title="[bold cyan]SETSTATUS[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_changepassword(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Change your password.
    Usage: /changepassword [old_password] [new_password]
    """
    if len(args) < 2:
        return False, "[bold magenta]Usage: /changepassword [old_password] [new_password][/bold magenta]"

    old_password = args[0]
    new_password = args[1]

    auth = Authentication()
    success, message = auth.change_password(user_id, new_password)

    if success:
        console.print(Panel("[bold green]Password changed successfully[/bold green]", title="[bold cyan]CHANGEPASSWORD[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel(f"[bold red]Failed to change password: {message}[/bold red]", title="[bold cyan]CHANGEPASSWORD[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_deleteaccount(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Permanently delete your account.
    Usage: /deleteaccount
    """
    auth = Authentication()
    user_manager = UserManager()

    # Delete account from Firebase Auth
    success, message = auth.delete_account(user_id)

    if success:
        # Delete user profile
        user_manager.delete_user(user_id)

        console.print(Panel("[bold green]Account deleted successfully[/bold green]", title="[bold cyan]DELETEACCOUNT[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel(f"[bold red]Failed to delete account: {message}[/bold red]", title="[bold cyan]DELETEACCOUNT[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_block(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Block messages from a specific user.
    Usage: /block [user]
    """
    if not args:
        return False, "[bold magenta]Usage: /block [user][/bold magenta]"

    target_user = args[0]

    user_manager = UserManager()
    success = user_manager.block_user(user_id, target_user)

    if success:
        console.print(Panel(f"[bold green]Blocked user: {target_user}[/bold green]", title="[bold cyan]BLOCK[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel("[bold red]Failed to block user[/bold red]", title="[bold cyan]BLOCK[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_unblock(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Unblock a previously blocked user.
    Usage: /unblock [user]
    """
    if not args:
        return False, "[bold magenta]Usage: /unblock [user][/bold magenta]"

    target_user = args[0]

    user_manager = UserManager()
    success = user_manager.unblock_user(user_id, target_user)

    if success:
        console.print(Panel(f"[bold green]Unblocked user: {target_user}[/bold green]", title="[bold cyan]UNBLOCK[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel("[bold red]Failed to unblock user[/bold red]", title="[bold cyan]UNBLOCK[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_friend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Send a friend request to a user.
    Usage: /friend [username or UID]
    """
    if not args:
        return False, "[bold magenta]Usage: /friend [username or UID][/bold magenta]"

    target_identifier = args[0]
    user_manager = UserManager()

    # Load current user's data
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        console.print(Panel("[bold red]Error happened while processing your request.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    user_id = user_data["user_id"]

    # Prevent sending friend requests to oneself
    if target_identifier == user_id:
        console.print(Panel("[bold red]You cannot send a friend request to yourself.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Check if the target user exists by UID
    target_user = user_manager.get_user(target_identifier)
    if not target_user:
        # Try to find the user by username
        all_users = user_manager.get_all_users()
        if not all_users:
            console.print(Panel("[bold red]No users found in the system.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
            return False, ""

        target_user = next((u for u in all_users if u.get("username") == target_identifier), None)
        if not target_user:
            console.print(Panel(f"[bold red]User '{target_identifier}' not found.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
            return False, ""

    target_user_id = target_user.get("user_id")

    # Prevent sending friend requests to oneself (redundant check for username input)
    if target_user_id == user_id:
        console.print(Panel("[bold red]You cannot send a friend request to yourself.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Check if already friends
    if target_user_id in user_data.get("friends", []):
        console.print(Panel(f"[bold red]You are already friends with {target_user.get('username', 'kalXuser')}.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Check if a friend request is already pending
    if target_user_id in user_data.get("pending_requests", []):
        console.print(Panel(f"[bold red]You have already sent a friend request to {target_user.get('username', 'kalXuser')}.[/bold red]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    # Add the friend request to the target user's pending requests
    target_pending_requests = target_user.get("pending_requests", [])
    if user_id not in target_pending_requests:
        target_pending_requests.append(user_id)
        user_manager.update_user(target_user_id, {"pending_requests": target_pending_requests})

    # Notify the target user if they are online
    if target_user.get("status") == UserStatus.ONLINE.value:
        console.print(f"[bold green]Friend request sent to {target_user.get('username', 'kalXuser')}[/bold green]")
    else:
        # Leave a message for the target user to see when they log in
        notification = f"You have a new friend request from {user_data.get('username', 'kalXuser')}."
        user_manager.update_user(target_user_id, {"notifications": target_user.get("notifications", []) + [notification]})

    console.print(Panel(f"[bold green]Friend request sent to {target_user.get('username', 'kalXuser')}.[/bold green]", title="[bold cyan]FRIEND[/bold cyan]", border_style="bright_magenta"))
    return True, ""

def handle_accept_friend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Accept a friend request.
    Usage: /acceptfriend [user]
    """
    if not args:
        return False, "[bold magenta]Usage: /acceptfriend [user][/bold magenta]"

    requester_id = args[0]
    user_manager = UserManager()
    notification_manager = NotificationManager()

    # Load current user's data from JSON
    user_data = user_manager._load_from_json()
    if not user_data or not user_data.get("user_id"):
        console.print(Panel("[bold red]Your user data could not be retrieved.[/bold red]", 
                          title="[bold cyan]ACCEPTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Get both users' data
    current_user = user_manager.get_user(user_id)
    requester = user_manager.get_user(requester_id)

    if not requester:
        console.print(Panel(f"[bold red]User with ID '{requester_id}' not found.[/bold red]", 
                          title="[bold cyan]ACCEPTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Check if there is a pending friend request
    pending_requests = user_data.get("pending_requests", [])
    if requester_id not in pending_requests:
        console.print(Panel(f"[bold red]No friend request from {requester.get('username', 'Unknown')}.[/bold red]", 
                          title="[bold cyan]ACCEPTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Add each other to friends list
    user_friends = user_data.get("friends", [])
    requester_friends = requester.get("friends", [])
    
    if user_id not in requester_friends:
        requester_friends.append(user_id)
        user_manager.update_user(requester_id, {"friends": requester_friends})
    
    if requester_id not in user_friends:
        user_friends.append(requester_id)
        user_manager.update_user(user_id, {"friends": user_friends})

    # Remove the friend request
    pending_requests.remove(requester_id)
    user_manager.update_user(user_id, {"pending_requests": pending_requests})

    # Send acceptance notification to requester
    notification = Notification(
        user_id=requester_id,
        sender_id=user_id,
        content=f"{current_user.get('username', 'Unknown')} accepted your friend request! You are now connected.",
        play_sound=True
    )
    notification_manager.add_notification(notification)

    console.print(Panel(f"[bold green]You are now friends with {requester.get('username', 'Unknown')}.[/bold green]", 
                       title="[bold cyan]ACCEPTFRIEND[/bold cyan]", 
                       border_style="bright_magenta"))
    return True, ""

def handle_rejectfriend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Reject a friend request.
    Usage: /rejectfriend [user]
    """
    if not args:
        return False, "[bold magenta]Usage: /rejectfriend [user][/bold magenta]"

    requester_id = args[0]
    user_manager = UserManager()
    notification_manager = NotificationManager()

    # Get current user's data directly from klx.json
    current_user = user_manager._load_from_json()
    if not current_user:
        console.print(Panel("[bold red]Failed to load user data from klx.json[/bold red]", 
                          title="[bold cyan]REJECTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Get requester's data using current user's authentication
    requester = user_manager.get_user(requester_id)
    if not requester:
        console.print(Panel(f"[bold red]User with ID '{requester_id}' not found.[/bold red]", 
                          title="[bold cyan]REJECTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Check if there is a pending request
    pending_requests = current_user.get("pending_requests", [])
    if requester_id not in pending_requests:
        console.print(Panel(f"[bold red]No friend request from {requester.get('username', 'Unknown')}.[/bold red]", 
                          title="[bold cyan]REJECTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Remove the friend request
    pending_requests.remove(requester_id)
    success = user_manager.update_user(current_user["user_id"], {"pending_requests": pending_requests})

    if not success:
        console.print(Panel("[bold red]Failed to update friend request status.[/bold red]", 
                          title="[bold cyan]REJECTFRIEND[/bold cyan]", 
                          border_style="bright_magenta"))
        return False, ""

    # Send rejection notification to requester
    notification = Notification(
        user_id=requester_id,
        sender_id=current_user["user_id"],
        content=f"{current_user.get('username', 'Unknown')} declined your friend request.",
        play_sound=True
    )
    notification_manager.add_notification(notification)

    console.print(Panel(f"[bold yellow]Friend request from {requester.get('username', 'Unknown')} rejected.[/bold yellow]", 
                       title="[bold cyan]REJECTFRIEND[/bold cyan]", 
                       border_style="bright_magenta"))
    return True, ""

def handle_unfriend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Remove a user from your friend list.
    Usage: /unfriend [user]
    """
    if not args:
        return False, "[bold magenta]Usage: /unfriend [user][/bold magenta]"

    target_user = args[0]

    user_manager = UserManager()
    success = user_manager.remove_friend(user_id, target_user)

    if success:
        console.print(Panel(f"[bold green]Removed {target_user} from friends[/bold green]", title="[bold cyan]UNFRIEND[/bold cyan]", border_style="bright_magenta"))
        return True, ""
    else:
        console.print(Panel("[bold red]Failed to remove friend[/bold red]", title="[bold cyan]UNFRIEND[/bold cyan]", border_style="bright_magenta"))
        return False, ""

def handle_listfriends(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show all users in your friend list.
    Usage: /listfriends
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        console.print(Panel("[bold red]User information not found[/bold red]", title="[bold cyan]LISTFRIENDS[/bold cyan]", border_style="bright_magenta"))
        return False, ""

    if not user_data.get("friends"):
        console.print(Panel("[bold yellow]You have no friends in your list.[/bold yellow]", title="[bold cyan]LISTFRIENDS[/bold cyan]", border_style="bright_magenta"))
        return True, ""

    friend_details = []
    for friend_id in user_data["friends"]:
        friend = user_manager.get_user(friend_id)
        if friend:
            friend_details.append(f"{friend.get('username', 'kalXuser')} ({friend.get('status', 'offline')})")
        else:
            friend_details.append(f"{friend_id} (Unknown)")

    friends_list = "\n".join(friend_details)
    console.print(Panel(f"[bold green]Friends List:\n{friends_list}[/bold green]", title="[bold cyan]LISTFRIENDS[/bold cyan]", border_style="bright_magenta"))
    return True, ""

def handle_onlist(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show online users.
    Usage: /onlist
    """
    user_manager = UserManager()
    online_users = user_manager.get_users_by_status(UserStatus.ONLINE)

    if not online_users:
        console.print(Panel("[bold yellow]No users are currently online.[/bold yellow]", title="[bold cyan]ONLIST[/bold cyan]", border_style="bright_magenta"))
        return True, ""

    table = Table(title="[bold cyan]Online Users[/bold cyan]")
    table.add_column("Username", style="cyan")
    table.add_column("UID", style="green", overflow="fold")
    table.add_column("Status", style="yellow")

    for user in online_users:
        if user.get("user_id") == user_id:
            table.add_row(f"{user.get('username', 'kalxUser')} (Me)", user.get("user_id", "kalxid0101"), user.get("status", "Busy"))
        else:
            table.add_row(user.get('username', 'kalxUser'), user.get("user_id", "kalxid0101"), user.get("status", "Busy"))

    console.print(table)
    return True, ""

def handle_offlist(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show offline users.
    Usage: /offlist
    """
    user_manager = UserManager()
    offline_users = user_manager.get_users_by_status(UserStatus.OFFLINE)

    if not offline_users:
        console.print(Panel("[bold yellow]No users are currently offline.[/bold yellow]", title="[bold cyan]OFFLIST[/bold cyan]", border_style="bright_magenta"))
        return True, ""

    table = Table(title="[bold cyan]Offline Users[/bold cyan]")
    table.add_column("Username", style="cyan")
    table.add_column("UID", style="green", overflow="fold")
    table.add_column("Status", style="yellow")

    for user in offline_users:
        if user.get("user_id") == user_id:
            table.add_row(f"{user.get('username', 'kalxUser')} (Me)", user.get("user_id", "kalxid0101"), user.get("status", "Busy"))
        else:
            table.add_row(user.get('username', 'kalxUser'), user.get("user_id", "kalxid0101"), user.get("status", "Busy"))

    console.print(table)
    return True, ""

def handle_alllist(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show all registered users.
    Usage: /alllist
    """
    user_manager = UserManager()
    all_users = user_manager.get_all_users()

    if not all_users:
        console.print(Panel("[bold yellow]No registered users found.[/bold yellow]", title="[bold cyan]ALLLIST[/bold cyan]", border_style="bright_magenta"))
        return True, ""

    table = Table(title="[bold cyan]All Users[/bold cyan]")
    table.add_column("Username", style="cyan")
    table.add_column("UID", style="green", overflow="fold")  # Ensure full UID is displayed
    #table.add_column("Status", style="yellow")

    for user in all_users:
        if user.get("user_id") == user_id:
            table.add_row(f"{user.get('username', 'kalxUser')} (Me)", user.get("user_id", "kalxid0101"))
        else:
            table.add_row(user.get('username', 'kalxUser'), user.get("user_id", "kalxid0101"))

    console.print(table)
    return True, ""

def handle_report(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Report a user for misconduct.
    Usage: /report [user] [reason]
    """
    if len(args) < 2:
        return False, "[bold magenta]Usage: /report [user] [reason][/bold magenta]"

    target_user = args[0]
    reason = " ".join(args[1:])

    # In a real implementation, this would store the report in a database
    # For now, just log it
    from kalx.utils.logger import get_logger
    logger = get_logger(__name__)
    logger.warning(f"User report: {user_id} reported {target_user} for: {reason}")

    console.print(Panel(f"[bold green]User {target_user} has been reported. Thank you for helping keep the chat safe.[/bold green]", title="[bold cyan]REPORT[/bold cyan]", border_style="bright_magenta"))
    return True, ""
