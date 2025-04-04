"""PowerMap exceptions module."""

class PowerMapError(Exception):
    """Base exception for PowerMap errors."""
    pass


class InvalidGeozoneError(PowerMapError):
    """Exception raised when an invalid geozone is provided."""
    pass


class AuthenticationError(PowerMapError):
    """Exception raised when authentication fails."""
    pass
