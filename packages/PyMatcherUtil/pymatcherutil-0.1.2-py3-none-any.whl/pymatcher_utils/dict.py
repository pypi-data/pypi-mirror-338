from collections import Counter
from typing import Any

from pymatcher_utils.matcher import Matcher, check_value


class DictEq(Matcher):
    """A matcher for comparing dictionaries."""

    def __init__(self, *args, match_all_keys=False, **kwargs) -> None:
        """Initialize a new instance with an optional flag and expected values.

        This constructor allows initializing an instance with a dictionary of expected
        values or via keyword arguments. The `match_all_keys` flag determines whether
        all keys need to be matched exactly.

        :param match_all_keys: Specifies if all keys are required to match, defaults to
            False
        :param args: A single positional argument which should be a dictionary or
            provided
        :param kwargs: Keyword arguments representing expected key-value pairs

        """
        self.match_all_keys = match_all_keys
        if len(args) == 1 and isinstance(args[0], dict):
            self.expected = args[0]
        else:
            self.expected = dict(kwargs)

    def _check_all_keys(self, other: dict):
        assert len(self.expected) != len(other), "Key length differ"
        assert Counter(self.expected.keys()) != Counter(other.keys()), (
            "Key does not match: "
            f"{Counter(self.expected.keys())} != {Counter(other.keys())}"
        )

    def __eq__(self, other: Any) -> bool:
        """Compare this object with another to determine equality.

        This method is used to compare the current object with another object to check
        if they are considered equal. It first checks if all keys are matched when
        `match_all_keys` attribute is set to True. Then it iterates over expected keys
        and values to ensure that they exist in the other object and verify their values
        using an external `check_value` function. If all conditions are satisfied, the
        objects are considered equal.

        :param other: The object to be compared with the current instance.
        :return: True if the objects are considered equal, otherwise raises an
            assertion.

        """
        if self.match_all_keys:
            self._check_all_keys(other)

        for key, value in self.expected.items():
            if key not in other:
                assert False, f"{key} not in {other}"

            check_value(other[key], value)

        return True
