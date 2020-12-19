from typing import (
    TypeVar,
    Any,
    Union,
    Callable,
    List,
    Dict,
)
from tinycss2 import (
    parse_stylesheet,
    parse_one_declaration,
    parse_component_value_list,
)
from tinycss2.color3 import parse_color
from tinycss2.ast import (
    AtRule,
    QualifiedRule,
    Comment,
    WhitespaceToken,
    ParseError,
)
from .exceptions import IllegalValueException

__all__ = ["kle_dps", "like_kle"]


T = TypeVar("T")
S = TypeVar("S")


def autorepr(self: object, attributes: Dict[str, Any]) -> str:
    """A utility function to easily replace __repr__.

    :param self: any instance of a class
    :type self: object
    :param attributes: a mapping of name to values to display
    :type attributes: Dict[str, Any]
    :return: a string representing the object
    :rtype: str
    """
    key_eq_val_strs: List[str] = []
    for key, value in attributes.items():
        key_eq_val_strs.append(f"{key}={repr(value)}")
    serial: str = ", ".join(key_eq_val_strs)
    return f"{self.__class__.__name__}({serial})"


def expect(
    value_name: str,
    value: T,
    condition_description: str,
    condition: Callable[[T], bool],
) -> None:
    """Throws an exception if value does not meet the condition.

    :param value_name: value name
    :type value_name: str
    :param value: any value
    :type value: T
    :param condition_description: a description of condition
    :type condition_description: str
    :param condition: a callback that returns a boolean value
    :type condition: Callable[[T], bool]
    :return: None
    :rtype: None
    """
    message = f"expected {value_name} {repr(value)} to {condition_description}"
    if not condition(value):
        raise IllegalValueException(message, value)


def is_valid_css_stylesheet(css: str) -> bool:
    """Determines whether entire css stylesheet is valid.

    :param css: css stylesheet
    :type css: str
    """
    rules: List[
        Union[
            AtRule,
            QualifiedRule,
            Comment,
            WhitespaceToken,
            ParseError,
        ]
    ] = parse_stylesheet(
        css,
        skip_comments=True,
        skip_whitespace=True,
    )
    for rule in rules:
        if not isinstance(rule, ParseError):
            continue
        return False
    return True


def is_valid_css_color(css_color: str) -> bool:
    """Determines whether css color is valid.

    :param css_color: css color
    :type css_color: str
    :return: whether css color is valid
    :rtype: bool
    """
    return parse_color(css_color) is not None


def is_valid_css_component_value_list(css_component_value_list: str) -> bool:
    """Determines whether css component values are valid.

    :param css_component_value_list: css component value lists
    :type css_component_value_list: str
    :return: whether css component values is valid
    :rtype: bool
    """
    values = parse_component_value_list(css_component_value_list)
    for value in values:
        if not isinstance(value, ParseError):
            continue
        return False
    return True


def is_valid_css_declaration(css_declaration: str) -> bool:
    """Determines whether css declaration is valid.

    :param css_declaration: css declaration
    :type css_declaration: str
    :return: whether css declaration is valid
    :rtype: bool
    """
    return parse_one_declaration(css_declaration) is not None
