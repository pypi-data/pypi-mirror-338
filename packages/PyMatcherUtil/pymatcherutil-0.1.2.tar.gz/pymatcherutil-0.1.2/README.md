# PyMatcherUtil 

[![python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org)
[![codecov](https://codecov.io/gh/anozaki/PyMatcherUtil/branch/main/graph/badge.svg?token=YOUR_TOKEN)](https://codecov.io/gh/anozaki/PyMatcherUtil)

## Introduction

PyMatcherUtil — a tailored library of custom matchers designed to extend the
capabilities of Python's `unittest.mock` for more comprehensive and expressive testing
assertions. As testing becomes an integral part of software development, having 
sophisticated, reusable, and expressive testing utilities can significantly enhance the
quality of your codebase. unittest.mock` for more comprehensive and expressive testing
assertions.

## Installation

You can install PyMatcherUtil using the following `pip` command:

```bash
python -m pip install https://github.com/anozaki/PyMatcherUtil/tarball/master
```

## Key Features

- **Custom Matchers**: Gain access to a variety of pre-built matchers such as `All`,
  `Eq`, `NotEq`, `Called`, `NotCalled`, `All`, `IsInstance`, `PropEq`, `DictEq`, 
  and `ListEq` to validate different aspects of your objects and mocks..
- **Expressive Assertions**: Write expressive and self-explanatory tests that improve 
  readability and maintainability.
- **Integration with Existing Frameworks**: Seamlessly integrate with standard testing 
  frameworks such as `unittest` and `pytest` to leverage familiar testing ecosystems.
- **Reusable Testing Utilities**: Centralize your testing logic and reuse it across
  multiple projects, promoting DRY (Don't Repeat Yourself) principles.

## Examples

### Basic Example

This example demonstrates the use of custom matchers from the `pymatcher_utils` library
to perform advanced assertions in unit tests. The function `sum_value`
takes two numbers, adds them, and returns the floor of the sum as an integer. The test
`test_sum_value` uses the `pytest.mark.parametrize` decorator to define several test
cases. It showcases the use of matchers `All`, `Eq`, and `IsInstance` from the library
to check that the results meet specific conditions, such as being equal to a specific
value and being an instance of a given type.

```python
import math
import pytest
from pymatcher_utils import All, Eq, IsInstance, check_value

def sum_value(a: int | float, b: int | float) -> int:
  return int(math.floor(a + b))

@pytest.mark.paramertrize("a_value, b_value, expect", [
  # normal without lib
  (1, 5, 6),
  
  # check value is equal
  # check returned instance is int
  (5, 7, All(Eq(12), IsInstance(int))),
  
  # check result that is < <n>.5 to make sure it is floored
  # check result is int
  (5.1, 7.1, All(Eq(12), IsInstance(int))),
  
  # check result that is > <n>.5 to make sure it is floored
  # check result is int
  (5.5, 7.1, All(Eq(12), IsInstance(int))),
  
  # check float and int input
  #   check output result is 12
  #   make sure we got back int
  (5.1, 7, All(Eq(12), IsInstance(int))),
])
def test_sum_value(a_value, b_value, expect):
    result = sum_value(a_value, b_value)
    check_value(result, expect)
```


### Testing Class

This example further explores the application of custom matchers to test a class,
`SumValue`, which encapsulates the addition operation. The test `test_sum_value` also
uses `pytest.mark.parametrize` for defining test cases involving object properties.
The `PropEq` matcher is used to assert that the properties of `SumValue` instances meet
the expected values. The example includes dynamic property updates using
`set_properties` and demonstrates how to verify the result using a combination of
property matchers and type matchers, ensuring the result is correctly calculated and its
type is verified.

```python
import math

import pytest

from pymatcher_utils import set_properties, PropEq, IsInstance, All, check_value, Eq


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
            # PropEq can be a dict or variable list
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

    check_value(target, expect)

```


### Other Examples

See [example folder](test/example) for additional usage example.

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
