from sys import platform
from platform import uname
from os import name as os_name

def is_windows() -> bool:
    return platform.startswith("win")

def is_mac() -> bool:
    return platform == "darwin"

def is_linux() -> bool:
    return platform.startswith("linux")

def is_wsl() -> bool:
    """Detect if running inside Windows Subsystem for Linux (WSL)."""
    if is_linux():
        try:
            with open("/proc/version", "r") as f:
                return "microsoft" in f.read().lower()
        except FileNotFoundError:
            return False
    return False

def is_unix() -> bool:
    return is_linux() or is_mac()

def is_posix() -> bool:
    return os_name == "posix"

def is_arm() -> bool:
    """Detect if the system is running on an ARM architecture."""
    return "arm" in uname().machine.lower() or "aarch" in uname().machine.lower()

def is_x86() -> bool:
    """Detect if the system is running on an x86 architecture."""
    return uname().machine.lower() in ["x86_64", "amd64", "i386", "i686"]

def network_name() -> str:
    """Get the network name of the machine."""
    return uname().node
