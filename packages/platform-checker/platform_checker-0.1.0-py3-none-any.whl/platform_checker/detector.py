from sys import platform
from platform import machine
from os import name as os_name

def is_windows():
    return platform.startswith("win")

def is_mac():
    return platform == "darwin"

def is_linux():
    return platform.startswith("linux")

def is_wsl():
    """Detect if running inside Windows Subsystem for Linux (WSL)."""
    if is_linux():
        try:
            with open("/proc/version", "r") as f:
                return "microsoft" in f.read().lower()
        except FileNotFoundError:
            return False
    return False

def is_unix():
    return is_linux() or is_mac()

def is_posix():
    return os_name == "posix"

def is_arm():
    """Detect if the system is running on an ARM architecture."""
    return "arm" in machine().lower() or "aarch" in machine().lower()

def is_x86():
    """Detect if the system is running on an x86 architecture."""
    return machine().lower() in ["x86_64", "amd64", "i386", "i686"]
