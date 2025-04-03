import math
from unittest.mock import MagicMock, call, ANY

import pytest

from pymatcher_utils import (
    PropEq,
    IsInstance,
    All,
    Eq,
    Called,
    set_properties,
    check_value, NotEq, NotCalled,
)



class AddService:
    def calculate(self, a, b):
        return int(math.floor(a + b))

    def not_called(self):
        pass


class Operation:
    def __init__(self, service: AddService):
        self.service = service

    def calculate(self, a, b):
        return self.service.calculate(a, b)

class SomeValue:
    def __init__(self):
        self.result = None

    def __eq__(self, other):
        # Example eq override
        return other == 1

class AlwaysFalse:
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

@pytest.mark.parametrize(
    "value_a, value_b, update, expect",
    [
        # example of test with no mock
        (1, 2, None, {"result": 3}),
        # example of test with calculate function mocked.
        (
            1,
            2,
            {"calculate": MagicMock(return_value=15)},
            {
                "result": 15,
                # example of property traversal for verification
                "operation": PropEq(
                    service=PropEq(
                        calculate=Called(
                            call(
                                All(Eq(1), IsInstance(int)),
                                2,
                            )
                        )
                    )
                ),
            },
        ),

        # example of test with calculate function mocked.
        (
            # this doesn't make any sense but as an example
            SomeValue(),
            2,
            {"calculate": MagicMock(return_value=15)},
            {
                # as an example, you can example ANY here.
                "result": ANY,

                # example of property traversal for verification
                "operation": PropEq(
                    service=PropEq(
                        calculate=Called(
                            call(
                                # all these should match.
                                All(1, Eq(1), NotEq(2), ANY, IsInstance(SomeValue)),
                                2,
                            )
                        )
                    )
                ),
            },
        ),

        (
                AlwaysFalse(),
                2,
                {"calculate": MagicMock(return_value=15), "not_called": MagicMock()},
                {
                    # example of property traversal for verification
                    "operation": PropEq(
                        service=PropEq(
                            calculate=Called(
                                call(
                                    # all these should match.
                                    All(ANY, Eq(ANY), NotEq(1), IsInstance(AlwaysFalse)),
                                    2,
                                )
                            ),
                            not_called=NotCalled()
                        )
                    ),
                },
        ),
    ],
)
def test_operation(value_a, value_b, update, expect):
    target = Operation(AddService())
    set_properties(target.service, update)
    result = target.calculate(value_a, value_b)

    if "result" in expect:
        check_value(result, expect["result"])

    if "operation" in expect:
        check_value(target, expect["operation"])
