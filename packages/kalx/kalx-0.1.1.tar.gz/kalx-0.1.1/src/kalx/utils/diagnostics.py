"""
System diagnostics utilities.
"""

import os
import socket
import ssl
import json
import requests
from pathlib import Path
from typing import Dict, List, Tuple
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from kalx.utils.logger import get_logger

logger = get_logger(__name__)
console = Console()

FIREBASE_ENDPOINTS = [
    "firestore.googleapis.com",
    "firebase-auth.googleapis.com",
    "firebase.googleapis.com"
]

def check_connection(host: str, port: int = 443) -> Tuple[bool, str]:
    """Test connection to a host."""
    try:
        socket.create_connection((host, port), timeout=5)
        return True, "Connection successful"
    except Exception as e:
        return False, str(e)

def check_ssl(host: str) -> Tuple[bool, str]:
    """Verify SSL certificate."""
    try:
        ssl_context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with ssl_context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                return True, "SSL verification successful"
    except Exception as e:
        return False, str(e)

def run_network_diagnostics() -> bool:
    """Run network connectivity tests."""
    table = Table(title="Network Diagnostics")
    table.add_column("Test", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Details", style="blue")

    all_passed = True

    with Progress() as progress:
        task = progress.add_task("[cyan]Running network diagnostics...", total=len(FIREBASE_ENDPOINTS) * 2)

        # Test Firebase endpoints
        for endpoint in FIREBASE_ENDPOINTS:
            # Connection test
            success, message = check_connection(endpoint)
            table.add_row(
                f"Connection to {endpoint}",
                "✓" if success else "✗",
                message
            )
            all_passed &= success
            progress.advance(task)

            # SSL test
            success, message = check_ssl(endpoint)
            table.add_row(
                f"SSL verify {endpoint}",
                "✓" if success else "✗",
                message
            )
            all_passed &= success
            progress.advance(task)

    console.print(table)
    
    if all_passed:
        console.print("[green]All network diagnostics passed[/green]")
    else:
        console.print("[red]Some network tests failed[/red]")
    
    return all_passed

def run_auth_diagnostics() -> bool:
    """Run authentication system diagnostics."""
    # Auth system checks would go here
    console.print("[yellow]Auth diagnostics not implemented yet[/yellow]")
    return True

def run_storage_diagnostics() -> bool:
    """Run storage system diagnostics."""
    # Storage system checks would go here
    console.print("[yellow]Storage diagnostics not implemented yet[/yellow]")
    return True

def run_diagnostics(diag_type: str) -> bool:
    """Run specified diagnostics."""
    console.print(f"[bold cyan]Running {diag_type} diagnostics...[/bold cyan]")
    
    try:
        if diag_type == 'network':
            return run_network_diagnostics()
        elif diag_type == 'auth':
            return run_auth_diagnostics()
        elif diag_type == 'storage':
            return run_storage_diagnostics()
        else:
            console.print(f"[red]Unknown diagnostic type: {diag_type}[/red]")
            return False
    except Exception as e:
        logger.error(f"Diagnostic error: {str(e)}")
        console.print(f"[red]Diagnostic failed: {str(e)}[/red]")
        return False
