class RaiseError:
    """Provides a side effect that can raise an exception.

    This class is useful for creating a mock side effect, allowing an exception to be
    raised without the need to create an anonymous class. It is particularly helpful
    because lambda functions cannot raise exceptions directly.

    """

    error: Exception
    """The exception to be raised when the instance is called."""

    def __init__(self, error: Exception) -> None:
        """Initialize the RaiseError instance with a given exception.

        :param error: The exception instance to encapsulate within the custom error.

        """
        self.error = error

    def __call__(self, *args: tuple, **kwargs: dict) -> None:
        """Represent a callable class that raises an error when invoked.

        This class implements the `__call__` magic method, allowing its instances to be
        used as a sideeffect callback. When an instance is called, it will immediately
        raise an error. The specific error to be raised is provided during the
        instantiation of the class. This allows the user to simulate errors in function
        calls for testing or other purposes.

        :param args: Positional arguments (catch all).
        :param kwargs: Keyword arguments (catch all).
        :return: This method does not return any value.
        :raises: The error specified during the instance creation of the class.

        """
        raise self.error
