class PromptOpsError(Exception):
    """Base exception for PromptOps client errors."""
    def __init__(self, message=None, http_status=None, response=None):
        self.message = message
        self.http_status = http_status
        self.response = response
        super().__init__(self.message)


class AuthenticationError(PromptOpsError):
    """Exception raised for authentication errors."""
    pass


class ResourceNotFoundError(PromptOpsError):
    """Exception raised when requested resource is not found."""
    pass


class ValidationError(PromptOpsError):
    """Exception raised for validation errors."""
    pass


class ServerError(PromptOpsError):
    """Exception raised for server errors."""
    pass


class RateLimitError(PromptOpsError):
    """Exception raised when rate limit is exceeded."""
    pass