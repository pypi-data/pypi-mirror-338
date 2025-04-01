from typing import Optional


class GitError(Exception):
    """An exception raised when something goes wrong while running the git operation."""
    pass


class MultipleValuesError(GitError):
    """Multiple values for a key encountered in an operation that supports only a single
    value."""
    pass


class _HandledError(GitError):
    """An internal indication of a git error to be handled."""
    def __init__(self, code: int, stdout: Optional[str] = None):
        self.code = code
        self.stdout = stdout
        super().__init__()
