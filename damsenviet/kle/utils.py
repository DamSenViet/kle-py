from copy import deepcopy
from decimal import (
    Decimal,
    getcontext,
)
from typing import (
    Any,
    Callable,
    Union,
    TypeVar,
    Tuple,
    List,
    Dict,
)
from typeguard import typechecked

from .metadata import Metadata
from .key import Key

T = TypeVar("T")
S = TypeVar("S")
getcontext().prec = 64

# fmt: off
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
# fmt: on


@typechecked
def unaligned(aligned_items: List, alignment: int, default_val: Any) -> List:
    """Returns the unaligned ordering of aligned items.

    :param items: The aligned_items to be unaligned.
    :type items: List
    :param align: The alignment option. 0-7
    :type align: int
    :return: The reordered items.
    :rtype: list
    """
    unaligned_items = [default_val for i in range(12)]
    for i, aligned_item in enumerate(aligned_items):
        unaligned_items[label_map[alignment][i]] = aligned_item
    return unaligned_items


@typechecked
def compare_text_sizes(
    text_sizes: Union[int, float, List[Union[int, float]]],
    aligned_text_sizes: List[Union[int, float]],
    aligned_text_labels: List[str],
) -> bool:
    """Determines whether text sizes and ordered version are equal.

    :param text_sizes: the text sizes to compare
    :type text_sizes: Union[int, List[int]]
    :param aligned_text_sizes: the ordered text sizes
    :type algined_text_sizes: List[Union[int, float]]
    :param aligned_text_labels: the ordered labels
    :type aligned_text_labels: List[str]
    :return: whether text sizes are equal
    :rtype: bool
    """
    if type(text_sizes) is int or type(text_sizes) is float:
        text_sizes = [text_sizes] + [0 for i in range(11)]
    for i in range(12):
        if aligned_text_labels[i] == "":
            continue

        if (
            # text size is non 0 and aligned text size is 0 or
            # text is 0 and aligned text size is non 0
            (bool(text_sizes[i]) != bool(aligned_text_sizes[i]))
            or (text_sizes[i] != 0 and text_sizes[i] != aligned_text_sizes[i])
        ):
            return False
    return True


@typechecked
def playback_metadata_changes(metadata: Metadata, metadata_changes: Dict) -> None:
    """Playback the changes into the metadata.

    :param metadata: metadata
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
        metadata.is_switches_pcb_mounted = metadata_changes["pcb"]
        metadata.include_switches_pcb_mounted = True
    if "plate" in metadata_changes:
        metadata.is_switches_plate_mounted = metadata_changes["plate"]
        metadata.include_switches_plate_mounted = True


@typechecked
def playback_key_changes(
    key: Key,
    key_changes: Dict,
    current_labels_color: List[str],
    current_labels_size: List[Union[int, float]],
    alignment: int,
    cluster_rotation_x: Decimal,
    cluster_rotation_y: Decimal,
) -> Tuple[List[str], List[Union[int, float]], int, Decimal, Decimal]:
    """Playback the changes into the key.

    :param key: the recording key
    :type key: Key
    :param key_changes: the changes
    :type key_changes: Dict
    :param current_labels_color: key's labels' color, default values set to ""
    :type current_labels_color: List[str]
    :param current_labels_size: key's labels' size, defaults values set to 0
    :type current_labels_size: List[Union[int, float]]
    :param alignment: the tracked text alignment
    :type alignment: int
    :param cluster_rotation_x: the tracked rotation origin x
    :type cluster_rotation_x: Decimal
    :param cluster_rotation_y: the tracked rotation origin y
    :type cluster_rotation_y: Decimal
    :return: current_labels_color, current_labels_size, align, cluster_rotation_x, cluster_rotation_y
    :rtype: Tuple[List[str], List[Union[int, float]], int, Decimal, Decimal]
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
        alignment = key_changes["a"]
    if "f" in key_changes:
        key.default_text_size = key_changes["f"]
        for i in range(len([size for size in current_labels_size])):
            current_labels_size[i] = 0
    if "f2" in key_changes:
        for i in range(1, 12):
            current_labels_size[i] = key_changes["f2"]
    if "fa" in key_changes:
        for i in range(len(key_changes["fa"])):
            current_labels_size[i] = key_changes["fa"][i]
        for i in range(len(key_changes["fa"]), 12):
            current_labels_size[i] = 0
    if "p" in key_changes:
        key.profile_and_row = key_changes["p"]
    if "c" in key_changes:
        key.color = key_changes["c"]
    if "t" in key_changes:
        labels_color = deepcopy(key_changes["t"]).split("\n")
        if labels_color[0] != "":
            key.default_text_color = labels_color[0]
        for i, color in enumerate(unaligned(labels_color, alignment, "")):
            current_labels_color[i] = color
    if "x" in key_changes:
        key.x = key.x + Decimal(key_changes["x"])
    if "y" in key_changes:
        key.y = key.y + Decimal(key_changes["y"])
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
        key.is_homing = key_changes["n"]
    if "l" in key_changes:
        key.is_stepped = key_changes["l"]
    if "d" in key_changes:
        key.is_decal = key_changes["d"]
    if "g" in key_changes:
        key.is_ghosted = key_changes["g"]
    if "sm" in key_changes:
        key.switch_mount = key_changes["sm"]
    if "sb" in key_changes:
        key.switch_brand = key_changes["sb"]
    if "st" in key_changes:
        key.switch_type = key_changes["st"]
    return (
        current_labels_color,
        current_labels_size,
        alignment,
        cluster_rotation_x,
        cluster_rotation_y,
    )


