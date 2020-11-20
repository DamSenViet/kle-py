from decimal import (
    Decimal,
    getcontext
)
from collections import OrderedDict
from typing import (
    Any,
    Union,
    TypeVar,
    Tuple,
    List,
    Dict,
)

from .key import Key
from .metadata import Metadata

getcontext().prec = 64


label_map = [
    # -1 indicates not used
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


def undo_align(items: List, align: int, default_val: Any) -> List:
    """Removes the alignment on the aligned items.

    :param items: The items to be reordered.
    :type items: List
    :param align: The alignment option. 0-7
    :type align: int
    :return: The reordered items.
    :rtype: list
    """
    ret = [default_val for i in range(12)]
    for i, item in enumerate(items):
        ret[label_map[align][i]] = item
    return ret


def compare_text_sizes(
    text_sizes: Union[int, List[int]],
    ordered_text_sizes: List[Union[int, float, None]],
    ordered_labels: List[str],
) -> bool:
    """Determines whether text sizes and ordered version are equal.

    :param text_sizes: the text sizes to compare
    :type text_sizes: Union[int, List[int]]
    :param ordered_text_sizes: the ordered text sizes
    :type ordered_text_sizes: List[Union[int, float, None]]
    :param ordered_labels: the ordered labels
    :type ordered_labels: List[str]
    :return: whether text sizes are equal
    :rtype: bool
    """
    if (
        type(text_sizes) is int or
        type(text_sizes) is float
    ):
        text_sizes = [text_sizes] + [None for i in range(11)]
    for i in range(12):
        if (
            bool(ordered_labels[i]) and
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


def playback_metadata_changes(metadata: Metadata, metadata_changes: Dict) -> None:
    """Playback the changes into the metadata.

    :param metadata: the metadata
    :type metadata: Metadata
    :param metadata_changes: the changes
    :type metadata_changes: Dict
    :return: the metadata
    :rtype: Metadata
    """
    if "author" in metadata_changes:
        metadata.author = metadata_changes["author"]
    if "backcolor" in metadata_changes:
        metadata.background_color = metadata_changes["backcolor"]
    if "background" in metadata_changes:
        if "name" in metadata_changes["background"]:
            metadata.background.name = metadata_changes["background"]["name"]
        if "style" in metadata_changes["background"]:
            metadata.background.style = metadata_changes["background"]["style"]
    if "name" in metadata_changes:
        metadata.name = metadata_changes["name"]
    if "notes" in metadata_changes:
        metadata.notes = metadata_changes["notes"]
    if "radii" in metadata_changes:
        metadata.radii = metadata_changes["radii"]
    if "switchMount" in metadata_changes:
        metadata.switch_mount = metadata_changes["switchMount"]
    if "switchBrand" in metadata_changes:
        metadata.switch_brand = metadata_changes["switchBrand"]
    if "switchType" in metadata_changes:
        metadata.switch_type = metadata_changes["switchType"]
    if "css" in metadata_changes:
        metadata.css = metadata_changes["css"]
    if "pcb" in metadata_changes:
        metadata.pcb = metadata_changes["pcb"]
    if "plate" in metadata_changes:
        metadata.plate = metadata_changes["plate"]


def playback_key_changes(
    key: Key,
    key_changes: Dict,
    align: int,
    cluster_rotation_x: Decimal,
    cluster_rotation_y: Decimal,
) -> Tuple[int, Decimal, Decimal]:
    """Playback the changes into the key.

    :param key: the recording key
    :type key: Key
    :param key_changes: the changes
    :type key_changes: Dict
    :param align: the tracked text alignment
    :type align: int
    :param cluster_rotation_x: the tracked rotation origin x
    :type cluster_rotation_x: Decimal
    :param cluster_rotation_y: the tracked rotation origin y
    :type cluster_rotation_y: Decimal
    :return: align, cluster_rotation_x, cluster_rotation_y
    :rtype: Tuple[int, Decimal, Decimal]
    """
    if "r" in key_changes:
        key.rotation_angle = Decimal(key_changes["r"])
    if "rx" in key_changes:
        key.rotation_x = Decimal(key_changes["rx"])
        cluster_rotation_x = Decimal(key_changes["rx"])
        key.x = cluster_rotation_x
        key.y = cluster_rotation_y
    if "ry" in key_changes:
        key.rotation_y = Decimal(key_changes["ry"])
        cluster_rotation_y = Decimal(key_changes["ry"])
        key.x = cluster_rotation_x
        key.y = cluster_rotation_y
    if "a" in key_changes:
        align = key_changes["a"]
    if "f" in key_changes:
        key.default_text_size = key_changes["f"]
        key.text_sizes = [None for i in range(12)]
    if "f2" in key_changes:
        for i in range(1, 12):
            key.text_sizes[i] = key_changes["f2"]
    if "fa" in key_changes:
        key.text_sizes = key_changes["fa"]
    if "p" in key_changes:
        key.profile = key_changes["p"]
    if "c" in key_changes:
        key.color = key_changes["c"]
    if "t" in key_changes:
        text_colors = key_changes["t"].split("\n")
        if text_colors[0] != "":
            key.default_text_color = text_colors[0]
        key.text_colors = undo_align(text_colors, align, None)
    if "x" in key_changes:
        key.x += Decimal(key_changes["x"])
    if "y" in key_changes:
        key.y += Decimal(key_changes["y"])
    if "w" in key_changes:
        key.width = Decimal(key_changes["w"])
        key.width2 = Decimal(key_changes["w"])
    if "h" in key_changes:
        key.height = Decimal(key_changes["h"])
        key.height2 = Decimal(key_changes["h"])
    if "x2" in key_changes:
        key.x2 = Decimal(key_changes["x2"])
    if "y2" in key_changes:
        key.y2 = Decimal(key_changes["y2"])
    if "w2" in key_changes:
        key.width2 = Decimal(key_changes["w2"])
    if "h2" in key_changes:
        key.height2 = Decimal(key_changes["h2"])
    if "n" in key_changes:
        key.nub = key_changes["n"]
    if "l" in key_changes:
        key.stepped = key_changes["l"]
    if "d" in key_changes:
        key.decal = key_changes["d"]
    if "g" in key_changes:
        key.ghost = key_changes["g"]
    if "sm" in key_changes:
        key.switch_mount = key_changes["sm"]
    if "sb" in key_changes:
        key.switch_brand = key_changes["sb"]
    if "st" in key_changes:
        key.switch_type = key_changes["st"]
    return (
        align,
        cluster_rotation_x,
        cluster_rotation_y,
    )


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


def record_change(
    changes: OrderedDict,
    name: str,
    val: T,
    default_val: T
) -> T:
    """Registers the change if value is not equal to default.

    :param changes: the existing changes
    :type changes: OrderedDict
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
            # determine if you can use an in there
            if val % Decimal(1.0) == Decimal(0.0):
                changes[name] = int(val)
            else:
                changes[name] = float(val)
        else:
            changes[name] = val
    return val


def reduced_text_sizes(text_sizes: List[Union[int, float, None]]):
    """Turns Nones into 0 and removes trailing zeroes from the text sizes.

    :param arr: [description]
    :type arr: List[Union[int, float]]
    :return: [description]
    :rtype: [type]
    """
    text_sizes = list(map(
        lambda text_size: 0 if text_size is None else text_size,
        text_sizes,
    ))
    while len(text_sizes) > 0 and text_sizes[-1] == 0:
        text_sizes.pop()
    return text_sizes


def reorder_labels(key: Key, current: Key) -> Dict:
    """More space efficient text labels, text colors, text sizes.

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
        "text_color": [None for i in range(12)],
        "text_size": [None for i in range(12)],
    }
    for i in range(12):
        if i not in label_map[ret["align"]]:
            continue
        ndx = label_map[ret["align"]].index(i)
        if ndx >= 0:
            if bool(key.text_labels[i]):
                ret["labels"][ndx] = key.text_labels[i]
            if bool(key.text_colors[i]):
                ret["text_color"][ndx] = key.text_colors[i]
            if bool(key.text_sizes[i]):
                ret["text_size"][ndx] = key.text_sizes[i]
    # clean up
    for i in range(len(reduced_text_sizes(ret["text_size"]))):
        if not ret["labels"][i]:
            ret["text_size"][i] = current.text_sizes[i]

        if not bool(ret["text_size"][i]) or ret["text_size"] == key.default_text_size:
            ret["text_size"][i] = 0
    return ret
