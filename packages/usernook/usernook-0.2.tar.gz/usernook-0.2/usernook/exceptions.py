class NookError(Exception):
    """Base exception for UserNook errors"""
    pass

class InvalidPathError(NookError):
    """Raised when a path is invalid"""
    pass

class PathTypeError(NookError):
    """Raised when a path is of incorrect type (file vs folder)"""
    pass

class JSONError(NookError):
    """Raised when there are issues with JSON operations"""
    pass

class SettingsError(NookError):
    """Raised when there are issues with settings operations"""
    pass

class FileOperationError(NookError):
    """Raised when file operations fail"""
    pass 