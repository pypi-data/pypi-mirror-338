import os
import json


def validate_path(path: str) -> bool:
    """Validates a path to check if it is allowed by the system"""
    if not path:
        return False

    # Windows drive letter pattern (e.g., "D:")
    has_drive_letter = False
    if len(path) >= 2 and path[1] == ':' and path[0].isalpha():
        has_drive_letter = True
        # Remove the drive letter part for the invalid char check
        path_to_check = path[2:]
    else:
        path_to_check = path

    # Check for invalid characters in Windows paths
    invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
    if any(char in path_to_check for char in invalid_chars):
        return False

    # Check for reserved names in Windows
    reserved_names = [
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    ]

    # Split the path and check each component
    parts = path.split(os.sep)
    for part in parts:
        if not part:  # Empty component (like double slashes)
            continue

        # Check if any part is a reserved name
        if part.upper() in reserved_names or part.upper().split('.')[0] in reserved_names:
            return False

        # Check for parts ending with spaces or periods (not allowed in Windows)
        if part.endswith(' ') or part.endswith('.'):
            return False

    # Check path length (Windows has a 260 character limit by default)
    if len(os.path.abspath(path)) > 260:
        return False

    return True


def get_path_type(path: str) -> str:
    """
    Determines if a path is a file or folder.

    Args:
        path: The path to check

    Returns:
        'file' if the path is a file
        'folder' if the path is a directory
        None if the path is invalid or doesn't exist
    """
    # First validate the path
    if not validate_path(path):
        return None

    # Initial assumption based on extension
    has_extension = os.path.splitext(os.path.basename(path))[1] != ''
    assumed_type = "file" if has_extension else "folder"

    # If path exists, determine the actual type
    if os.path.exists(path):
        if os.path.isfile(path):
            return "file"
        elif os.path.isdir(path):
            return "folder"
        return None  # rare case (not a file or folder)

    # If path doesn't exist, return the assumed type
    return assumed_type


def as_folder(path: str) -> str:
    if not validate_path(path):
        raise ValueError(f"Invalid path: {path}")

    if get_path_type(path) == "folder":
        return path

    # return parent folder
    return os.path.dirname(path)


def ensure_json(json_path: str) -> str:
    """
    Ensures a JSON file exists at the specified path.
    If it doesn't exist, creates an empty JSON file with {}.
    If it exists but is empty, initializes it with {}.
    If it exists but contains invalid JSON, raises an error.

    Args:
        json_path: Path to the JSON file

    Returns:
        The validated json_path

    Raises:
        ValueError: If the path is invalid
        json.JSONDecodeError: If the file contains invalid JSON
    """
    if not validate_path(json_path):
        raise ValueError(f"Invalid JSON path: {json_path}")

    # Create parent directories if they don't exist
    parent_dir = os.path.dirname(json_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)

    # Check if file exists
    if os.path.exists(json_path):
        # File exists, check its content
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                # File has content, try to parse it
                try:
                    json.loads(content)
                except json.JSONDecodeError as e:
                    raise json.JSONDecodeError(
                        f"Invalid JSON in {json_path}: {str(e)}", e.doc, e.pos)
            else:
                # File is empty, initialize it
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
    else:
        # Create the JSON file if it doesn't exist
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    return json_path
