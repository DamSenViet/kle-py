from typing import (
    TypeVar,
    Any,
    List,
    Dict,
)

__all__ = ["json_dump_options"]


T = TypeVar("T")
S = TypeVar("S")


def _autorepr(self: object, attributes: Dict[str, Any]) -> str:
    """A utility function to easily replace __repr__.

    :param self: any instance of a class
    :param attributes: a mapping of name to values to display
    :return: a string representing the object
    """
    key_eq_val_strs: List[str] = []
    for key, value in attributes.items():
        key_eq_val_strs.append(f"{key}={repr(value)}")
    serial: str = ", ".join(key_eq_val_strs)
    return f"{self.__class__.__name__}({serial})"


json_dump_options = {
    "skipkeys": False,
    "ensure_ascii": True,
    "check_circular": True,
    "allow_nan": True,
    "cls": None,
    "indent": 2,
    "separators": None,
    "default": None,
    "sort_keys": False,
}
"""Kwargs to be spread into ``json.dump`` or ``json.dumps`` to match KLE JSON.

.. code-block:: python

    json.dumps(keyboard.to_json(), **json_dump_options)
"""