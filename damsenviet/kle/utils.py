from typing import TypeVar

__all__ = ["json_dump_options"]


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
"""
Kwargs to be spread into ``json.dump`` or ``json.dumps`` to match KLE JSON format.

.. code-block:: python

    json.dumps(keyboard.to_json(), **json_dump_options)
"""
