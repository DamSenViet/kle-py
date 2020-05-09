import decimal as dec
import collections as col
import copy
import json
import typing as typ
import pprint

from .key import Key
from .metadata import Metadata, Background
from .keyboard import Keyboard
from .util import serialize_prop

# dec.getcontext().prec = 15

class DeserializeException(Exception):
    """Class for all exceptions encountered during deserialization."""

    def __init__(self, message: str = None,
        payload: typ.Union[dict, list] = None):
        """Construct a `DeserializeException`.

        :param message: A message indicating a processing error during
            deserialization of the KLE file.
        :type message: str
        :param payload: The offending payload during deserialization, defaults
            to `None`.
        :type payload: typ.Union[dict, list, None], optional
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
    key_class = Key

    label_map = [
        [ 0, 6, 2, 8, 9,11, 3, 5, 1, 4, 7,10], # 0 = no centering
        [ 1, 7,-1,-1, 9,11, 4,-1,-1,-1,-1,10], # 1 = center x
        [ 3,-1, 5,-1, 9,11,-1,-1, 4,-1,-1,10], # 2 = center y
        [ 4,-1,-1,-1, 9,11,-1,-1,-1,-1,-1,10], # 3 = center x & y
        [ 0, 6, 2, 8,10,-1, 3, 5, 1, 4, 7,-1], # 4 = center front (default)
        [ 1, 7,-1,-1,10,-1, 4,-1,-1,-1,-1,-1], # 5 = center front & x
        [ 3,-1, 5,-1,10,-1,-1,-1, 4,-1,-1,-1], # 6 = center front & y
        [ 4,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,-1], # 7 = center front & x & y
    ]

    disallowed_alignnment_for_labels = [
        [1,2,3,5,6,7],	#0
        [2,3,6,7],			#1
        [1,2,3,5,6,7],	#2
        [1,3,5,7],			#3
        [],							#4
        [1,3,5,7],			#5
        [1,2,3,5,6,7],	#6
        [2,3,6,7],			#7
        [1,2,3,5,6,7],	#8
        [4,5,6,7],			#9
        [],							#10
        [4,5,6,7]
    ]

    @classmethod
    def key_sort_criteria(cls, key) -> (
        dec.Decimal,
        dec.Decimal,
        dec.Decimal,
        dec.Decimal,
        dec.Decimal
    ):
        """Lambda that returns ordering criteria for key sorting.

        :param key: A single key consumed by python `sort`.
        :type key: Key
        :return: Tuple with ordering criteria.
        :rtype: tuple
        """
        return (
            (key.rotation_angle + 360) % 360,
            key.rotation_x,
            key.rotation_y,
            key.y,
            key.x
        )

    @classmethod
    def serialize(cls, keyboard: Keyboard) -> str:
        """Serializes the keyboard object to a KLE formatted json file.

        :param keyboard: The keyboard to deserialize.
        :type keyboard: Keyboard
        :return: The prettified formatted json string.
        :rtype: str
        """
        # current key that we track
        keys = keyboard.keys
        rows = list()
        row = list()
        current = cls.key_class()
        current.text_color = current.default["text_color"]
        current.align = 4
        cluster_rotation_angle = dec.Decimal(0.0)
        cluster_rotation_x = dec.Decimal(0.0)
        cluster_rotation_y = dec.Decimal(0.0)

        if keyboard.metadata is not None:
            meta_props = col.OrderedDict()
            def_meta = Metadata()
            metadata = keyboard.metadata # alias
            serialize_prop(meta_props, "backcolor", metadata.backcolor, def_meta.backcolor)
            serialize_prop(meta_props, "name", metadata.name, def_meta.name)
            serialize_prop(meta_props, "author", metadata.author, def_meta.author)
            serialize_prop(meta_props, "notes", metadata.notes, def_meta.notes)
            if metadata.background is not None:
                background = metadata.background # alias
                bg_props = col.OrderedDict()
                def_bg = Background()
                serialize_prop(bg_props, "name", background.name, def_bg.name)
                serialize_prop(bg_props, "style", background.style, def_bg.style)
                if len(bg_props) > 0:
                    serialize_prop(meta_props, "background", bg_props, None)
            serialize_prop(meta_props, "radii", metadata.radii, def_meta.radii)
            serialize_prop(meta_props, "switchMount", metadata.switch_mount, def_meta.switch_mount)
            serialize_prop(meta_props, "switchBrand", metadata.switch_brand, def_meta.switch_brand)
            serialize_prop(meta_props, "switchType", metadata.switch_type, def_meta.switch_type)
            serialize_prop(meta_props, "pcb", metadata.pcb, def_meta.pcb)
            serialize_prop(meta_props, "plate", metadata.plate, def_meta.plate)
            rows.append(meta_props)

        is_new_row = False
        # serialize meta
        for key_n, key in enumerate(sorted(keyboard.keys, key=cls.key_sort_criteria)):
            props = col.OrderedDict()
            ordered = cls.reorder_labels(key, current)

            is_origin_changed = (
                cluster_rotation_x != key.rotation_x or
                cluster_rotation_y != key.rotation_y)
            is_cluster_changed = (
                is_origin_changed or
                cluster_rotation_angle != key.rotation_angle)
            is_row_changed = current.y != key.y

            # on first pass, this never triggers
            if len(row) > 0 and is_row_changed or is_cluster_changed:
                rows.append(row)
                row = list()
                is_new_row = True

            if is_new_row:
                if key_n != 0:
                    current.y += dec.Decimal(1.0)
                if (
                    key.rotation_y != cluster_rotation_y or
                    key.rotation_x != cluster_rotation_x
                ):
                    if is_origin_changed:
                        current.y = key.rotation_y
                current.x = key.rotation_x

                cluster_rotation_angle = key.rotation_angle
                cluster_rotation_x = key.rotation_x
                cluster_rotation_y = key.rotation_y

                is_new_row = False
            current.rotation_angle = serialize_prop(props, "r", key.rotation_angle, cluster_rotation_angle)
            current.rotation_x = serialize_prop(props, "rx", key.rotation_x, current.rotation_x)
            current.rotation_y = serialize_prop(props, "ry", key.rotation_y, current.rotation_y)
            current.y += serialize_prop(props, "y", key.y - current.y, 0)
            current.x += serialize_prop(props, "x", key.x - current.x, 0) + key.width
            current.color = serialize_prop(props, "c", key.color, current.color)
            # if statement for ordered color
            if ordered["text_color"][0] is None:
                ordered["text_color"][0] = key.default["text_color"]
            else:
                for i in range(2, 12):
                    if ordered["text_color"] is None and ordered["text_color"][i] != ordered["text_color"][0]:
                        # maybe an error in the original referenced source code here
                        ordered["text_color"][i] = key.default["text_color"]
            current.text_color = serialize_prop(props, "t", "\n".join(ordered["text_color"]).rstrip(), current.text_color)
            current.ghost = serialize_prop(props, "g", key.ghost, current.ghost)
            current.profile = serialize_prop(props, "p", key.profile, current.profile)
            current.sm = serialize_prop(props, "sm", key.sm, current.sm)
            current.sb = serialize_prop(props, "sb", key.sb, current.sb)
            current.st = serialize_prop(props, "st", key.st, current.st)
            current.align = serialize_prop(props, "a", ordered["align"], current.align)
            current.default["text_size"] = serialize_prop(props, "f", key.default["text_size"], current.default["text_size"])
            if "f" in props: current.textSize = []
            # compare text sizes
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
                        current.text_size = serialize_prop(props, "fa", ordered["text_size"], [])
            serialize_prop(props, "w", key.width, 1)
            serialize_prop(props, "h", key.height, 1)
            serialize_prop(props, "w2", key.width2, key.width)
            serialize_prop(props, "h2", key.height2, key.height)
            serialize_prop(props, "x2", key.x2, 0)
            serialize_prop(props, "y2", key.y2, 0)
            serialize_prop(props, "n", key.nub or False, False)
            serialize_prop(props, "l", key.stepped or False, False)
            serialize_prop(props, "d", key.decal or False, False)
            if len(props) > 0: row.append(props)
            current.labels = ordered["labels"]
            row.append("\n".join(ordered["labels"]).rstrip())
        if len(row) > 0:
            rows.append(row)
        return rows

    @classmethod
    def compare_text_sizes(cls, current, key, labels):
        if type(current) is int or type(current) is dec.Decimal:
            current = [current]
        for i in range(12):
            if (
                labels[i] is not None and
                (
                    # shitty code ported from original shitty source
                    (bool(current[i]) != bool(key[i])) or
                    (current[i] != key[i])
                )
            ):
                return False
        return True

    @classmethod
    def reorder_labels(cls, key: Key, current: Key):
        align = [7, 5, 6, 4, 3, 1, 2, 0]

        # remove impossible flag combinations
        for i in range(len(key.labels)):
            if key.labels[i] is not None:
                align = list(filter(lambda n: n not in cls.disallowed_alignnment_for_labels[i], align))

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
            if item: ret[cls.label_map[align][i]] = item
        return ret

    @classmethod
    def deserialize_adjustment(
        cls,
        key: Key,
        align: int,
        cluster_rotation_angle: dec.Decimal,
        cluster_rotation_x: dec.Decimal,
        cluster_rotation_y: dec.Decimal,
        item: dict,
    # needs to return everything in same order
    ) -> (
        Key,
        int,
        dec.Decimal,
        dec.Decimal,
        dec.Decimal,
    ):
        """Interprets the adjustments (formatted as a `dict`) specified by the
        `dict` keys and returns the appropriate data to the parsing loop.

        :param key: The copy of the key data tracked in the parsing loop.
        :type key: Key
        :param align:
        :type align: int
        :param cluster_rotation_angle: The current rotation angle.
        :type cluster_rotation_angle: dec.Decimal
        :param cluster_rotation_x: The current rotation point on the x axis.
        :type cluster_rotation_x: dec.Decimal
        :param cluster_rotation_y: The current rotation point on the y axis.
        :type cluster_rotation_y: dec.Decimal
        :return: A tuple of all arguments in the same order without the
            adjustment item. Used to overwrite tracked data in parsing
            loop.
        :rtype: tuple
        """
        # rotation changes can only be specified at beginning of row
        if item.get("r"): key.rotation_angle = dec.Decimal(item["r"])
        if item.get("rx"): key.rotation_x = dec.Decimal(item["rx"])
        if item.get("ry"): key.rotation_y = dec.Decimal(item["ry"])

        # check for resets against rotation rows
        is_origin_changed = (
            cluster_rotation_x != key.rotation_x or
            cluster_rotation_y != key.rotation_y
        )

        is_cluster_changed = (
            cluster_rotation_angle != key.rotation_angle or
            is_origin_changed
        )

        if is_cluster_changed:
            if is_origin_changed:
                key.y = key.rotation_y

            cluster_rotation_angle = key.rotation_angle
            cluster_rotation_x = key.rotation_x
            cluster_rotation_y = key.rotation_y
            key.x = key.rotation_x

        if item.get("a"): algin = item["a"]
        if item.get("f"):
            key.text_size = [None for i in range(12)]
            key.text_color = [None for i in range(12)]
        if item.get("f2"):
            for i in range(12):
                key.text_size[i] = item["f2"]
        if item.get("fa"): key.text_size = item["fa"]
        if item.get("p"): key.profile = item["p"]
        if item.get("c"): key.color = item["c"]
        if item.get("t"):
            split = item["t"].split("\n")
            if len(split[0]) == 0: key.default["text_color"] = split[0]
            key.text_color = cls.reorder_labels_in(split, align)
        if item.get("x"): key.x += dec.Decimal(item["x"])
        if item.get("y"): key.y += dec.Decimal(item["y"])
        if item.get("w"):
            key.width = dec.Decimal(item["w"])
            key.width2 = dec.Decimal(item["w"])
        if item.get("h"):
            key.height = dec.Decimal(item["h"])
            key.height2 = dec.Decimal(item["h"])
        if item.get("x2"): key.x2 = dec.Decimal(item["x2"])
        if item.get("y2"): key.y2 = dec.Decimal(item["y2"])
        if item.get("w2"): key.width2 = dec.Decimal(item["width2"])
        if item.get("h2"): key.height2 = dec.Decimal(item["height2"])
        if item.get("n"): key.nub = item["n"]
        if item.get("l"): key.stepped = item["l"]
        if item.get("d"): key.decal = item["d"]
        if item.get("g"): key.ghost = item["g"]
        if item.get("sm"): key.sm = item["sm"]
        if item.get("sb"): key.sb = item["sb"]
        if item.get("st"): key.st = item["st"]
        return (
            key,
            align,
            cluster_rotation_angle,
            cluster_rotation_x,
            cluster_rotation_y
        )

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
        key = cls.key_class() # readies the next key data when str encountered
        keyboard = Keyboard()
        align = 4

        # keys are row separated by clusters, clusters defines
        cluster_rotation_angle = dec.Decimal(0.0)
        cluster_rotation_x = dec.Decimal(0.0)
        cluster_rotation_y = dec.Decimal(0.0)

        # for object in list
        for r in range(len(rows)):
            if type(rows[r]) == list:
                # for item in list
                for k in range(len(rows[r])):
                    item = rows[r][k]
                    if type(item) == str:
                        # create copy of key data
                        new_key = copy.deepcopy(key)

                        # calculate generated values
                        new_key.width2 = key.width if new_key.width2 == 0 else key.width
                        new_key.height2 = key.width if new_key.height2 == 0 else key.height
                        new_key.labels = cls.reorder_labels_in(item.split("\n"), align)
                        new_key.text_size = cls.reorder_labels_in(new_key.text_size, align)

                        # clean up generated data
                        for i in range(12):
                            if not new_key.labels[i]:
                                new_key.text_size[i] = None
                                new_key.text_color[i] = None
                            if new_key.text_size[i] == new_key.default["text_size"]:
                                new_key.text_size[i] = None
                            if new_key.text_color[i] == new_key.default["text_color"]:
                                new_key.text_color = None

                        # add key
                        keyboard.keys.append(new_key)

                        # adjustments for next key gen
                        key.x += dec.Decimal(key.width)
                        key.width = 1
                        key.height = 1
                        key.x2 = 0
                        key.y2 = 0
                        key.width2 = 0
                        key.height2 = 0
                        key.nub = False
                        key.stepped = False
                        key.decal = False

                    else:
                        if k != 0 and (item.get("r") or
                            item.get("rx") or
                            item.get("ry")):
                            raise DeserializeException(
                                "Rotation changes can only be made at the \
                                 beginning of the row:",
                                rows[r]
                            )
                        (
                            key,
                            align,
                            cluster_rotation_angle,
                            cluster_rotation_x,
                            cluster_rotation_y
                        ) = cls.deserialize_adjustment(
                            copy.deepcopy(key, {}),
                            align,
                            cluster_rotation_angle,
                            cluster_rotation_x,
                            cluster_rotation_y,
                            item
                        )

                key.y += dec.Decimal(1.0)
                key.x = dec.Decimal(key.rotation_x)
            elif type(rows[r]) == dict:
                if r != 0:
                    raise DeserializeException(
                        f"Keyboard metadata can only be at index 0, is index {r}:",
                        rows[r]
                    )
                # unpack metadata into keyboard metadata
                metadata = rows[r] # aliased
                keyboard.metadata = Metadata() # instantiate metadata
                keyboard.metadata.author = metadata.get("author")
                if metadata.get("backcolor"):
                    keyboard.metadata.backcolor = metadata.get("backcolor")
                if metadata.get("background"):
                    keyboard.metadata.background = Background(
                        metadata["background"].get("name"),
                        metadata["background"].get("style")
                    )
                keyboard.metadata.name = metadata.get("name")
                keyboard.metadata.notes = metadata.get("notes")
                keyboard.metadata.radii = metadata.get("radii")
                keyboard.metadata.switch_brand = metadata.get("switchBrand")
                keyboard.metadata.switch_mount = metadata.get("switchMount")
                keyboard.metadata.switch_type = metadata.get("switchType")
                keyboard.metadata.pcb = metadata.get("pcb")
                keyboard.metadata.plate = metadata.get("plate")
            else:
                raise DeserializeException(
                    f"Unexpected row type: {type(rows[r])}",
                    rows[r]
                )
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
    def load(cls, f: typ.TextIO) -> Keyboard:
        """Converts a KLE formatted json file into a `Keyboard`. NOTE: does not
        close the file.

        :param f: An open `file` with read permissions.
        :type f: typ.TextIO
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

        json_str = json.dumps(cls.serialize(keyboard), indent=2, sort_keys=False)
        return json_str

    @classmethod
    def dump(cls, keyboard: Keyboard, file: typ.TextIO):
        """Converts a `Keyboard` into a KLE formatted json `str` and writes the
        string into a open file. NOTE: Does not close the file.

        :param keyboard: An instance of `Keyboard` to dump.
        :type keyboard: Keyboard
        :param file: An open `file` with write permissions.
        :type file: typ.TextIO
        """
        file.write(cls.dumps(keyboard))

# aliases for static class methods
load = Cereal.load
loads = Cereal.loads
dump = Cereal.dump
dumps = Cereal.dumps