import copy
import json
from decimal import (
    Decimal,
    getcontext
)
from collections import (
    OrderedDict,
)
from typing import (
    Dict,
    List,
    Tuple,
    TextIO,
    Union,
)

from .key import Key
from .metadata import Metadata
from .background import Background
from .keyboard import Keyboard
from .exceptions import (
    DeserializeException,
)
from .utils import (
    key_sort_criteria,
    serialize_prop,
    reorder_labels,
    reorder_labels_in,
    compare_text_sizes,
)

getcontext().prec = 64


def serialize(keyboard: Keyboard) -> List[Union[Dict, List[Union[str, Dict]]]]:
    """Serializes the keyboard object to a KLE formatted json file.

    :param keyboard: The keyboard to deserialize.
    :type keyboard: Keyboard
    :return: The KLE formatted json string.
    :rtype: List[Union[Dict, List[Union[str, Dict]]]]
    """
    # current key that we track
    rows = list()
    row = list()
    current = Key()
    current.text_color = current.default_text_color
    current.align = 4
    cluster_rotation_angle = Decimal(0.0)
    cluster_rotation_x = Decimal(0.0)
    cluster_rotation_y = Decimal(0.0)

    meta_props = OrderedDict()
    def_meta = Metadata()
    metadata = keyboard.metadata  # alias
    serialize_prop(meta_props, "backcolor",
                   metadata.background_color, def_meta.background_color)
    serialize_prop(meta_props, "name", metadata.name, def_meta.name)
    serialize_prop(meta_props, "author", metadata.author, def_meta.author)
    serialize_prop(meta_props, "notes", metadata.notes, def_meta.notes)
    background = metadata.background  # alias
    bg_props = OrderedDict()
    def_bg = Background()
    serialize_prop(bg_props, "name", background.name, def_bg.name)
    serialize_prop(bg_props, "style", background.style, def_bg.style)
    if len(bg_props) > 0:
        serialize_prop(meta_props, "background", bg_props, None)
    serialize_prop(meta_props, "radii", metadata.radii, def_meta.radii)
    serialize_prop(meta_props, "switchMount",
                   metadata.switch_mount, def_meta.switch_mount)
    serialize_prop(meta_props, "switchBrand",
                   metadata.switch_brand, def_meta.switch_brand)
    serialize_prop(meta_props, "switchType",
                   metadata.switch_type, def_meta.switch_type)
    serialize_prop(meta_props, "pcb", metadata.pcb, def_meta.pcb)
    serialize_prop(meta_props, "plate", metadata.plate, def_meta.plate)
    if len(meta_props) > 0:
        rows.append(meta_props)

    is_new_row = True
    current.y -= Decimal(1)  # will be incremented on first row

    sorted_keys = list(sorted(keyboard.keys, key=key_sort_criteria))
    for key in sorted_keys:
        props = OrderedDict()
        ordered = reorder_labels(key, current)

        # start a new row when necessary
        is_cluster_changed = (
            (key.rotation_angle != cluster_rotation_angle) or
            (key.rotation_x != cluster_rotation_x) or
            (key.rotation_y != cluster_rotation_y)
        )
        is_row_changed = (key.y != current.y)
        if len(row) > 0 and (is_row_changed or is_cluster_changed):
            # set up for the new row
            rows.append(row)
            row = list()
            is_new_row = True

        if is_new_row:
            current.y += Decimal(1)

            # set up for the new row
            # y is reset if either rx or ry are changed
            if (
                key.rotation_y != cluster_rotation_y or
                key.rotation_x != cluster_rotation_x
            ):
                current.y = key.rotation_y
            # always reset x to rx (which defaults to zero)
            current.x = key.rotation_x

            # update current cluster
            cluster_rotation_angle = key.rotation_angle
            cluster_rotation_x = key.rotation_x
            cluster_rotation_y = key.rotation_y

            is_new_row = False

        current.rotation_angle = serialize_prop(
            props, "r", key.rotation_angle, current.rotation_angle)
        current.rotation_x = serialize_prop(
            props, "rx", key.rotation_x, current.rotation_x)
        current.rotation_y = serialize_prop(
            props, "ry", key.rotation_y, current.rotation_y)
        current.y += serialize_prop(props, "y",
                                    key.y - current.y, Decimal(0))
        current.x += serialize_prop(props, "x",
                                    key.x - current.x, Decimal(0)) + key.width
        current.color = serialize_prop(
            props, "c", key.color, current.color)
        # if statement for ordered color
        if not ordered["text_color"][0]:
            ordered["text_color"][0] = key.default_text_color
        else:
            for i in range(2, 12):
                if (
                    ordered["text_color"] is None and
                    ordered["text_color"][i] != ordered["text_color"][0]
                ):
                    # maybe an error in the original referenced source code here
                    ordered["text_color"][i] = key.default["text_color"]
        current.text_color = serialize_prop(props, "t", "\n".join(
            ordered["text_color"]).rstrip(), current.text_color)
        current.ghost = serialize_prop(
            props, "g", key.ghost, current.ghost)
        current.profile = serialize_prop(
            props, "p", key.profile, current.profile)
        current.sm = serialize_prop(
            props, "sm", key.switch_mount, current.switch_mount)
        current.sb = serialize_prop(
            props, "sb", key.switch_brand, current.switch_brand)
        current.st = serialize_prop(
            props, "st", key.switch_type, current.switch_type)
        current.align = serialize_prop(
            props, "a", ordered["align"], current.align)
        current.default_text_size = serialize_prop(
            props, "f", key.default_text_size, current.default_text_size)
        if "f" in props:
            current.textSize = [None for i in range(12)]
        if not compare_text_sizes(
                current.text_size, ordered["text_size"], ordered["labels"]):
            if (len(ordered["text_size"]) == 0):
                serialize_prop(props, "f", key.default["text_size"], -1)
            else:
                optimizeF2 = not bool(ordered["text_size"][0])
                for i in range(2, len(ordered["text_size"])):
                    if not optimizeF2:
                        break
                    optimizeF2 = ordered["text_size"][i] == ordered["text_size"][1]
                if optimizeF2:
                    f2 = ordered["text_size"][1]
                    # current.f2 = serialize_prop(props, "f2", f2, -1)
                    current.text_size = [1] + [f2 for i in range(11)]
                else:
                    current.f2 = None
                    current.text_size = serialize_prop(
                        props, "fa", ordered["text_size"], [])
        serialize_prop(props, "w", key.width, 1)
        serialize_prop(props, "h", key.height, 1)
        serialize_prop(props, "w2", key.width2, key.width)
        serialize_prop(props, "h2", key.height2, key.height)
        serialize_prop(props, "x2", key.x2, 0)
        serialize_prop(props, "y2", key.y2, 0)
        serialize_prop(props, "n", key.nub or False, False)
        serialize_prop(props, "l", key.stepped or False, False)
        serialize_prop(props, "d", key.decal or False, False)
        if len(props) > 0:
            row.append(props)
        current.text_labels = ordered["labels"]
        row.append("\n".join(ordered["labels"]).rstrip())
    if len(row) > 0:
        rows.append(row)
    return rows


