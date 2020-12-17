from typing import (
    TypeVar,
    Any,
    Union,
    Callable,
    List,
    Dict,
)
from contextlib import ContextDecorator
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
from mpmath import mp, MPContext
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


kle_dps: int = 15
"""The mpmath dps to use to maintain the identical KLE precision.

JSON number format is double-precision (binary64) IEEE-754.
mp.dps = 15 when mp.prec = 53 is IEEE-754 double-precision.

https://mpmath.org/doc/current/technical.html#double-precision-emulation
"""


# decorator factory
class like_kle(ContextDecorator):
    """Temporarily modifies the mp context to match KLE computation precision."""

    def __init__(self, dps: int = kle_dps) -> None:
        """We gottem son

        :param dps: [description], defaults to kle_dps
        :type dps: int, optional
        """
        self.target_dps = dps
        self.source_dps = None

    def __enter__(self) -> MPContext:
        """Modifies the mp context to target settings upon entry.

        :return: the global mp context
        :rtype: MPContext
        """
        self.source_dps = mp.dps
        mp.dps = self.target_dps
        return mp

    def __exit__(
        self,
        *exc,
    ) -> bool:
        """Resets the mp context to before changes upon exit."""
        mp.dps = self.source_dps
        return False


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
