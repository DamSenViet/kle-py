from decimal import Decimal
from collections import OrderedDict
from typing import (
    Union,
    TypeVar,
    Tuple,
    List,
    Dict,
)

from .key import Key


def key_sort_criteria(key: Key) -> Tuple[
    Decimal,
    Decimal,
    Decimal,
    Decimal,
    Decimal,
]:
    """A helper to sort keys into the KLE order before serialization.

    :param key: the key to compare
    :type key: Key
    :return: the multidimensional ordering for comparison
    :rtype: Tuple[ Decimal, Decimal, Decimal, Decimal, Decimal, ]
    """
    return (
        (key.rotation_angle + 360) % 360,
        key.rotation_x,
        key.rotation_y,
        key.y,
        key.x,
    )


label_map = [
    [0, 6, 2, 8, 9, 11, 3, 5, 1, 4, 7, 10],  # 0 = no centering
    [1, 7, -1, -1, 9, 11, 4, -1, -1, -1, -1, 10],  # 1 = center x
    [3, -1, 5, -1, 9, 11, -1, -1, 4, -1, -1, 10],  # 2 = center y
    [4, -1, -1, -1, 9, 11, -1, -1, -1, -1, -1, 10],  # 3 = center x & y
    [0, 6, 2, 8, 10, -1, 3, 5, 1, 4, 7, -1],  # 4 = center front (default)
    [1, 7, -1, -1, 10, -1, 4, -1, -1, -1, -1, -1],  # 5 = center front & x
    [3, -1, 5, -1, 10, -1, -1, -1, 4, -1, -1, -1],  # 6 = center front & y
    # 7 = center front & x & y
    [4, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1],
]


disallowed_alignnment_for_labels = [
    [1, 2, 3, 5, 6, 7],  # 0
    [2, 3, 6, 7],  # 1
    [1, 2, 3, 5, 6, 7],  # 2
    [1, 3, 5, 7],  # 3
    [],  # 4
    [1, 3, 5, 7],  # 5
    [1, 2, 3, 5, 6, 7],  # 6
    [2, 3, 6, 7],  # 7
    [1, 2, 3, 5, 6, 7],  # 8
    [4, 5, 6, 7],  # 9
    [],  # 10
    [4, 5, 6, 7]  # 11
]

T = TypeVar('T')


def serialize_prop(
    props: OrderedDict,
    name: str,
    val: T,
    default_val: T
) -> T:
    """Sets a prop using the name if values are different.

    :param props: the props
    :type props: OrderedDict
    :param name: the property name
    :type name: str
    :param val: the value
    :type val: T
    :param default_val: the value to compare against
    :type default_val: T
    :return: the value
    :rtype: T
    """
    if val != default_val:
        if type(val) is Decimal:
            props[name] = float(val)
        else:
            props[name] = val
    return val


def reorder_labels(key: Key, current: Key) -> Dict:
    """Gets an efficient version of the  key's labels, text colors, text sizes.

    :param key: the key to compute the reorder of
    :type key: Key
    :param current: the current key to compare to
    :type current: Key
    :return: a return dict with reordered version of props stored
    :rtype: Dict
    """
    align = [7, 5, 6, 4, 3, 1, 2, 0]

    # remove impossible flag combinations
    for i in range(len(key.text_labels)):
        if bool(key.text_labels[i]):
            align = list(
                filter(lambda n: n not in disallowed_alignnment_for_labels[i], align))

    # generate label array in correct order
    ret = {
        "align": align[0],
        "labels": ["" for i in range(12)],
        "text_color": ["" for i in range(12)],
        "text_size": [None for i in range(12)],
    }
    for i in range(12):
        if i not in label_map[ret["align"]]:
            continue
        ndx = label_map[ret["align"]].index(i)
        if ndx >= 0:
            if bool(key.text_labels[i]):
                ret["labels"][ndx] = key.text_labels[i]
            if bool(key.text_color[i]):
                ret["text_color"][ndx] = key.text_color[i]
            if bool(key.text_size[i]):
                ret["text_size"][ndx] = key.text_size[i]

    # clean up
    for i in range(len(ret["text_size"])):
        if not bool(ret["labels"][i]):
            ret["text_size"][i] = current.text_size[i]
        if not bool(ret["text_size"][i]) or ret["text_size"] == key.default_text_size:
            ret["text_size"][i] = 0
    return ret


def reorder_labels_in(items: List, align: int) -> List:
    """Realigns the labels based on align setting.

    :param items: The items to be reordered.
    :type items: list
    :param align: The alignment option. 0-7
    :type align: int
    :return: The reordered items.
    :rtype: list
    """
    ret = [None for i in range(12)]
    for i, item in enumerate(items):
        if item:
            ret[label_map[align][i]] = item
    return ret


def compare_text_sizes(
    text_sizes: Union[int, List[int]],
    ordered_text_sizes: List[Union[int, float, None]],
    ordered_labels: List[Union[str, None]]
) -> bool:
    """Determines whether text sizes and ordered version are equal.

    :param text_sizes: the text sizes to compare
    :type text_sizes: Union[int, List[int]]
    :param ordered_text_sizes: the ordered text sizes
    :type ordered_text_sizes: List[Union[int, float, None]]
    :param ordered_labels: the ordered labels
    :type ordered_labels: List[Union[str, None]]
    :return: whether text sizes are equal
    :rtype: bool
    """
    if (
        type(text_sizes) is int or
        type(text_sizes) is float
    ):
        current = [text_sizes] + [None for i in range(11)]
    for i in range(12):
        if (
            ordered_labels[i] is not None and
            (
                (bool(text_sizes[i]) != bool(ordered_text_sizes[i])) or
                (
                    bool(text_sizes[i]) and
                    text_sizes[i] != ordered_text_sizes[i]
                )
            )
        ):
            return False
    return True