def deserialize(rows: List[Union[Dict, List[Union[str, Dict]]]]) -> Keyboard:
    """Deserializes a KLE json array into a keyboard.

    :param rows: the rows of the KLE json
    :type rows: List[Union[Dict, List[Union[str, Dict]]]]
    :raises DeserializeException: rows is not an array
    :raises DeserializeException: rotation changes not made at beginning of row
    :raises DeserializeException: metadata specified but not first object in json
    :raises DeserializeException: a row in the json is not an expected type
    :return: the Keyboard
    :rtype: Keyboard
    """
    if type(rows) != list:
        raise DeserializeException("Expected an array of objects:", rows)

    # track rotation info for reset x/y positions
    # if rotation_angle != 0, it is always specified LAST
    current = Key()  # readies the next key data when str encountered
    keyboard = Keyboard()
    align = 4

    # keys are row separated by clusters, clusters defines
    cluster_rotation_x = Decimal(0.0)
    cluster_rotation_y = Decimal(0.0)

    # for object in list
    for r in range(len(rows)):
        if type(rows[r]) is list:
            # for item in list
            for k in range(len(rows[r])):
                item = rows[r][k]
                if type(item) is str:
                    label = item
                    # create copy of key data
                    new_key = copy.deepcopy(current, {})

                    # calculate generated values
                    new_key.width2 = (
                        current.width
                        if new_key.width2 == 0
                        else current.width2
                    )
                    new_key.height2 = (
                        current.height
                        if new_key.height2 == 0
                        else current.height2
                    )
                    new_key.text_labels = reorder_labels_in(
                        label.split("\n"), align)
                    new_key.text_size = reorder_labels_in(
                        new_key.text_size, align)
                    # clean up generated data
                    for i in range(12):
                        if not new_key.text_labels[i]:
                            new_key.text_size[i] = None
                            new_key.text_color[i] = None
                        if new_key.text_size[i] == new_key.default_text_size:
                            new_key.text_size[i] = None
                        if new_key.text_color[i] == new_key.default_text_color:
                            new_key.text_color[i] = None

                    # add key
                    keyboard.keys.append(new_key)

                    # adjustments for next key gen
                    current.x += Decimal(current.width)
                    current.width = Decimal(1)
                    current.height = Decimal(1)
                    current.x2 = Decimal(0)
                    current.y2 = Decimal(0)
                    current.width2 = Decimal(0)
                    current.height2 = Decimal(0)
                    current.nub = False
                    current.stepped = False
                    current.decal = False
                elif type(item) is dict:
                    key_changes = item
                    if k != 0 and (
                        "r" in key_changes or
                        "rx" in key_changes or
                        "ry" in key_changes
                    ):
                        raise DeserializeException(
                            "Rotation changes can only be made at the \
                            beginning of the row:",
                            rows[r]
                        )
                    # rotation changes can only be specified at beginning of row
                    (
                        align,
                        cluster_rotation_x,
                        cluster_rotation_y,
                    ) = record_key_changes(
                        current,
                        key_changes,
                        align,
                        cluster_rotation_x,
                        cluster_rotation_y
                    )
                else:
                    raise DeserializeException(
                        "Expected an object specifying key changes or a label \
                        for a key",
                        item
                    )
            current.y += Decimal(1.0)
        elif type(rows[r]) is dict:
            metadata_changes = rows[r]
            if r != 0:
                raise DeserializeException(
                    f"Keyboard metadata can only be at index 0, is index {r}:",
                    rows[r]
                )
            record_metadata_changes(keyboard.metadata, metadata_changes)
        else:
            raise DeserializeException(
                f"Unexpected row type: {type(rows[r])}",
                rows[r]
            )
        current.x = Decimal(current.rotation_x)
    return keyboard


