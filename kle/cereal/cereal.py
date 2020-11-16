from decimal import Decimal, getcontext
from collections import OrderedDict
from typing import (
    Dict,
    List,
    Tuple,
    TextIO,
    Union,
)
import copy
import json

from .key import Key
from .metadata import Metadata, Background
from .keyboard import Keyboard
from .util import serialize_prop

getcontext().prec = 15


class DeserializeException(Exception):
    """Class for all exceptions encountered during deserialization."""

    def __init__(self, message: str = None,
                 payload: Union[Dict, List] = None):
        """Construct a `DeserializeException`.

        :param message: A message indicating a processing error during
            deserialization of the KLE file.
        :type message: str
        :param payload: The offending payload during deserialization, defaults
            to `None`.
        :type payload: Union[dict, list, None], optional
        """
        super().__init__(
            message + ("\n" + json.dumps(payload) if payload else "")
            if message else None
        )


class SerializeException(Exception):
    """Class for all exceptions encountered during serialization."""

    def __init__(self, message: str = None):
        """Construct a 'SerializeException`.

        :param message: A message indicating a processing error during
            serialization of the keyboard, defaults to `None`.
        :type message: str, optional
        """
        super().__init__(message if message else None)


class Cereal:
    """Class for serializing and deserializing a KLE formatted json."""
    # default Key, use this variable to allow for easy extensions

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

    @classmethod
    def serialize(cls, keyboard: Keyboard) -> str:
        """Serializes the keyboard object to a KLE formatted json file.

        :param keyboard: The keyboard to deserialize.
        :type keyboard: Keyboard
        :return: The prettified formatted json string.
        :rtype: str
        """
        # current key that we track
        rows = list()
        row = list()
        current = Key()
        current.text_color = current.default["text_color"]
        current.align = 4
        cluster_rotation_angle = Decimal(0.0)
        cluster_rotation_x = Decimal(0.0)
        cluster_rotation_y = Decimal(0.0)

        meta_props = OrderedDict()
        def_meta = Metadata()
        metadata = keyboard.metadata  # alias
        serialize_prop(meta_props, "backcolor",
                       metadata.backcolor, def_meta.backcolor)
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
        rows.append(meta_props)

        is_new_row = True
        current.y -= Decimal(1)  # will be incremented on first row
        
        # serialize meta
        def key_sort_criteria(key: Key) -> Tuple[
            Decimal,
            Decimal,
            Decimal,
            Decimal,
            Decimal,
        ]: return (
            (key.rotation_angle + 360) % 360,
            key.rotation_x,
            key.rotation_y,
            key.y,
            key.x,
        )
        sorted_keys = list(sorted(keyboard.keys, key=key_sort_criteria))
        for index, key in enumerate(sorted_keys):
            props = OrderedDict()
            ordered = cls.reorder_labels(key, current)
            
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
                current.y += Decimal(1.0)

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
                ordered["text_color"][0] = key.default["text_color"]
            else:
                for i in range(2, 12):
                    if ordered["text_color"] is None and ordered["text_color"][i] != ordered["text_color"][0]:
                        # maybe an error in the original referenced source code here
                        ordered["text_color"][i] = key.default["text_color"]
            current.text_color = serialize_prop(props, "t", "\n".join(
                ordered["text_color"]).rstrip(), current.text_color)
            current.ghost = serialize_prop(
                props, "g", key.ghost, current.ghost)
            current.profile = serialize_prop(
                props, "p", key.profile, current.profile)
            current.sm = serialize_prop(props, "sm", key.sm, current.sm)
            current.sb = serialize_prop(props, "sb", key.sb, current.sb)
            current.st = serialize_prop(props, "st", key.st, current.st)
            current.align = serialize_prop(
                props, "a", ordered["align"], current.align)
            current.default["text_size"] = serialize_prop(
                props, "f", key.default["text_size"], current.default["text_size"])
            if "f" in props:
                current.textSize = [None for i in range(12)]
            if not cls.compare_text_sizes(
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
            serialize_prop(props, "w2", key.width2, key.width2)
            serialize_prop(props, "h2", key.height2, key.height2)
            serialize_prop(props, "x2", key.x2, 0)
            serialize_prop(props, "y2", key.y2, 0)
            serialize_prop(props, "n", key.nub or False, False)
            serialize_prop(props, "l", key.stepped or False, False)
            serialize_prop(props, "d", key.decal or False, False)
            if len(props) > 0:
                row.append(props)
            current.labels = ordered["labels"]
            row.append("\n".join(ordered["labels"]).rstrip())
        if len(row) > 0:
            rows.append(row)
        return rows

    @classmethod
    def compare_text_sizes(cls, current, key, labels):
        if type(current) is int or type(current) is Decimal:
            current = [current]
        for i in range(12):
            if (
                labels[i] is not None and
                (
                    ((not not current[i]) != (not not key[i])) or
                    (current[i] and current[i] != key[i])
                )
            ):
                return False
        return True

    @classmethod
    def reorder_labels(cls, key: Key, current: Key):
        align = [7, 5, 6, 4, 3, 1, 2, 0]

        # remove impossible flag combinations
        for i in range(len(key.labels)):
            if bool(key.labels[i]):
                align = list(
                    filter(lambda n: n not in cls.disallowed_alignnment_for_labels[i], align))

        # generate label array in correct order
        ret = {
            "align": align[0],
            "labels": ["" for i in range(12)],
            "text_color": ["" for i in range(12)],
            "text_size": [None for i in range(12)],
        }
        for i in range(12):
            if i not in cls.label_map[ret["align"]]:
                continue
            ndx = cls.label_map[ret["align"]].index(i)
            if ndx >= 0:
                if key.labels[i] is not None:
                    ret["labels"][ndx] = key.labels[i]
                if key.text_color[i] is not None:
                    ret["text_color"][ndx] = key.text_color[i]
                if key.text_size[i] is not None:
                    ret["text_size"][ndx] = key.text_size[i]

        # clean up
        for i in range(len(ret["text_size"])):
            if ret["labels"][i] is None:
                ret["text_size"][i] = current.text_size[i]
            if ret["text_size"][i] is None or ret["text_size"] == key.default["text_size"]:
                ret["text_size"][i] = 0
        return ret

    @classmethod
    def reorder_labels_in(cls, items: list, align: int) -> list:
        """Reorders the items in the labels to properly match.

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
                ret[cls.label_map[align][i]] = item
        return ret


    @classmethod
    def deserialize(cls, rows: list) -> Keyboard:
        """Parses the rows of the KLE json to an object of `Keyboard` class
        suitable for simple third-party api usage.

        :param rows: The `list` of `list` or `dict` generated by loading the
            json.
        :type rows: list
        :raises DeserializeException: Rows should be of type `list`.
        :raises DeserializeException: Rotation changes can only be made at the
            beginning of each row.
        :raises DeserializeException: An unexpected item in the row (not of
            type `dict` or `list`).
        :raises DeserializeException: Keyboard metadata, a `dict`, can only be
            specified as the first element in the row.
        :return: The json data parsed into an object of class `Keyboard`.
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
                    key = rows[r][k]
                    if type(key) is str:
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
                        new_key.labels = cls.reorder_labels_in(
                            key.split("\n"), align)
                        new_key.text_size = cls.reorder_labels_in(
                            new_key.text_size, align)
                        # clean up generated data
                        for i in range(12):
                            if not new_key.labels[i]:
                                new_key.text_size[i] = None
                                new_key.text_color[i] = None
                            if new_key.text_size[i] == new_key.default["text_size"]:
                                new_key.text_size[i] = None
                            if new_key.text_color[i] == new_key.default["text_color"]:
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
        
                    else:
                        if k != 0 and (
                            "r" in key or
                            "rx" in key or
                            "ry" in key
                        ): raise DeserializeException(
                            "Rotation changes can only be made at the \
                                beginning of the row:",
                            rows[r]
                        )
                        # rotation changes can only be specified at beginning of row
                        if "r" in key:
                            current.rotation_angle = Decimal(key["r"])
                        if "rx" in key:
                            current.rotation_x = Decimal(key["rx"])
                            cluster_rotation_x = Decimal(key["rx"])
                            current.x = cluster_rotation_x
                            current.y = cluster_rotation_y
                        if "ry" in key:
                            current.rotation_y = Decimal(key["ry"])
                            cluster_rotation_y = Decimal(key["ry"])
                            current.x = cluster_rotation_x
                            current.y = cluster_rotation_y
                        if "a" in key:
                            align = key["a"]
                        if "f" in key:
                            current.default["text_size"] = key["f"]
                            current.text_size = [None for i in range(12)]
                        if "f2" in key:
                            for i in range(1, 12):
                                current.text_size[i] = key["f2"]
                        if "fa" in key:
                            current.text_size = key["fa"]
                        if "p" in key:
                            current.profile = key["p"]
                        if "c" in key:
                            current.color = key["c"]
                        if "t" in key:
                            split = key["t"].split("\n")
                            current.default["text_color"] = split[0]
                            current.text_color = cls.reorder_labels_in(split, align)
                        if "x" in key and key["x"] != 0:
                            current.x += Decimal(key["x"])
                        if "y" in key:
                            current.y += Decimal(key["y"])
                        if "w" in key:
                            current.width = Decimal(key["w"])
                            current.width2 = Decimal(key["w"])
                        if "h" in key:
                            current.height = Decimal(key["h"])
                            current.height2 = Decimal(key["h"])
                        if "x2" in key:
                            current.x2 = Decimal(key["x2"])
                        if "y2" in key:
                            current.y2 = Decimal(key["y2"])
                        if "w2" in key:
                            current.width2 = Decimal(key["w2"])
                        if "h2" in key:
                            current.height2 = Decimal(key["h2"])
                        if "n" in key:
                            current.nub = key["n"]
                        if "l" in key:
                            current.stepped = key["l"]
                        if "d" in key:
                            current.decal = key["d"]
                        if "g" in key:
                            current.ghost = key["g"]
                        if "sm" in key:
                            current.sm = key["sm"]
                        if "sb" in key:
                            current.sb = key["sb"]
                        if "st" in key:
                            current.st = key["st"]
                current.y += Decimal(1.0)
            elif type(rows[r]) is dict:
                if r != 0:
                    raise DeserializeException(
                        f"Keyboard metadata can only be at index 0, is index {r}:",
                        rows[r]
                    )
                # unpack metadata into keyboard metadata
                metadata = rows[r]  # aliased
                if "author" in metadata:
                    keyboard.metadata.author = metadata["author"]
                if "backcolor" in metadata:
                    keyboard.metadata.backcolor = metadata["backcolor"]
                if "background" in metadata:
                    if "name" in metadata["background"]:
                        keyboard.metadata.background.name = metadata["background"]["name"]
                    if "style" in metadata["background"]:
                        keyboard.metadata.background.style = metadata["background"]["style"]
                if "name" in metadata:
                    keyboard.metadata.name = metadata["name"]
                if "notes" in metadata:
                    keyboard.metadata.notes = metadata["notes"]
                if "radii" in metadata:
                    keyboard.metadata.radii = metadata["radii"]
                if "switchBrand" in metadata:
                    keyboard.metadata.switch_mount = metadata["switchBrand"]
                if "switchMount" in metadata:
                    keyboard.metadata.switch_mount = metadata["switchMount"]
                if "switchType" in metadata:
                    keyboard.metadata.switch_type = metadata["switchType"]
                if "pcb" in metadata:
                    keyboard.metadata.pcb = metadata["pcb"]
                if "plate" in metadata:
                    keyboard.metadata.plate = metadata["plate"]
            else:
                raise DeserializeException(
                    f"Unexpected row type: {type(rows[r])}",
                    rows[r]
                )
            current.x = Decimal(current.rotation_x)
        return keyboard

    # following json library conventions
    @classmethod
    def loads(cls, s: str) -> Keyboard:
        """Converts a KLE formatted json of type `str` into a `Keyboard`.

        :param s: The KLE formatted json `str`.
        :type s: str
        :return: Resulting instance of `Keyboard` from the string.
        :rtype: Keyboard
        """
        return cls.deserialize(json.loads(s))

    # parse from file
    @classmethod
    def load(cls, f: TextIO) -> Keyboard:
        """Converts a KLE formatted json file into a `Keyboard`. NOTE: does not
        close the file.

        :param f: An open `file` with read permissions.
        :type f: TextIO
        :return: Resulting instance of `Keyboard` from the file.
        :rtype: Keyboard
        """
        return cls.deserialize(json.load(f))

    @classmethod
    def dumps(cls, keyboard: Keyboard) -> str:
        """Converts a `Keyboard` into a KLE formatted json `str`.

        :param keyboard: An instance of `Keyboard` to convert.
        :type keyboard: Keyboard
        :return: The resulting string from the `Keyboard`.
        :rtype: str
        """

        json_str = json.dumps(cls.serialize(keyboard),
                              indent=2, sort_keys=False, ensure_ascii=False)
        return json_str

    @classmethod
    def dump(cls, keyboard: Keyboard, file: TextIO):
        """Converts a `Keyboard` into a KLE formatted json `str` and writes the
        string into a open file. NOTE: Does not close the file.

        :param keyboard: An instance of `Keyboard` to dump.
        :type keyboard: Keyboard
        :param file: An open `file` with write permissions.
        :type file: TextIO
        """
        file.write(cls.dumps(keyboard))


# aliases for static class methods
load = Cereal.load
loads = Cereal.loads
dump = Cereal.dump
dumps = Cereal.dumps
