import math

import pytest

from pymatcher_utils import set_properties, PropEq, IsInstance, All, check_value, Eq, \
    check_properties


class SumValue:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def sum(self) -> int:
        self.result = int(math.floor(self.a + self.b))
        return self.result


@pytest.mark.parametrize(
    "value_a, value_b, update, expect",
    [
        (1, 2, None, {"a": 1, "b": 2, "result": 3}),
        (1.2, 3.1, None, PropEq({"a": 1.2, "b": 3.1, "result": 4})),
        (1.2, 3.4, None, PropEq({"a": 1.2, "b": 3.4, "result": 4})),
        (
            1.2,
            3.4,
            {"b": 4.4},

            # make sure result state of the class has the specified values
            PropEq(
                a=1.2,
                b=4.4,

                # checking result using matchers
                result=All(
                    Eq(5),
                    IsInstance(int),
                ),
            ),
        ),
    ],
)
def test_sum_value(value_a, value_b, update, expect):
    target = SumValue(value_a, value_b)
    if update is not None:
        set_properties(target, update)
    target.sum()

    if isinstance(expect, dict):
        check_properties(target, expect)
    else:
        check_value(target, expect)
