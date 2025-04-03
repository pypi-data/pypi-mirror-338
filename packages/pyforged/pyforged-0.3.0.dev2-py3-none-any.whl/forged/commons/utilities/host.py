import platform
import os
import sys
import tempfile
from pathlib import Path


def get_program_files_paths():
    system = platform.system()

    if system == 'Windows':
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        program_files_x86 = os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')
        return [program_files, program_files_x86]

    elif system == 'Darwin':  # macOS
        return ['/Applications', '/usr/local/bin']

    elif system == 'Linux':
        return ['/usr/bin', '/usr/local/bin', '/opt', '/snap']

    else:
        return []

if __name__ == "__main__":
    paths = get_program_files_paths()
    print("Program installation directories:", paths)


def get_temp_dir():
    """Returns the system temporary directory."""
    return tempfile.gettempdir()


def get_home_dir():
    """Returns the user's home directory."""
    return str(Path.home())


def get_config_dir():
    """Returns the user-specific configuration directory, platform-aware."""
    home = get_home_dir()
    system = platform.system()

    if system == 'Windows':
        return os.getenv('APPDATA', os.path.join(home, 'AppData', 'Roaming'))
    elif system == 'Darwin':  # macOS
        return os.path.join(home, 'Library', 'Application Support')
    else:  # Linux and others
        return os.getenv('XDG_CONFIG_HOME', os.path.join(home, '.config'))


def get_python_install_dir():
    """Returns the base Python installation directory."""
    return sys.prefix
