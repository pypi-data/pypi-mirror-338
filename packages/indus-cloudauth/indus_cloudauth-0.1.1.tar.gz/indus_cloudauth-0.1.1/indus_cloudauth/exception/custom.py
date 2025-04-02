from typing import Optional

class EnvironmentVariableNotFoundError(Exception):
    """Exception raised when a required environment variable is not found.

    This exception should be raised when a critical environment variable
    that is required for the application to function is missing or empty.

    Attributes:
        variable_name (str): The name of the missing environment variable.
        message (str): Explanation of the error with remediation suggestions.
    """

    def __init__(self, variable_name: str, message: Optional[str] = None) -> None:
        """Initialize the exception with variable name and custom message.

        Args:
            variable_name: Name of the missing environment variable.
            message: Optional custom error message. If not provided, a default
                message with remediation advice will be used.

        Example:
            >>> raise EnvironmentVariableNotFoundError("API_KEY")
            EnvironmentVariableNotFoundError: Required environment variable 'API_KEY' not found.
            Please set this variable in your environment or .env file.
        """
        self.variable_name = variable_name
        self.message = message or (
            f"Required environment variable '{variable_name}' not found.\n"
            f"Please set this variable in your environment or .env file."
        )
        super().__init__(self.message)

    def __str__(self) -> str:
        """Return the formatted error message."""
        return self.message