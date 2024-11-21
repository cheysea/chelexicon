# Type annotation for basic data types
def greet(name: str) -> str:
    return f"Hello, {name}"


# Type annotation for a function that returns None
def print_message(message: str) -> None:
    print(message)


# Type annotation for list
def process_items(items: list[int]) -> list[int]:
    return [item * 2 for item in items]


# Type annotation for optional values
from typing import Optional


def find_item(items: list[int], value: int) -> Optional[int]:
    try:
        return items.index(value)
    except ValueError:
        return None


# Type annotation for dictionaries
def count_frequencies(items: list[str]) -> dict[str, int]:
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies


# Type annotation for tuples
def get_user_info() -> tuple[str, int]:
    return "Alice", 25


# Type annotation for sets
def find_unique_numbers(numbers: list[int]) -> set[int]:
    return set(numbers)


# Type annotation for union types
from typing import Union


def parse_value(value: Union[str, int]) -> int:
    if isinstance(value, int):
        return value
    elif value.isdigit():
        return int(value)
    else:
        raise ValueError("Invalid input")


# Type annotation for callable objects (like functions)
from typing import Callable


def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


# Type annotation for any type
from typing import Any


def handle_anything(value: Any) -> str:
    return f"Handled value: {value}"


# Type annotation for generic types
from typing import TypeVar, Generic

T = TypeVar('T')


class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value







from typing import List, Optional, Dict, Tuple, Set, Union, Callable, Any, TypeVar, Generic

T = TypeVar('T')


def greet(name: str) -> str:
    """
    Greet the user by name.

    :param name: The name of the user
    :type name: str
    :return: A greeting message
    :rtype: str
    """
    return f"Hello, {name}"


def print_message(message: str) -> None:
    """
    Print a message.

    :param message: The message to print
    :type message: str
    """
    print(message)


def process_items(items: List[int]) -> List[int]:
    """
    Process a list of integers.

    :param items: A list of integers
    :type items: list[int]
    :return: A list of processed integers
    :rtype: list[int]
    """
    return [item * 2 for item in items]


def find_item(items: List[int], value: int) -> Optional[int]:
    """
    Find an item in a list.

    :param items: A list of integers
    :type items: list[int]
    :param value: The value to find
    :type value: int
    :return: The index of the item if found, otherwise None
    :rtype: Optional[int]
    """
    try:
        return items.index(value)
    except ValueError:
        return None


def count_frequencies(items: List[str]) -> Dict[str, int]:
    """
    Count the frequency of items in a list.

    :param items: A list of strings
    :type items: list[str]
    :return: A dictionary with item frequencies
    :rtype: dict[str, int]
    """
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies


def get_user_info() -> Tuple[str, int]:
    """
    Get user information.

    :return: A tuple containing the user's name and age
    :rtype: tuple[str, int]
    """
    return "Alice", 25


def find_unique_numbers(numbers: List[int]) -> Set[int]:
    """
    Find unique numbers in a list.

    :param numbers: A list of integers
    :type numbers: list[int]
    :return: A set of unique integers
    :rtype: set[int]
    """
    return set(numbers)


def parse_value(value: Union[str, int]) -> int:
    """
    Parse a value into an integer.

    :param value: The value to parse
    :type value: Union[str, int]
    :return: The parsed integer
    :rtype: int
    :raises ValueError: If the input is invalid
    """
    if isinstance(value, int):
        return value
    elif value.isdigit():
        return int(value)
    else:
        raise ValueError("Invalid input")


def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    """
    Execute a function with two integer arguments.

    :param func: The function to execute
    :type func: Callable[[int, int], int]
    :param a: The first integer argument
    :type a: int
    :param b: The second integer argument
    :type b: int
    :return: The result of the function
    :rtype: int
    """
    return func(a, b)


def handle_anything(value: Any) -> str:
    """
    Handle any type of value.

    :param value: The value to handle
    :type value: Any
    :return: A string representation of the handled value
    :rtype: str
    """
    return f"Handled value: {value}"


class Container(Generic[T]):
    """
    A container for a generic value.

    :param value: The value to store
    :type value: T
    """

    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        """
        Get the value from the container.

        :return: The stored value
        :rtype: T
        """
        return self.value
