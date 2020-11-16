from decimal import Decimal
from collections import OrderedDict
from typing import Any


def serialize_prop(
    props: OrderedDict,
    name: str,
    val: Any,
    default_val: Any
) -> Any:
    """Adds the name field to the props collection if value is not the same
    as the default value. Since KLE uses a specify differences only format.
    """
    if val != default_val:
        if type(val) is Decimal:
            props[name] = float(val)
        else:
            props[name] = val
    return val
