import decimal as dec
import collections as col

def serialize_prop(props: col.OrderedDict, name: str, val, defVal) -> dict:
    """Adds the name field to the props collection if value is not the same
    as the default value. Since KLE uses a specify differences only format.
    """
    if val != defVal:
        if type(val) is dec.Decimal:
            props[name] = float(val)
        else:
            props[name] = val
    return val