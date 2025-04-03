from typing import Any, Union

from pymatcher_utils.matcher import Matcher, check_value


def set_properties(
    obj: Any, values: Union[dict[str, Any], list[tuple[str, Any]]]
) -> None:
    """Set properties on an object using a dictionary or list of tuples.

    This function assigns the specified attributes to the given object based on the
    provided dictionary or list of tuples. If a dictionary is passed, keys represent
    attribute names and values are the attributes to be set. If a list is passed, each
    tuple should contain the attribute name as the first element and the value to be set
    as the second element.

    :param obj: the target object on which attributes are to be set
    :param values: a dictionary or list of tuples containing attribute names and their
        corresponding values
    :return: None

    """
    if isinstance(values, dict):
        for key, value in values.items():
            setattr(obj, key, value)
    elif isinstance(values, list):
        for key, value in values:
            setattr(obj, key, value)


def check_properties(obj: Any, expected: dict[str, Any]) -> None:
    """Verify that an object has the expected properties.

    This function takes an object and a dictionary of expected attributes and values. It
    checks if the object possesses each of the specified attributes, and confirms that
    the corresponding attribute values match the expected values as defined in the
    dictionary.

    :param obj: The object whose properties are to be verified.
    :param expected: A dictionary where keys are attribute names and values are the
        expected values of those attributes.
    :return: None

    """
    for key, value in expected.items():
        assert hasattr(obj, key), f"{key} not found in {obj}"
        check_value(getattr(obj, key), value)


class PropEq(Matcher):
    """Check properties for equality within an object.

    This class is designed to compare expected property values to the actual properties
    present within an object. It can be initialized with either a dictionary of expected
    properties or with keyword arguments representing those properties. The class
    primarily exists to determine if another object's attributes meet the expected
    criteria by providing a mechanism to evaluate equality.

    """

    expected: dict[Any, Any]
    """A dictionary of expected property names and their values."""

    def __init__(self, *args, **expected) -> None:
        """Initialize the CheckParameters instance with the provided arguments.

        This constructor can accept either a single dictionary or a variable number of
        keyword arguments. If a single dictionary is provided as positional argument, it
        will be used as the expected parameters. If keyword arguments are provided, they
        will be used to construct the expected parameter dictionary. This allows for
        flexible initialization of the instance with expected parameter values.

        :param args: Positional arguments which can either be a single dictionary
            containing expected parameters or can be ignored if using keyword arguments.
        :param expected: Expected keyword arguments which are combined into a dictionary
            to set as the expected parameters.

        """
        if len(args) == 1 and isinstance(args[0], dict):
            self.expected = args[0]
        else:
            self.expected = dict(expected)

    def __eq__(self, other: Any) -> bool:
        """Compare the current object with another for equality.

        :param other: The object to compare against. It must have attributes
            corresponding to keys in the `expected` dictionary.
        :return: True if all attributes specified in `expected` match the respective
            attributes in `other`; otherwise, False.

        """
        # check if property is assigned correctly.
        check_properties(other, self.expected)
        return True
