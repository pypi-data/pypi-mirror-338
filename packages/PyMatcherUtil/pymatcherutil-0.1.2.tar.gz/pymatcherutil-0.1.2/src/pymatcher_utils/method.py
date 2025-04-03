from typing import Any, Sequence

from pymatcher_utils.matcher import Matcher


class NotCalled(Matcher):
    """Represent a matcher to verify that a mock object was not called."""

    def __eq__(self, other: Any) -> bool:
        """Determine equality by ensuring the `other` MagicMock has not been called.

        :param other: A MagicMock instance to check against
        :return: True if `other` has not been called, otherwise comparison cannot be
            completed as intended in this context.

        """
        other.assert_not_called()
        return True


class Called(Matcher):
    """Represent a matcher for verifying call patterns on mocked objects.

    The Called class is used to assert that a MagicMock object has been called with
    specific arguments a certain number of times. It provides comparison capabilities to
    check if the simulated calls match the expected ones.

    :type calls: list

    """

    calls: Sequence[tuple[Any]]
    """The expected series of calls to validate against the mocked object."""

    def __init__(self, *calls: tuple) -> None:
        """Initialize the object with a list of calls or multiple call arguments.

        Constructs an instance where the calls attribute is a list of call objects. If a
        single list of calls is provided as the argument, it is used directly as the
        list of calls. Otherwise, all provided individual call arguments are collected
        into a list.

        :param calls: A single list of call objects or multiple call objects. If a
            single list is passed, it will be directly assigned to the calls attribute.
            Otherwise, each call object is gathered into a list.

        """
        if len(calls) == 1 and isinstance(calls[0], list):
            self.calls = calls[0]
        else:
            self.calls = list(calls)

    def __eq__(self, other: Any) -> bool:
        """Compare the number of calls and the sequence of calls.

        This method verifies that the call count on the `other` MagicMock instance
        matches the expected number of calls recorded in `self.calls`. It also checks
        that the sequence of calls made on the `other` instance matches the sequence in
        `self.calls`.

        :param other: Another MagicMock instance to compare against.
        :return: True if the call count and sequence of calls match.
        :raises AssertionError: If the call count or call sequences do not match.

        """
        assert other.call_count == len(
            self.calls
        ), f"expected {len(self.calls)} calls, got {other.call_count}"
        other.assert_has_calls(self.calls)
        return True
