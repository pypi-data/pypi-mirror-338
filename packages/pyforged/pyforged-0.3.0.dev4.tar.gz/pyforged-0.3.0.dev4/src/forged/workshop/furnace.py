import os
import sys
import tempfile
import platform
from pathlib import Path

from forged.commons.utilities.host import get_temp_dir, get_home_dir
from forged.elements.reporting import logger, setup_logger
from forged.commons.patterns.project import ProjectToml
from forged.commons.utilities.pyth import is_package_installed

import tempfile

# Set Paths

def get_program_files_paths():
    """Returns common global application install directories by OS."""
    system = platform.system()

    if system == 'Windows':
        return [
            os.environ.get('ProgramFiles', 'C:\\Program Files'),
            os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')
        ]
    elif system == 'Darwin':  # macOS
        return ['/Applications', '/usr/local/bin']
    elif system == 'Linux':
        return ['/usr/bin', '/usr/local/bin', '/opt', '/snap']
    else:
        return []

if __name__ == "__main__":
    os.environ.update({"FORGED_PATH": os.path.join(get_home_dir(), 'PyForged')})
    # Create a temporary log file
    temp_log_file = tempfile.NamedTemporaryFile(suffix=".log", dir=get_temp_dir(), delete=False)
    log_file_path = temp_log_file.name


    pyforged = ProjectToml(f"C:/Users/aidan/PycharmProjects/Forged/pyproject.toml")

    logger.info(f"Loading PyForged {pyforged.version}")
    logger.info(f"Found {len(pyforged.dependencies)} dependencies.")

    if not os.path.isdir(os.path.join(get_home_dir(), 'PyForged')):
        logger.info("PyForged not found in Program Files, installing...")
        os.mkdir(os.path.join(get_home_dir(), 'PyForged'))
    else:
        logger.success(f"Found: {os.path.join(get_home_dir(), 'PyForged')}")

    from forged.elements.configured.manager import ConfigManager

    from forged.elements.named import Namespace, CompositeNamespace

    logger.info("Establishing namespaces. . .")
    forged_ns = Namespace('forged')
    main_ns = CompositeNamespace(forged_ns)
    logger.success(f"Main namespace created with {len(main_ns.namespaces)} primary registrations.")