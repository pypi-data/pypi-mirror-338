class DrebedengiError(Exception):
    """Base exception for all SDK-related errors."""
    pass

class DrebedengiConnectionError(DrebedengiError):
    """Raised when there is a network or connection issue."""
    pass

class DrebedengiAPIError(DrebedengiError):
    """Raised when the API returns an error response."""
    pass
