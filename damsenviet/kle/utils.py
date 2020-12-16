from typing import (
    TypeVar,
    Any,
    Union,
    Callable,
    List,
    Dict,
)
from functools import wraps
from tinycss2 import (
    parse_stylesheet,
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
from mpmath import mp
from tinycss2.parser import parse_one_declaration
from typeguard import typechecked
from .exceptions import IllegalValueException

__all__ = [""]


T = TypeVar("T")
S = TypeVar("S")


def autorepr(self: Any, attributes: Dict[str, Any]):
    key_eq_val_strs: List[str] = []
    for key, value in attributes.items():
        key_eq_val_strs.append(f"{key}={repr(value)}")
    serial: str = ", ".join(key_eq_val_strs)
    return f"{self.__class__.__name__}({serial})"


# JSON numbers is IEEE-754 (double precision)
# https://mpmath.org/doc/current/technical.html#double-precision-emulation
# mp.dps = 15 when mp.prec = 53
kle_precision = 15


@typechecked
def with_precision(precision: int):
    """Temporarily modifies the precision of mpmath.

    :param precision: the mpf precision
    :type precision: int
    :return: wrapped function
    :rtype: Callable
    """

    def decorator(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            # mp.dps is decimal significant places
            # mp.prec is the number of precision bits
            old_precision = mp.dps
            mp.dps = precision
            result = function(*args, **kwargs)
            mp.dps = old_precision
            return result

        return wrapped

    return decorator


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
