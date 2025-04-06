from __future__ import annotations

import os
import json
from pathlib import Path
from .utils import validate_path, get_path_type, ensure_json


class Nook:
    """A Nook is a class that stores a directory for which all user data for this nook is stored"""

    def __init__(self, path: str = None):
        if path is None:
            # Default to user's home directory with .nook folder
            home_dir = Path.home()
            path = os.path.join(home_dir, ".nook")
            # Ensure the default directory exists
            os.makedirs(path, exist_ok=True)
            
        path_type = get_path_type(path)
        if path_type != "folder":
            raise ValueError(
                f"Invalid path provided to Nook, needs to be a valid folder path, instead got: {path}")
        self.path = path

        self.ensure()

    def __enter__(self):
        """Support for context manager protocol"""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Handle cleanup when exiting context manager"""
        # Currently no cleanup needed, but this enables future extensions
        pass

    def ensure(self, path: str | None = None):
        """
        Ensures that the appropriate directory exists

        Args:
            path: Path to ensure exists. Can be absolute or relative to self.path.
                 If None, uses self.path.

        Raises:
            ValueError: If the path is invalid
        """
        # Use self.path if no path provided
        if path is None:
            path_to_check = self.path
            is_relative = False
        else:
            # Determine if path is relative (no drive letter)
            is_relative = not (
                len(path) >= 2 and path[1] == ':' and path[0].isalpha())

            # If relative, join with self.path
            if is_relative:
                path_to_check = os.path.join(self.path, path)
            else:
                path_to_check = path

        # Validate the path
        if not validate_path(path_to_check):
            raise ValueError(f"Invalid path: {path_to_check}")

        # Determine if it's a file or folder
        # If it has an extension, treat as file (simple heuristic)
        is_file = os.path.splitext(path_to_check)[1] != ''

        if is_file:
            # For files, ensure the parent directory exists
            directory = os.path.dirname(path_to_check)
            if not os.path.exists(directory):
                os.makedirs(directory)
        else:
            # For folders, ensure the folder exists
            if not os.path.exists(path_to_check):
                os.makedirs(path_to_check)

        return path_to_check  # Return the full path that was ensured

    def get_all_files(self):
        """
        Returns all files in the entire directory tree

        Returns:
            list: List of file paths relative to the nook root, in the order they are walked
        """
        files = []
        # Walk through the directory tree
        for root, _, filenames in os.walk(self.path):
            # Get the relative path from the nook root
            rel_dir = os.path.relpath(root, self.path)

            # Add each file with its relative path
            for filename in filenames:
                # Construct the relative path correctly
                if rel_dir == '.':
                    rel_path = filename
                else:
                    rel_path = os.path.join(rel_dir, filename)

                files.append(rel_path)

        return files

    def get_all_folders(self):
        """
        Returns all folders in the entire directory tree

        Returns:
            list: List of folder paths relative to the nook root, in the order they are walked
        """
        folders = []
        visited = set()  # Track paths we've already added

        # Walk through the directory tree
        for root, dirnames, _ in os.walk(self.path):
            # Get the relative path from the nook root
            rel_dir = os.path.relpath(root, self.path)

            # Add current directory if not root and not already added
            if rel_dir != '.' and rel_dir not in visited:
                folders.append(rel_dir)
                visited.add(rel_dir)

            # Add subdirectories from current level
            for dirname in dirnames:
                folder_path = dirname if rel_dir == '.' else os.path.join(
                    rel_dir, dirname)

                # Only add if not already added
                if folder_path not in visited:
                    folders.append(folder_path)
                    visited.add(folder_path)

        return folders

    def get_all_content(self):
        """
        Returns all files and folders in the entire directory tree

        Returns:
            list: Combined list of file and folder paths relative to the nook root, in the order they are walked
        """
        content = []
        visited = set()  # Track paths we've already added

        # First add all folders
        for folder in self.get_all_folders():
            content.append(folder)
            visited.add(folder)

        # Then add all files
        for file_path in self.get_all_files():
            if file_path not in visited:
                content.append(file_path)

        return content

    def grep(self, pattern: str):
        """
        Search for a pattern in all files within the nook

        Args:
            pattern: The string pattern to search for

        Returns:
            list: List of dictionaries with 'file', 'line_num', and 'line' keys for each match
        """
        if not pattern:
            return []

        results = []

        # Get all files in the directory tree
        files = self.get_all_files()

        for file_path in files:
            full_path = os.path.join(self.path, file_path)

            try:
                # Open each file and search for the pattern
                with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                    for line_num, line in enumerate(f, 1):
                        if pattern in line:
                            results.append({
                                'file': file_path,
                                'line_num': line_num,
                                'line': line.rstrip('\n')
                            })
            except (IOError, UnicodeDecodeError):
                # Skip files that can't be read
                continue

        return results

    def find(self, pattern: str):
        """
        Search for a pattern in file and folder names within the nook

        Args:
            pattern: The string pattern to search for in names

        Returns:
            dict: Dictionary with 'files' and 'folders' lists containing matching paths
        """
        if not pattern:
            return {'files': [], 'folders': []}

        matching_files = []
        matching_folders = []

        # Get all files and folders
        all_files = self.get_all_files()
        all_folders = self.get_all_folders()

        # Search for pattern in file names/paths
        for file_path in all_files:
            if pattern.lower() in file_path.lower():
                matching_files.append(file_path)

        # Search for pattern in folder names/paths
        for folder_path in all_folders:
            if pattern.lower() in folder_path.lower():
                matching_folders.append(folder_path)

        return {
            'files': matching_files,
            'folders': matching_folders
        }

    def get_setting(self, key: str | list[str], default_value: any = None, path_parts: list[str] | None = None):
        """
        Get a setting from the nook
        
        Args:
            key: The key to get, either a string or a list of strings for nested access
            default_value: The default value if the key doesn't exist
            path_parts: Optional path parts to specify the settings file location
                        Defaults to ["default_settings"]
                        
        Returns:
            The value at the specified key path, or the default value if not found
        """

        if path_parts is None:
            path_parts = ["default_settings"]

        path_parts[-1] += ".json"

        path = os.path.join(self.path, *path_parts).replace("\\", "/")

        self.ensure(path)

        path = ensure_json(path)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Convert string key to list for consistent handling
        keys = [key] if isinstance(key, str) else key
        
        if not keys:
            return default_value
            
        # Navigate to the nested location
        current = data
        for i, k in enumerate(keys[:-1]):
            if k not in current or not isinstance(current[k], dict):
                # Create missing dict or replace non-dict with dict
                current[k] = {}
            current = current[k]
                
        # Check if final key exists
        if keys[-1] not in current:
            # Key doesn't exist, set it to default value
            current[keys[-1]] = default_value
            # Write updated data back to file
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

        return current.get(keys[-1], default_value)

    def set_setting(self, key: str | list[str], value: any, path_parts: list[str] | None = None):
        """
        Set a setting in the nook
        
        Args:
            key: The key to set, either a string or a list of strings for nested access
            value: The value to set for the key
            path_parts: Optional path parts to specify the settings file location
                        Defaults to ["default_settings"]
                        
        Returns:
            The value that was set
        """
        
        if path_parts is None:
            path_parts = ["default_settings"]
            
        path_parts[-1] += ".json"
        
        path = os.path.join(self.path, *path_parts).replace("\\", "/")
        
        self.ensure(path)
        
        path = ensure_json(path)
        
        # Load existing data
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Convert string key to list for consistent handling
        keys = [key] if isinstance(key, str) else key
        
        if not keys:
            return value
            
        # Navigate to the nested location, creating dicts as needed
        current = data
        for k in keys[:-1]:
            if k not in current or not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]
            
        # Set the key with the new value
        current[keys[-1]] = value
        
        # Write updated data back to file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        return value

    def get_settings(self, path_parts: list[str] | None = None):
        """
        Get all settings from a settings file
        
        Args:
            path_parts: Optional path parts to specify the settings file location
                        Defaults to ["default_settings"]
                        
        Returns:
            dict: The complete settings dictionary
        """
        
        if path_parts is None:
            path_parts = ["default_settings"]
            
        path_parts[-1] += ".json"
        
        path = os.path.join(self.path, *path_parts).replace("\\", "/")
        
        self.ensure(path)
        
        path = ensure_json(path)
        
        # Load and return all data
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        return data
        
    def set_settings(self, settings: dict, path_parts: list[str] | None = None):
        """
        Set all settings in a settings file
        
        Args:
            settings: Dictionary containing all settings to save
            path_parts: Optional path parts to specify the settings file location
                        Defaults to ["default_settings"]
                        
        Returns:
            dict: The settings dictionary that was saved
        """
        
        if path_parts is None:
            path_parts = ["default_settings"]
            
        path_parts[-1] += ".json"
        
        path = os.path.join(self.path, *path_parts).replace("\\", "/")
        
        self.ensure(path)
        
        path = ensure_json(path)
        
        # Write settings to file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)
            
        return settings
