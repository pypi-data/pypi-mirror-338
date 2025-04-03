from abc import ABC
from typing import Any
from unittest.mock import ANY


def check_value(left: Any, right: Any) -> None:
    """Check if `left` matches `right` and assert equality according to type.

    :param left: The left-hand operand for the equality check.
    :param right: The right-hand operand, which may be a `Matcher`.

    """
    if isinstance(right, Matcher) or right is ANY:
        assert right == left, f"{left} != {right}"
    else:
        assert left == right, f"{left} != {right})"


class Matcher(ABC):
    """Base class for all matchers.

    Any class extending Matcher will have their matching prioritized.

    """


class All(Matcher):
    """Match all matchers in the list."""

    def __init__(self, *args):
        """Initialize MyClass with expected arguments.

        :param args: Variable length argument list storing expected arguments

        """
        self.expected = args

    def __eq__(self, other: Any):
        """Compare this instance to another for equality.

        Executes all expected matcher against 'other' and will raise an AssertionError
        if the match fails.

        :param other: The object to compare with this instance.
        :return: True if all expected items are equal to those in 'other'.

        """
        for exp in self.expected:
            assert exp == other

        return True


class Eq(Matcher):
    """Compare values for equality."""

    def __init__(self, value) -> None:
        """Initialize the class with a value.

        :param value: The value to initialize the instance with.
        :type value: Any

        """
        self.value = value

    def __eq__(self, other) -> bool:
        """Compare if two values are equal.

        :param other: The value to compare against.
        :return: True if values are equal, False otherwise.

        """
        check_value(self.value, other)
        return True


class NotEq(Matcher):
    """Compare values for inequality."""

    def __init__(self, value) -> None:
        """Initialize NotEq with an expected value.

        :param value: The value to be set as the internal attribute.

        """
        self.value = value

    def __eq__(self, other) -> bool:
        """Compare the current instance with another for equality.

        Will handle Matcher in special way by giving equality check priority.

        :param other: The object to compare with the current instance.
        :return: True if the comparison does not raise an assertion error

        """
        if isinstance(other, Matcher) or other is ANY:
            assert other != self.value, f"{self.value} == {other}"
        else:
            assert self.value != other, f"{self.value} == {other}"

        return True


class Is(Matcher):
    """Compare value for `is` equality."""

    def __init__(self, value) -> None:
        """Initialize is with an expected value.

        :param value: The value to be set as the internal attribute.

        """
        self.value = value

    def __eq__(self, other) -> bool:
        """Compare the current instance with another for `is` equality.

        Will handle Matcher in special way by giving equality check priority.

        :param other: The object to compare with the current instance.
        :return: True if the comparison does not raise an assertion error

        """
        if isinstance(other, Matcher) or other is ANY:
            assert other is self.value, f"{other} is not {self.value}"
        else:
            assert self.value is other, f"{other} is not {self.value}"

        return True


class IsNot(Matcher):
    """Compare value for `is not` equality."""

    def __init__(self, value) -> None:
        """Initialize is with an expected value.

        :param value: The value to be set as the internal attribute.

        """
        self.value = value

    def __eq__(self, other) -> bool:
        """Compare the current instance with another for `is not` equality.

        Will handle Matcher in special way by giving equality check priority.

        :param other: The object to compare with the current instance.
        :return: True if the comparison does not raise an assertion error

        """
        if isinstance(other, Matcher) or other is ANY:
            assert other is not self.value, f"{other} is {self.value}"
        else:
            assert self.value is not other, f"{other} is {self.value}"

        return True


class IsInstance(Matcher):
    """Check if an object is an instance of a given type."""

    def __init__(self, istype):
        """Initialize IsInstance with a type to check against.

        :param istype: The type to check against.

        """
        self.istype = istype

    def __eq__(self, other: Any):
        """Compare this instance with another for equality.

        :param other: The object to compare with for equality.
        :return: True if `other` is of the type `self.istype`, otherwise an
            AssertionError is raised.
        :rtype: bool

        """
        assert isinstance(other, self.istype), f"{other} is not {self.istype}"
        return True