def record_metadata_changes(metadata: Metadata, metadata_changes: Dict) -> None:
    """Records the changes into the metadata.

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
    if "switchBrand" in metadata_changes:
        metadata.switch_mount = metadata_changes["switchBrand"]
    if "switchMount" in metadata_changes:
        metadata.switch_mount = metadata_changes["switchMount"]
    if "switchType" in metadata_changes:
        metadata.switch_type = metadata_changes["switchType"]
    if "pcb" in metadata_changes:
        metadata.pcb = metadata_changes["pcb"]
    if "plate" in metadata_changes:
        metadata.plate = metadata_changes["plate"]


def record_key_changes(
    key: Key,
    key_changes: Dict,
    align: int,
    cluster_rotation_x: Decimal,
    cluster_rotation_y: Decimal
) -> Tuple[int, Decimal, Decimal]:
    """Records the changes into the key.

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
        key.text_size = [None for i in range(12)]
    if "f2" in key_changes:
        for i in range(1, 12):
            key.text_size[i] = key_changes["f2"]
    if "fa" in key_changes:
        key.text_size = key_changes["fa"]
    if "p" in key_changes:
        key.profile = key_changes["p"]
    if "c" in key_changes:
        key.color = key_changes["c"]
    if "t" in key_changes:
        split = key_changes["t"].split("\n")
        key.default_text_color = split[0]
        key.text_color = reorder_labels_in(split, align)
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


def loads(string: str) -> Keyboard:
    """Converts a KLE formatted json string into a Keyboard.

    :param string: the KLE formatted json string
    :type string: str
    :return: the Keyboard
    :rtype: Keyboard
    """
    return deserialize(json.loads(string))


def load(file: TextIO) -> Keyboard:
    """Converts a KLE formatted json file into a Keyboard.

    :param file: an open file with read permissions
    :type file: TextIO
    :return: the Keyboard
    :rtype: Keyboard
    """
    return deserialize(json.load(file))


def dumps(keyboard: Keyboard) -> str:
    """Converts a Keyboard into a KLE formatted json str.

    :param keyboard: the Keyboard to convert
    :type keyboard: Keyboard
    :return: the KLE formatted json str
    :rtype: str
    """

    json_str = json.dumps(serialize(keyboard),
                          indent=2, sort_keys=False, ensure_ascii=False)
    return json_str


def dump(keyboard: Keyboard, file: TextIO) -> None:
    """Converts a Keyboard into a KLE formatted json file.

    :param keyboard: a Keyboard
    :type keyboard: Keyboard
    :param file: an open file with write permissions
    :type file: TextIO
    """
    file.write(dumps(keyboard))
