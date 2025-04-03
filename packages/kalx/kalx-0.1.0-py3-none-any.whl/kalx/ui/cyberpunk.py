from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich.columns import Columns
from rich.layout import Layout
from rich import box
from rich.table import Table
import time
import random
import string
import sys
import threading
from typing import List, Optional, Tuple

# Enhanced Matrix-inspired color palette
MATRIX_GREEN = "#00FF41"
MATRIX_DARK_GREEN = "#008F11"
MATRIX_LIGHT_GREEN = "#7FFF00"
NEON_BLUE = "#4DEEEA"
NEON_PINK = "#FF10F0"
NEON_PURPLE = "#BD00FF"
CYBER_YELLOW = "#FFD700"
CYBER_RED = "#FF3F3F"
MATRIX_BLACK = "#0D0208"

# Rich console setup
console = Console()

class MatrixRain:
    """Generate digital rain animation effect."""

    def __init__(self, width: int = 80, height: int = 15, density: float = 0.05, speed: float = 0.1):
        self.width = width
        self.height = height
        self.density = density
        self.speed = speed
        self.drops = []
        # Modified to use only binary digits (0s and 1s)
        self.chars = "01"
        self.running = False
        self.thread = None
        self._initialize_drops()

    def _initialize_drops(self):
        """Initialize the rain drops with more density."""
        self.drops = []
        # Increased density for more visible rain effect
        for x in range(self.width):
            if random.random() < self.density * 2:  # Doubled the density
                self.drops.append({
                    'x': x,
                    'y': random.randint(-self.height, 0),
                    'length': random.randint(5, 20),  # Increased max length
                    'speed': random.random() * self.speed + 0.05,
                    'chars': [random.choice(self.chars) for _ in range(20)],
                    'brightness': random.random()
                })

    def _update_drops(self):
        """Update the positions of rain drops."""
        for drop in self.drops[:]:
            drop['y'] += drop['speed']

            # Randomly change some characters, only using 0 and 1
            for i in range(len(drop['chars'])):
                if random.random() < 0.2:  # Increased probability of character change
                    drop['chars'][i] = random.choice(self.chars)

            # Remove drops that go off screen and add new ones
            if drop['y'] > self.height + drop['length']:
                self.drops.remove(drop)
                if random.random() < self.density * 4:  # Increased probability of new drops
                    self.drops.append({
                        'x': random.randint(0, self.width - 1),
                        'y': random.randint(-self.height, 0),
                        'length': random.randint(5, 20),
                        'speed': random.random() * self.speed + 0.05,
                        'chars': [random.choice(self.chars) for _ in range(20)],  # Only binary
                        'brightness': random.random()
                    })

    def _render(self) -> str:
        """Render the digital rain effect."""
        # Create a grid of spaces
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # Place each drop in the grid
        for drop in self.drops:
            for i in range(drop['length']):
                y = int(drop['y']) - i
                if 0 <= y < self.height and 0 <= drop['x'] < self.width:
                    if i == 0:
                        # Head of the drop is brighter
                        char_idx = i % len(drop['chars'])
                        grid[y][drop['x']] = f"[bold {MATRIX_LIGHT_GREEN}]{drop['chars'][char_idx]}[/]"
                    else:
                        # Body of the drop fades with distance from head
                        fade = min(1.0, i / drop['length'])
                        intensity = int(100 - (fade * 75))
                        color = f"#{int(intensity * 0.01 * int(MATRIX_GREEN[1:3], 16)):02x}{int(intensity * 0.01 * int(MATRIX_GREEN[3:5], 16)):02x}{int(intensity * 0.01 * int(MATRIX_GREEN[5:7], 16)):02x}"
                        char_idx = i % len(drop['chars'])
                        grid[y][drop['x']] = f"[{color}]{drop['chars'][char_idx]}[/]"

        # Convert grid to string
        return "\n".join("".join(row) for row in grid)

    def start(self, duration: float = 10.0):  # Default duration increased to 10 seconds
        """Start the animation for a specified duration."""
        self.running = True
        self.thread = threading.Thread(target=self._run_animation, args=(duration,))
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """Stop the animation."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)

    def _run_animation(self, duration: float):
        """Run the animation for a specified duration."""
        start_time = time.time()
        try:
            with Live(self._render(), refresh_per_second=15, screen=True) as live:  # Increased refresh rate
                while self.running and (time.time() - start_time < duration):
                    self._update_drops()
                    live.update(self._render())
                    time.sleep(0.05)
        except Exception:
            # Silently handle any errors without showing stack traces
            self.running = False

class TerminalGlitch:
    """Terminal glitch effects."""

    @staticmethod
    def glitch_text(text: str, intensity: float = 0.3) -> str:
        """Apply glitch effect to text."""
        glitch_chars = "!@#$%^&*()_+-=[]\\{}|;':\",./<>?`~01"  # Added binary digits
        result = list(text)

        for _ in range(int(len(text) * intensity)):
            idx = random.randint(0, len(text) - 1)
            if random.random() < 0.5:
                # Replace with glitch char
                result[idx] = random.choice(glitch_chars)
            else:
                # Shift case
                if result[idx].isalpha():
                    result[idx] = result[idx].swapcase()

        return "".join(result)

    @staticmethod
    def animate_glitch(text: str, duration: float = 1.0, intensity: float = 0.3):
        """Animate text with glitch effect."""
        try:
            end_time = time.time() + duration
            frames = int(duration * 10)  # 10 frames per second

            with console.status("", spinner="dots") as status:
                for _ in range(frames):
                    if time.time() >= end_time:
                        break

                    # Display glitched text
                    status.update(f"[bold {MATRIX_GREEN}]{TerminalGlitch.glitch_text(text, intensity)}[/]")
                    time.sleep(1.0 / 10)

            # Show final clean text
            console.print(f"[bold {MATRIX_GREEN}]{text}[/]")
        except Exception:
            # Silently handle any errors
            console.print(f"[bold {MATRIX_GREEN}]{text}[/]")

class CyberpunkTemplates:
    """Handles safe string templating for cyberpunk UI elements"""

    @staticmethod
    def format_safe(text: str, **kwargs) -> str:
        """Safely format a string with variables"""
        try:
            return text.format(**kwargs)
        except Exception:
            return text

class CyberpunkLogos:
    """Collection of cyberpunk-styled logos"""

    @staticmethod
    def format_error_message(error_text: str) -> str:
        """Format error message to fit the error logo width"""
        max_width = 36  # Width of error logo
        if len(error_text) > max_width:
            return error_text[:max_width-3] + "..."
        return error_text

    @staticmethod
    def get_error_box(message: str) -> str:
        """Create an error box with a message"""
        formatted_msg = CyberpunkLogos.format_error_message(message)
        width = max(len(formatted_msg) + 4, 40)
        top = f"╔{'═' * (width-2)}╗"
        middle = f"║ {formatted_msg.center(width-4)} ║"
        bottom = f"╚{'═' * (width-2)}╝"
        return f"{top}\n{middle}\n{bottom}"

    @staticmethod
    def get_main_logo() -> str:
        """Get the main Matrix-inspired kalX logo"""
        return (
            r"    ██╗  ██╗ █████╗ ██╗     ██╗  ██╗" + "\n" +
            r"    ██║ ██╔╝██╔══██╗██║     ╚██╗██╔╝" + "\n" +
            r"    █████╔╝ ███████║██║      ╚███╔╝ " + "\n" +
            r"    ██╔═██╗ ██╔══██║██║      ██╔██╗ " + "\n" +
            r"    ██║  ██╗██║  ██║███████╗██╔╝ ██╗" + "\n" +
            r"    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
        )

    @staticmethod
    def get_mini_logo() -> str:
        """Get the mini logo with Matrix styling"""
        return (
            r"┌┐┌┌─┐┬ ┬┬─┐┌─┐┬    ┬┌┐┌┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐" + "\n" +
            r"││││ │├─┤├┬┘├─┤│    ││││ │ ├┤ ├┬┘├┤ ├─┤└─┐├┤ " + "\n" +
            r"┘└┘└─┘┴ ┴┴└─┴ ┴┴─┘  ┴┘└┘ ┴ └─┘┴└─└  ┴ ┴└─┘└─┘"
        )

    @staticmethod
    def get_matrix_logo() -> str:
        """Get a Matrix-inspired logo"""
        return (
            r"    ┌┬┐┌─┐┌┬┐┬─┐┬─┐ ┬" + "\n" +
            r"    │││├─┤ │ ├┬┘│┌┴┬┘" + "\n" +
            r"    ┴ ┴┴ ┴ ┴ ┴└─┴┴ └─" + "\n" +
            r"    ╔══════════════╗" + "\n" +
            r"    ║ Follow the   ║" + "\n" +
            r"    ║ white rabbit ║" + "\n" +
            r"    ╚══════════════╝"
        )

    @staticmethod
    def get_welcome_message() -> str:
        """Get the matrix-inspired welcome message"""
        return (
            "Wake up, User...\n"
            "The Matrix has you...\n"
            "Follow the white rabbit.\n"
            "Welcome to the kalX Neural Interface Terminal."
        )

    @staticmethod
    def generate_ascii_art_text(text: str) -> str:
        """Generate simple ASCII art text"""
        # This is a simplified function - in a real app you might use a library like pyfiglet
        result = []

        # Simple character mappings for capital letters
        ascii_chars = {
            'K': [" /|  ", "/K|  ", "K_|_ "],
            'A': ["  /\\  ", " /--\\ ", "/    \\"],
            'L': ["|    ", "|    ", "|___ "],
            'X': ["\\  / ", " \\/ ", " /\\ "]
        }

        height = 3  # Fixed height for this simple implementation

        # Initialize result lines
        for _ in range(height):
            result.append("")

        # Build each line
        for char in text.upper():
            if char in ascii_chars:
                for i in range(height):
                    result[i] += ascii_chars[char][i]
            else:
                for i in range(height):
                    result[i] += "     "  # Space for unknown chars

        return "\n".join(result)

class CyberpunkAnimations:
    """Collection of Matrix-inspired cyberpunk animations"""

    @staticmethod
    def display_logo(logo_type="main", tagline=None, error_message=None, welcome_message=None):
        """Display a cyberpunk logo with optional tagline and welcome message"""
        try:
            # Digital rain effect before displaying the logo
            rain = MatrixRain(width=70, height=15, density=10.15)  # Increased density
            rain.start(duration=10.0)  # Set to 10 seconds
            time.sleep(10.0)  # Wait for the rain to finish

            # Set up basic parameters
            if error_message:
                logo_text = CyberpunkLogos.get_error_box(error_message)
                style = border_style = CYBER_RED
                title = "SYSTEM FAILURE"
            elif logo_type == "main":
                logo_text = CyberpunkLogos.get_main_logo()
                style = MATRIX_GREEN
                border_style = MATRIX_DARK_GREEN
                title = "NEURAL LINK"
            elif logo_type == "mini":
                logo_text = CyberpunkLogos.get_mini_logo()
                style = border_style = MATRIX_GREEN
                title = "NEURAL LINK"
            elif logo_type == "matrix":
                logo_text = CyberpunkLogos.get_matrix_logo()
                style = border_style = MATRIX_GREEN
                title = "THE MATRIX"
            else:
                logo_text = CyberpunkLogos.get_main_logo()
                style = MATRIX_GREEN
                border_style = MATRIX_DARK_GREEN
                title = "NEURAL LINK"

            # Build content directly with Rich markup
            content = f"[{style}]{logo_text}[/{style}]"

            if tagline:
                # Apply glitch effect to the tagline text
                content += f"\n\n[{MATRIX_LIGHT_GREEN}]"

                # Show the tagline with a typing effect
                TerminalGlitch.animate_glitch(tagline, duration=1.0, intensity=0.2)

            if welcome_message:
                content += f"\n\n[{NEON_BLUE}]{welcome_message}[/{NEON_BLUE}]"

            # Create panel with direct content
            panel = Panel(
                content,
                title=title,
                border_style=border_style,
                box=box.HEAVY,
                expand=False,
                padding=(1, 2)
            )

            console.print(panel)

        except Exception:
            # Simple fallback display without revealing error details
            try:
                console.print(f"[{MATRIX_GREEN}]{logo_text}[/{MATRIX_GREEN}]")
                if tagline:
                    console.print(f"[{MATRIX_GREEN}]{tagline}[/{MATRIX_GREEN}]")
                if welcome_message:
                    console.print(f"[{NEON_BLUE}]{welcome_message}[/{NEON_BLUE}]")
            except Exception:
                # Ultimate fallback
                console.print(f"[{MATRIX_GREEN}]System Interface Loaded[/{MATRIX_GREEN}]")

    @staticmethod
    def matrix_typing_effect(text: str, speed: float = 0.03):
        """Display text with a Matrix-style typing effect."""
        try:
            # Fixed: Completely rewritten to avoid the character glitching issue
            styled_text = Text()

            for char in text:
                # Add character with proper styling
                styled_text.append(char, style=f"{MATRIX_GREEN}")

                # Print the entire text so far
                console.print(styled_text, end="\r")

                # Random delay for typing effect
                time.sleep(speed * (1.0 + random.random() * 0.3))

            # Final newline
            console.print()
        except Exception:
            # Fallback without showing error details
            console.print(f"[{MATRIX_GREEN}]{text}[/{MATRIX_GREEN}]")

    @staticmethod
    def connection_animation(message="Establishing neural connection", duration=1.0):
        """Display a Matrix-style connection animation"""
        try:
            # First show digital static noise - only binary
            try:
                for _ in range(5):  # Increased repetitions
                    # Only binary digits
                    noise = "".join(random.choice("01") for _ in range(70))
                    console.print(f"[{MATRIX_DARK_GREEN}]{noise}[/{MATRIX_DARK_GREEN}]")
                    time.sleep(0.1)
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]Initializing connection...[/bold {MATRIX_LIGHT_GREEN}]")

            console.print()

            try:
                with Progress(
                    SpinnerColumn(spinner_name="dots"),
                    TextColumn(f"[{MATRIX_GREEN}]{{task.description}}[/{MATRIX_GREEN}]"),
                    BarColumn(bar_width=40, complete_style=MATRIX_LIGHT_GREEN),
                    console=console,
                    transient=True,
                ) as progress:
                    task = progress.add_task(f"[bold {MATRIX_GREEN}]{message}", total=100)
                    for i in range(1, 101):
                        progress.update(task, completed=i)

                        # Occasionally show "signal trace" messages
                        if i % 20 == 0 and i > 0:
                            trace_msg = random.choice([
                                "Bypassing ICE protocol...",
                                "Tracing neural pathways...",
                                "Syncing neural interface...",
                                "Decrypting signal...",
                                "Establishing secure tunnel..."
                            ])
                            #progress.log(f"[dim {MATRIX_DARK_GREEN}]> {trace_msg}[/dim {MATRIX_DARK_GREEN}]")

                        time.sleep(duration/100)
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]Connection process interrupted.[/bold {MATRIX_LIGHT_GREEN}]")

            # Show code-like trace log after connection - only using binary
            try:
                console.print()
                for _ in range(3):
                    log_line = f"[{MATRIX_DARK_GREEN}]" + "".join(random.choice("01") for _ in range(32))
                    log_line += f"[/{MATRIX_DARK_GREEN}]"
                    console.print(log_line)
                    time.sleep(0.1)

                console.print()
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]CONNECTION ESTABLISHED[/bold {MATRIX_LIGHT_GREEN}]")
                time.sleep(0.3)
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]Finalizing connection...[/bold {MATRIX_LIGHT_GREEN}]")
        except Exception:
            # Fallback without showing error details
            console.print(f"[bold {MATRIX_LIGHT_GREEN}]CONNECTION ESTABLISHED[/bold {MATRIX_LIGHT_GREEN}]")


    @staticmethod
    def system_check(checks=None):
        """Run a Matrix-style system check animation"""
        try:
            if checks is None:
                checks = [
                    "Neural Pathways",
                    "Quantum Cores",
                    "Memory Substrate",
                    "Cryptographic Matrix",
                    "Interface Protocols",
                    "Reality Distortion Field",
                    "Proxy Connections"
                ]

            # Start with digital rain effect
            try:
                rain = MatrixRain(width=70, height=10, density=10.15)  # Increased density
                rain.start(duration=10.0)  # Increased to 10 seconds
                time.sleep(10.0)  # Wait for animation
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]Initializing system diagnostic...[/bold {MATRIX_LIGHT_GREEN}]")

            console.print(f"[bold {MATRIX_LIGHT_GREEN}]Initializing system diagnostic...[/bold {MATRIX_LIGHT_GREEN}]")
            time.sleep(0.3)

            # First show quick system information
            info_table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
            info_table.add_column("Key", style=MATRIX_DARK_GREEN)
            info_table.add_column("Value", style=MATRIX_GREEN)

            info_table.add_row("System", "kalX Neural Matrix v1.0.0")
            info_table.add_row("Kernel", f"NeoCore {random.randint(3, 9)}.{random.randint(1, 9)}.{random.randint(1, 99)}")
            info_table.add_row("Memory", f"{random.randint(16, 64)}TB Neural Cache")
            info_table.add_row("Network", "Secured Quantum Tunnel")

            console.print(info_table)
            time.sleep(0.5)

            console.print()
            console.print(f"[{MATRIX_GREEN}]Running neural diagnostics...[/{MATRIX_GREEN}]")
            time.sleep(0.2)

            # Enhanced progress bars with Matrix aesthetic
            try:
                with Progress(
                    TextColumn("{task.description}"),
                    BarColumn(bar_width=40, complete_style=MATRIX_LIGHT_GREEN, finished_style=MATRIX_LIGHT_GREEN),
                    TextColumn("{task.percentage:.0f}%"),
                    console=console,
                    expand=True,
                ) as progress:
                    tasks = {check: progress.add_task(f"[{MATRIX_GREEN}]Scanning {check}", total=100)
                            for check in checks}

                    for _ in range(20):
                        time.sleep(0.05)
                        for check, task_id in tasks.items():
                            if not progress.tasks[task_id].completed:
                                # More realistic progress - some systems check faster than others
                                advance = random.uniform(3.0, 7.0)
                                progress.update(task_id, advance=advance)

                                # Occasionally show trace logs during check
                                if random.random() < 0.05:
                                    progress.log(f"[dim {MATRIX_DARK_GREEN}]> {check}: {random.choice(['OPTIMAL', 'NOMINAL', 'FUNCTIONAL'])}[/dim {MATRIX_DARK_GREEN}]")

                    # Ensure all tasks complete
                    for task_id in tasks.values():
                        progress.update(task_id, completed=100)
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]System check interrupted.[/bold {MATRIX_LIGHT_GREEN}]")

            # Final system status with a table
            try:
                console.print()
                status_table = Table(title="System Status", box=box.HEAVY, title_style=MATRIX_LIGHT_GREEN, border_style=MATRIX_DARK_GREEN)
                status_table.add_column("System", style=MATRIX_GREEN)
                status_table.add_column("Status", style=MATRIX_LIGHT_GREEN)
                status_table.add_column("Efficiency", style=MATRIX_DARK_GREEN)

                for check in checks:
                    status = random.choice(["OPTIMAL", "NOMINAL", "EXCELLENT"])
                    efficiency = f"{random.randint(92, 99)}.{random.randint(0, 9)}%"
                    status_table.add_row(check, status, efficiency)

                console.print(status_table)
                console.print()
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]All systems operational. The Matrix is online.[/bold {MATRIX_LIGHT_GREEN}]")
                time.sleep(0.5)
            except Exception:
                console.print(f"[bold {MATRIX_LIGHT_GREEN}]System status display failed.[/bold {MATRIX_LIGHT_GREEN}]")
        except Exception:
            # Fallback without showing error details
            console.print(f"[bold {MATRIX_LIGHT_GREEN}]System check complete.[/bold {MATRIX_LIGHT_GREEN}]")


    @staticmethod
    def data_stream_effect(duration: float = 2.0):
        """Display a Matrix-style data stream effect"""
        try:
            start_time = time.time()
            while time.time() - start_time < duration:
                # Generate a random line of binary only
                line = ""
                for _ in range(random.randint(40, 70)):
                    line += random.choice("01")

                # Vary the color slightly
                if random.random() < 0.1:
                    color = MATRIX_LIGHT_GREEN
                else:
                    color = MATRIX_GREEN

                console.print(f"[{color}]{line}[/{color}]")
                time.sleep(0.05)
        except Exception:
            # Silently handle errors
            pass

    @staticmethod
    def decode_text_effect(final_text: str, duration: float = 2.0):
        """Display a Matrix-style text decoding effect"""
        try:
            # Fixed: Better decoding effect using only binary for undecoded chars
            chars = "01"  # Only binary characters for the effect
            text_length = len(final_text)
            decoded = [""] * text_length
            is_decoded = [False] * text_length

            iterations = int(duration * 10)  # 10 iterations per second

            # Gradually decode the text
            for iteration in range(iterations):
                # Determine how many characters to decode in this iteration
                progress = iteration / iterations
                target_decoded = int(progress * text_length)

                # Decode some new characters
                while sum(is_decoded) < target_decoded:
                    idx = random.randint(0, text_length - 1)
                    if not is_decoded[idx]:
                        decoded[idx] = final_text[idx]
                        is_decoded[idx] = True

                # Create the current state with random characters for undecoded positions
                current = []
                for i in range(text_length):
                    if is_decoded[i]:
                        current.append(decoded[i])
                    else:
                        current.append(random.choice(chars))

                # Create a rich text object for proper rendering
                display_text = Text("".join(current), style=MATRIX_GREEN)
                console.print(display_text, end="\r")
                time.sleep(0.1)

            # Final decoded text with proper styling
            console.print(f"[bold {MATRIX_LIGHT_GREEN}]{final_text}[/bold {MATRIX_LIGHT_GREEN}]")
        except Exception:
            # Fallback without showing error details
            console.print(f"[bold {MATRIX_LIGHT_GREEN}]{final_text}[/bold {MATRIX_LIGHT_GREEN}]")

    @staticmethod
    def matrix_banner():
        """Display an animated Matrix-style banner"""
        try:
            # Initialize the MatrixRain effect with higher density
            rain = MatrixRain(width=70, height=15, density=10.15)
            rain.start(duration=10.0)  # Changed to 10 seconds
            time.sleep(10.0)  # Let the rain effect display for 10 seconds

            # First show the "Wake up..." message with typing effect
            console.print()
            CyberpunkAnimations.matrix_typing_effect("Wake up, User...", speed=0.08)
            time.sleep(0.5)
            CyberpunkAnimations.matrix_typing_effect("The Matrix has you...", speed=0.08)
            time.sleep(0.5)
            CyberpunkAnimations.matrix_typing_effect("Follow the white rabbit.", speed=0.08)
            time.sleep(0.5)

            # Show the main logo with a decode effect
            logo_lines = CyberpunkLogos.get_main_logo().split("\n")
            for line in logo_lines:
                CyberpunkAnimations.decode_text_effect(line, duration=0.2)

            # Show the tagline
            time.sleep(0.5)
            console.print()
            CyberpunkAnimations.decode_text_effect("NEURAL INTERFACE v2.0", duration=1.0)
            console.print()

            # Final system message
            time.sleep(0.5)
            CyberpunkAnimations.matrix_typing_effect("Initializing neural link...", speed=0.05)
            time.sleep(0.2)
        except Exception:
            # Fallback without showing error details
            console.print(f"[bold {MATRIX_GREEN}]NEURAL INTERFACE v2.0[/bold {MATRIX_GREEN}]")
            console.print(f"[{MATRIX_GREEN}]Initializing neural link...[/{MATRIX_GREEN}]")

    @staticmethod
    def display_menu(title="NEURAL COMMAND INTERFACE", options=None):
        """Display a cyberpunk-styled menu with options"""
        try:
            if options is None:
                options = [
                    {"key": "1", "label": "Login", "description": "Access your neural profile"},
                    {"key": "2", "label": "Register", "description": "Create a new neural identity"},
                    {"key": "3", "label": "Quit", "description": "Disconnect from the system"}
                ]

            # Calculate width based on content
            max_length = max([len(opt["label"]) + len(opt["description"]) + 10 for opt in options])
            width = max(max_length + 10, len(title) + 10)

            panel_content = Text("\n")

            # Add each menu option
            for opt in options:
                option_text = f"   {opt['key']}. {opt['label']}"
                padding = " " * (15 - len(option_text))
                description = opt["description"]
                panel_content.append(f"{option_text}{padding}{description}\n")

            panel_content.append("\n")

            # Create and display the panel
            panel = Panel(
                panel_content,
                title=title,
                border_style=MATRIX_GREEN,
                box=box.HEAVY,
                width=width,
                padding=(0, 2)
            )

            console.print(panel)
            return console.input(f"Select neural command [{'/'.join([opt['key'] for opt in options])}]: ")
        except Exception:
            # Fallback without showing error details
            console.print(f"[{MATRIX_GREEN}]{title}[/{MATRIX_GREEN}]")
            for opt in options:
                console.print(f"[{MATRIX_GREEN}]{opt['key']}. {opt['label']} - {opt['description']}[/{MATRIX_GREEN}]")
            return console.input(f"Select option [{'/'.join([opt['key'] for opt in options])}]: ")