@typechecked
def key_sort_criteria(
    key: Key,
) -> Tuple[Decimal, Decimal, Decimal, Decimal, Decimal]:
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


@typechecked
def record_change(changes: Dict, name: str, val: T, default_val: S) -> T:
    """Registers the change if value is not equal to default.

    :param changes: the existing changes
    :type changes: Dict
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


@typechecked
def reduced_text_sizes(text_sizes: List[Union[int, float]]):
    """Returns a copy of text sizes with right zeroes stripped.

    :param arr: [description]
    :type arr: List[Union[int, float]]
    :return: [description]
    :rtype: [type]
    """
    text_sizes: List[Union[int, float]] = deepcopy(text_sizes)
    while len(text_sizes) > 0 and text_sizes[-1] == 0:
        text_sizes.pop()
    return text_sizes


@typechecked
def aligned_key_properties(
    key: Key,
    current_labels_size: List[Union[int, float]],
) -> Tuple[int, List[str], List[str], List[Union[int, float]]]:
    """More space efficient text labels, text colors, text sizes.

    :param key: the key to compute the reorder of
    :type key: Key
    :param current: the current key to compare to
    :type current: Key
    :return: a return dict with reordered version of props stored
    :rtype: Dict
    """
    # size and colors if match default changed to base values
    key_labels_size = [label.size for label in key.labels]
    key_labels_color = [label.color for label in key.labels]
    for i, label in enumerate(key.labels):
        if label.text == "":
            key_labels_color[i] = ""
            key_labels_size[i] = 0
        if label.color == key.default_text_color:
            key_labels_color[i] = ""
        if label.size == key.default_text_size:
            key_labels_size[i] = 0

    texts: List[str] = [label.text for label in key.labels]
    colors: List[str] = [color for color in key_labels_color]
    sizes: List[Union[int, float]] = [size for size in key_labels_size]
    alignments: List[int] = [7, 5, 6, 4, 3, 1, 2, 0]

    # remove impossible flag combinations
    for i in range(len(texts)):
        if texts[i] != "":
            try:
                for alignment in deepcopy(alignments):
                    if alignment in disallowed_alignnment_for_labels[i]:
                        alignments.remove(alignment)
            except ValueError:
                pass

    # generate label arrays in correct order
    alignment = alignments[0]
    aligned_text_labels = ["" for i in range(12)]
    aligned_text_color = ["" for i in range(12)]
    aligned_text_size = [0 for i in range(12)]
    for i in range(12):
        if i not in label_map[alignment]:
            continue
        ndx = label_map[alignment].index(i)
        if ndx >= 0:
            if texts[i] != "":
                aligned_text_labels[ndx] = texts[i]
            if colors[i] != "":
                aligned_text_color[ndx] = colors[i]
            if sizes[i] != 0:
                aligned_text_size[ndx] = sizes[i]
    # clean up
    for i in range(len(reduced_text_sizes(aligned_text_size))):
        if aligned_text_labels[i] == "":
            aligned_text_size[i] = current_labels_size[i]
        if aligned_text_size == key.default_text_size:
            aligned_text_size[i] = 0

    return (
        alignment,
        aligned_text_labels,
        aligned_text_color,
        aligned_text_size,
    )


class IllegalValueException(Exception):
    """Class for encountering illegal arguments."""

    def __init__(
        self,
        message: str,
    ):
        """Initializes an IllegalArgumentException.

        :param message: A message indicating an illegal argument.
        :type message: str
        """
        super().__init__(message)


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
    :param condition_description: [description]
    :type condition_description: str
    :param condition: [description]
    :type condition: Callable[[T], bool]
    :return: None
    :rtype: None
    """
    message = f"expected {value_name} to {condition_description}"
    if not condition(value):
        raise IllegalValueException(message)