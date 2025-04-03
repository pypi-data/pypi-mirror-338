from typing import Any

from pymatcher_utils.matcher import Matcher, check_value


class ArrayEq(Matcher):
    """Create a matcher for comparing array-like structures."""

    expected: list[Any]
    """The list of expected values to compare against."""

    def __init__(self, *args) -> None:
        """Initialize the object with a list of expected items.

        If a single list argument is provided, use it as the internal list of expected
        items; otherwise, use all provided arguments to form the list.

        :param args: A single list or multiple individual arguments to be used to
            initialize the expected items.

        """
        if len(args) == 1 and isinstance(args[0], list):
            self.expected = args[0]
        else:
            self.expected = list(args)

    def __eq__(self, other: Any) -> bool:
        """Compare this object with another to check for equality.

        This function ensures that the current object and the `other` object have the
        same length and that their elements match according to the `check_value`
        function. If any mismatch occurs, an AssertionError is raised. This method
        returns `True` if both objects are equal.

        :param other: The object to compare with.
        :return: Returns `True` if both objects are equal.
        :raises AssertionError: If the lengths of objects differ or any element does not
            match.

        """
        assert len(self.expected) == len(
            other
        ), f"Length mismatch: {len(self.expected)} != {len(other)}"

        for value, other_value in zip(self.expected, other):
            check_value(value, other_value)

        return True
