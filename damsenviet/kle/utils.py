from typing import (
    TypeVar,
    Any,
    List,
    Dict,
)

__all__ = []


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
