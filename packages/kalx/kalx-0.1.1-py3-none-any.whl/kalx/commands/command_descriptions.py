"""Module containing command descriptions and categories for kalX CLI."""

from typing import Dict, Tuple

# Basic frequently used commands
BASIC_COMMANDS: Dict[str, Tuple[str, str]] = {
    "help": ("Show all commands", "/help"),
    "msg": ("Private chat", "/msg <user> <msg>"),
    "join": ("Join group", "/joingroup <group>"),
    "friend": ("Add connection", "/friend <user>"),
    "creategroup": ("Create secure channel", "/creategroup [group_name] [description]"),
    "exit": ("Terminate session", "/exit")
}

# All command descriptions by category
COMMAND_DESCRIPTIONS: Dict[str, Dict[str, Tuple[str, str]]] = {
    "User": {
        "login": ("Login to your account", "/login <email> <password>"),
        "register": ("Create a new account", "/register <email> <password>"),
        "logout": ("Logout from current session", "/logout"),
        "whoami": ("Display your user information", "/whoami"),
        "setname": ("Change your display name", "/setname <new_name>"),
        "setstatus": ("Update your status message", "/setstatus <new_status>"),
        "changepassword": ("Change account password", "/changepassword <old> <new>"),
        "deleteaccount": ("Delete account permanently", "/deleteaccount"),
        "block": ("Block a user", "/block <username>"),
        "unblock": ("Unblock a user", "/unblock <username>")
    },
    "Chat": {
        "msg": ("Send private message", "/msg <username> <message>"),
        "gmsg": ("Send group message", "/gmsg <group> <message>"),
        "reply": ("Reply to message", "/reply <msg_id> <message>"),
        "editmsg": ("Edit message", "/editmsg <msg_id> <new>"),
        "delete": ("Delete message", "/delete <msg_id>"),
        "clear": ("Clear chat screen", "/clear"),
        "history": ("View chat history", "/history <target>"),
        "search": ("Search messages", "/search <keyword>"),
        "pin": ("Pin message", "/pin <msg_id>"),
        "unpin": ("Unpin message", "/unpin <msg_id>")
    },
    "Groups": {
        "creategroup": ("Create new group", "/creategroup [group_name] [description]"),
        "joingroup": ("Join group", "/joingroup <name>"),
        "leavegroup": ("Leave group", "/leavegroup <name>"),
        "invite": ("Invite user", "/invite <group> <user>"),
        "kick": ("Remove user from group", "/kick <group> <user>"),
        "setadmin": ("Set group admin", "/setadmin <group> <user>"),
        "removeadmin": ("Remove admin", "/removeadmin <group> <user>"),
        "setgroupname": ("Rename group", "/setgroupname <group> <new>"),
        "listgroups": ("List your groups", "/listgroups"),
        "mute": ("Mute group", "/mute <group>"),
        "unmute": ("Unmute group", "/unmute <group>")
    },
    "Social": {
        "friend": ("Add friend", "/friend <user>"),
        "unfriend": ("Remove friend", "/unfriend <user>"),
        "listfriends": ("List friends", "/listfriends"),
        "onlist": ("Show online users", "/onlist"),
        "offlist": ("Show offline users", "/offlist"),
        "alllist": ("Show all users", "/alllist"),
        "report": ("Report user", "/report <user> <reason>")
    },
    "System": {
        "help": ("Show help", "/help"),
        "version": ("Show version", "/version"),
        "uptime": ("Show runtime", "/uptime"),
        "debug": ("Toggle debug", "/debug"),
        "backup": ("Create backup", "/backup"),
        "restore": ("Restore backup", "/restore <file>"),
        "export": ("Export history", "/export <file>"),
        "import": ("Import history", "/import <file>"),
        "settings": ("Modify settings", "/settings"),
        "settheme": ("Change theme", "/settheme <name>"),
        "setfont": ("Change font", "/setfont <name>"),
        "setcolor": ("Change colors", "/setcolor <scheme>"),
        "setnotif": ("Notifications", "/setnotif <on/off>"),
        "setpeep": ("Typing indicator", "/setpeep <on/off>"),
        "setautoscroll": ("Auto-scroll", "/setautoscroll <on/off>"),
        "exit": ("Exit app", "/exit")
    },
    "Admin": {
        "ban": ("Ban user", "/ban <user>"),
        "unban": ("Unban user", "/unban <user>"),
        "muteuser": ("Mute user", "/muteuser <user>"),
        "unmuteuser": ("Unmute user", "/unmuteuser <user>"),
        "shutdown": ("Shutdown server", "/shutdown"),
        "announce": ("Send announcement", "/announce <msg>")
    }
}
