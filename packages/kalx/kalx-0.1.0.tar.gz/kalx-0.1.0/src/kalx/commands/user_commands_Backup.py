# kalx/commands/user_commands.py
"""
Command handlers for user management.
"""

from typing import List, Tuple, Any, Dict
from kalx.auth.authentication import Authentication
from kalx.auth.user import UserManager, UserStatus, User
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
        return False, "Usage: /register [email] [password]"
        
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
        return True, f"Account registered successfully. User ID: {result}"
    else:
        return False, f"Registration failed: {result}"

def handle_login(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Log into your account.
    Usage: /login [email] [password]
    """
    if len(args) < 2:
        return False, "Usage: /login [email] [password]"
        
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
        
        return True, f"Logged in successfully as {user.username}"
    else:
        return False, f"Login failed: {token}"

def handle_logout(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Log out of the chat session.
    Usage: /logout
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        return False, "Logout failed: No user is currently logged in."

    user_id = user_data["user_id"]

    # Update user status to offline
    success = user_manager.update_status(user_id, UserStatus.OFFLINE)
    if not success:
        return False, "Failed to update user status to offline."

    # Clear the screen and print a logout message
    console.clear()
    console.print("[bold green]Logged out successfully.[/bold green]")
    return True, ""

def handle_whoami(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Display your current username, status, and user ID.
    Usage: /whoami
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        return False, "User information not found"

    user_id = user_data["user_id"]
    user = user_manager.get_user(user_id)
    
    if not user:
        return False, "User information not found"

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
    panel = Panel(user_info, title="Who Am I", border_style="green", expand=False)
    console.print(panel)

    return True, ""

def handle_setname(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Change your display name.
    Usage: /setname [new_name]
    """
    if not args:
        return False, "Usage: /setname [new_name]"
        
    new_name = " ".join(args)  # Allow multi-word names
    
    user_manager = UserManager()
    user = user_manager.get_user(user_id)
    
    if not user:
        return False, "User information not found"
        
    user.display_name = new_name
    success = user_manager.update_user(user)
    
    if success:
        return True, f"Display name changed to '{new_name}'"
    else:
        return False, "Failed to update display name"

def handle_setstatus(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Update your chat status.
    Usage: /setstatus [online/away/busy/offline]
    """
    if not args:
        return False, "Usage: /setstatus [online/away/busy/offline]"
        
    status_str = args[0].lower()
    
    try:
        status = UserStatus(status_str)
    except ValueError:
        return False, "Invalid status. Choose from: online, away, busy, offline"
    
    user_manager = UserManager()
    success = user_manager.update_status(user_id, status)
    
    if success:
        return True, f"Status updated to {status.value}"
    else:
        return False, "Failed to update status"

def handle_changepassword(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Change your password.
    Usage: /changepassword [old_password] [new_password]
    """
    if len(args) < 2:
        return False, "Usage: /changepassword [old_password] [new_password]"
        
    old_password = args[0]
    new_password = args[1]
    
    auth = Authentication()
    success, message = auth.change_password(user_id, new_password)
    
    if success:
        return True, "Password changed successfully"
    else:
        return False, f"Failed to change password: {message}"

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
        
        return True, "Account deleted successfully"
    else:
        return False, f"Failed to delete account: {message}"

def handle_block(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Block messages from a specific user.
    Usage: /block [user]
    """
    if not args:
        return False, "Usage: /block [user]"
        
    target_user = args[0]
    
    user_manager = UserManager()
    success = user_manager.block_user(user_id, target_user)
    
    if success:
        return True, f"Blocked user: {target_user}"
    else:
        return False, "Failed to block user"

def handle_unblock(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Unblock a previously blocked user.
    Usage: /unblock [user]
    """
    if not args:
        return False, "Usage: /unblock [user]"
        
    target_user = args[0]
    
    user_manager = UserManager()
    success = user_manager.unblock_user(user_id, target_user)
    
    if success:
        return True, f"Unblocked user: {target_user}"
    else:
        return False, "Failed to unblock user"

def handle_friend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Send a friend request to a user.
    Usage: /friend [username or UID]
    """
    if not args:
        return False, "Usage: /friend [username or UID]"

    target_identifier = args[0]
    user_manager = UserManager()

    # Load current user's data
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        return False, "Error happened while processing your request."

    user_id = user_data["user_id"]

    # Prevent sending friend requests to oneself
    if target_identifier == user_id:
        return False, "You cannot send a friend request to yourself."

    # Check if the target user exists by UID
    target_user = user_manager.get_user(target_identifier)
    if not target_user:
        # Try to find the user by username
        all_users = user_manager.get_all_users()
        if not all_users:
            return False, "No users found in the system."

        target_user = next((u for u in all_users if u.get("username") == target_identifier), None)
        if not target_user:
            return False, f"User '{target_identifier}' not found."

    target_user_id = target_user.get("user_id")

    # Prevent sending friend requests to oneself (redundant check for username input)
    if target_user_id == user_id:
        return False, "You cannot send a friend request to yourself."

    # Check if already friends
    if target_user_id in user_data.get("friends", []):
        return False, f"You are already friends with {target_user.get('username', 'kalXuser')}."

    # Check if a friend request is already pending
    if target_user_id in user_data.get("pending_requests", []):
        return False, f"You have already sent a friend request to {target_user.get('username', 'kalXuser')}."

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

    return True, f"Friend request sent to {target_user.get('username', 'kalXuser')}."

def handle_accept_friend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Accept a friend request.
    Usage: /acceptfriend [user]
    """
    if not args:
        return False, "Usage: /acceptfriend [user]"
        
    requester_id = args[0]
    user_manager = UserManager()
    
    # Load current user's data from JSON
    user_data = user_manager._load_from_json()
    if not user_data or not user_data.get("user_id"):
        return False, "Your user data could not be retrieved."

    user_id = user_data["user_id"]

    # Check if the requester exists
    requester = user_manager.get_user(requester_id)
    if not requester:
        return False, f"User with ID '{requester_id}' not found."
    
    # Check if there is a pending friend request from the requester
    pending_requests = user_data.get("pending_requests", [])
    if requester_id not in pending_requests:
        return False, f"No friend request from {requester.get('username', 'Unknown')}."
    
    # Add each other to the friends list
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
    
    # Notify the requester
    notification = f"{user_data.get('username', 'Unknown')} has accepted your friend request."
    user_manager.update_user(requester_id, {"notifications": requester.get("notifications", []) + [notification]})
    
    return True, f"You are now friends with {requester.get('username', 'Unknown')}."

def handle_unfriend(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Remove a user from your friend list.
    Usage: /unfriend [user]
    """
    if not args:
        return False, "Usage: /unfriend [user]"
        
    target_user = args[0]
    
    user_manager = UserManager()
    success = user_manager.remove_friend(user_id, target_user)
    
    if success:
        return True, f"Removed {target_user} from friends"
    else:
        return False, "Failed to remove friend"

def handle_listfriends(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show all users in your friend list.
    Usage: /listfriends
    """
    user_manager = UserManager()
    user_data = user_manager._load_from_json()  # Load user data from JSON

    if not user_data or not user_data.get("user_id"):
        return False, "User information not found"

    if not user_data.get("friends"):
        return True, "You have no friends in your list."

    friend_details = []
    for friend_id in user_data["friends"]:
        friend = user_manager.get_user(friend_id)
        if friend:
            friend_details.append(f"{friend.get('username', 'kalXuser')} ({friend.get('status', 'offline')})")
        else:
            friend_details.append(f"{friend_id} (Unknown)")

    friends_list = "\n".join(friend_details)
    return True, f"Friends List:\n{friends_list}"

def handle_onlist(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Show online users.
    Usage: /onlist
    """
    user_manager = UserManager()
    online_users = user_manager.get_users_by_status(UserStatus.ONLINE)

    if not online_users:
        return True, "No users are currently online."

    table = Table(title="Online Users")
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
        return True, "No users are currently offline."

    table = Table(title="Offline Users")
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
        return True, "No registered users found."

    table = Table(title="All Users")
    table.add_column("Username", style="cyan")
    table.add_column("UID", style="green", overflow="fold")  # Ensure full UID is displayed
    table.add_column("Status", style="yellow")

    for user in all_users:
        if user.get("user_id") == user_id:
            table.add_row(f"{user.get('username', 'kalxUser')} (Me)", user.get("user_id", "kalxid0101"), user.get("status", "Busy"))
        else:
            table.add_row(user.get('username', 'kalxUser'), user.get("user_id", "kalxid0101"), user.get("status", "Busy"))

    console.print(table)
    return True, ""

def handle_report(user_id: str, args: List[str], context: Any) -> Tuple[bool, str]:
    """
    Report a user for misconduct.
    Usage: /report [user] [reason]
    """
    if len(args) < 2:
        return False, "Usage: /report [user] [reason]"
        
    target_user = args[0]
    reason = " ".join(args[1:])
    
    # In a real implementation, this would store the report in a database
    # For now, just log it
    from kalx.utils.logger import get_logger
    logger = get_logger(__name__)
    logger.warning(f"User report: {user_id} reported {target_user} for: {reason}")
    
    return True, f"User {target_user} has been reported. Thank you for helping keep the chat safe."

