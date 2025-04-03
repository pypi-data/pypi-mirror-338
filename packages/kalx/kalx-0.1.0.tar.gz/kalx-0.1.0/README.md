# kalX - Neural Interface Chat System

A cyberpunk-themed secure chat application with advanced visual aesthetics and neural-link simulation.

<div align="center">
  
![kalX Logo](https://via.placeholder.com/150)

**A retro-style terminal chat application with secure Firebase backend,**
**inspired by cyberpunk aesthetics and hacker culture.**

![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Firebase](https://img.shields.io/badge/firebase-v9.0-orange)
![Python](https://img.shields.io/badge/python-3.8+-yellow)

</div>

## 🌐 Overview

kalX combines nostalgic terminal aesthetics with modern security practices to create a unique messaging experience. Navigate a neon-lit digital landscape where privacy and style converge.

```

    ██╗  ██╗ █████╗ ██╗     ██╗  ██╗
    ██║ ██╔╝██╔══██╗██║     ╚██╗██╔╝
    █████╔╝ ███████║██║      ╚███╔╝ 
    ██╔═██╗ ██╔══██║██║      ██╔██╗ 
    ██║  ██╗██║  ██║███████╗██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

```

## Features

### Core Features
- Secure end-to-end messaging
- Group chat capabilities
- Friend system
- Plugin support
- Custom themes

### Cyberpunk Visual Elements
- Neural interface simulation
- Dynamic system animations
- Encrypted transmission visualization
- Multiple logo styles:
  - Main logo (full-size)
  - Mini logo (compact)
  - Error logo (for alerts)
- Real-time status indicators
- Cyberpunk color schemes:
  - Neon Green (#39FF14)
  - Neon Blue (#4DEEEA)
  - Neon Pink (#FF10F0)
  - Neon Purple (#BD00FF)
  - Cyber Yellow (#FFD700)
  - Cyber Red (#FF3F3F)

## 💽 Installation

### Prerequisites
- Python 3.8+
- pip
- Firebase account

### Standard Installation

1. Clone repository & install dependencies:
```bash
git clone https://github.com/Odeneho-Calculus/kalx.git
cd kalX
pip install -e .
```

2. Set up Firebase:
   - Create Firebase project in the [Firebase Console](https://console.firebase.google.com/)
   - Enable Authentication & Firestore
   - Download credentials to `~/.kalx/firebase_credentials.json`

3. Configure environment:
```bash
# Create .env file
KALX_ENCRYPTION_KEY=your_key
KALX_FIREBASE_CREDENTIALS=path_to_credentials
```

### Docker Installation

```bash
# Build and run with Docker
docker build -t kalx .
docker run -it --name kalx-terminal kalx
```

## Usage

Basic commands:
```bash
# Start the application
python -m kalx

# Start with specific commands
python -m kalx login
python -m kalx register

# Enable debug mode
python -m kalx --debug
```

System themes:
```bash
# Available themes:
- matrix (Classic green cyberpunk)
- neon (Bright neon aesthetics)
- shadow (Dark cyberpunk theme)
```

## 🖲️ Commands Reference

### Basic Commands
```bash
/help                          # Show all commands
/register <username> <email>   # Create new account
/login <username>              # Login to account
/logout                        # End current session
/exit                          # Close application
/info                          # Show system information
/ping                          # Test connection latency
```

### Messaging
```bash
/msg <username> <message>      # Send private message
/r <message>                   # Reply to last message
/clear                         # Clear chat screen
/search <query> [--date] [--from] # Search message history
/encrypt <message>             # Send encrypted message
/file <path>                   # Send file (max 25MB)
```

### Groups
```bash
/creategroup <name> [desc]     # Create new group
/joingroup <code>              # Join existing group
/leavegroup <code>             # Leave current group
/invite <username> <group>     # Invite user to group
/kick <username> <group>       # Remove user from group
/gmsg <group> <message>        # Send group message
/ginfo <group>                 # Show group information
```

### User Management
```bash
/friend <username>             # Add friend
/unfriend <username>           # Remove friend
/block <username>              # Block user
/unblock <username>            # Unblock user
/status <state>                # Set status (online/away/busy)
/profile                       # View/edit your profile
/whois <username>              # Get user information
```

### Admin Commands
```bash
/setadmin <username> <group>   # Promote user to admin
/removeadmin <username> <group> # Demote admin to member
/ban <username> [reason]       # Ban user from platform
/unban <username>              # Unban user
/logs [--system] [--user]      # View system or user logs
/broadcast <message>           # Send message to all users
```

## Project Structure

```
kalX/
├── src/
│   └── kalx/
│       ├── __init__.py
│       ├── __main__.py
│       ├── ui/
│       │   ├── cyberpunk.py     # Cyberpunk visual elements
│       │   ├── console.py       # Console interface
│       │   └── themes.py        # Theme definitions
│       ├── auth/
│       ├── chat/
│       └── utils/
├── tests/
├── docs/
└── README.md
```

## Cyberpunk Module Usage

```python
from kalx.ui.cyberpunk import CyberpunkAnimations, CyberpunkLogos

# Display logos
CyberpunkAnimations.display_logo()  # Main logo
CyberpunkAnimations.display_logo("mini")  # Compact logo
CyberpunkAnimations.display_logo("error")  # Error logo

# Add custom taglines
CyberpunkAnimations.display_logo(tagline="SYSTEM ACTIVE")

# Show animations
CyberpunkAnimations.connection_animation("Establishing secure link")
CyberpunkAnimations.system_check()
```

## 🔧 Troubleshooting

### Common Issues

**Connection Problems**
```bash
# Test network connectivity
kalx --diagnose network

# Reset connection cache
kalx --reset-cache
```

**Authentication Issues**
```bash
# Reset credentials (will require re-login)
kalx --reset-auth

# Verify credentials without full login
kalx --verify-credentials
```

### Logs
View logs for debugging:
```bash
# View last 50 log entries
kalx --logs 50

# Export logs to file
kalx --export-logs kalx_debug.log
```

## 🌟 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Rich library for terminal styling
- Cyberpunk aesthetics inspired by classic sci-fi

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## 🔗 Links

- [Official Website](https://kalx.io)
- [Documentation](https://docs.kalx.io)
- [Issue Tracker](https://github.com/Odeneho-Calculus/kalx/issues)
- [Discord Community](https://discord.gg/kalx)

---

<div align="center">
  <code>Transmitting from the digital underground since 2025</code>
</div>