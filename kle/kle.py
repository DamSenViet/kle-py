from typing import TextIO, Union
from collections import OrderedDict
from copy import deepcopy
from decimal import Decimal
import json

from .key import Key
from .metadata import Metadata, Background
from .keyboard import Keyboard

class DeserializeException(Exception):
    """Class for all exceptions encountered during deserialization."""

    def __init__(self, message: str, payload: Union[dict, list] = None) -> None:
        """Construct a `DeserializeException`.

        Arguments:
            message {str} -- A message indicating a processing error during
                             deserialization of the KLE file.

        Keyword Arguments:
            payload {some primitive} -- The offending payload during deserialization.
                              (default: {`None`})
        """
        super().__init__(message +
            ("\n" + json.dumps(payload) if payload else ""))

class SerializeException(Exception):
    """Class for all exceptions encountered during serialization."""

    def __init__(self, message: str) -> None:
        """Construct a 'SerializeException`.

        Arguments:
            message {str} -- A message indicating a processing error during
                             serialization of the keyboard.
        """
        super().__init__(message)

class KLE:
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

    @classmethod
    def serialize(cls, keyboard: Keyboard) -> str:
        """Serializes a keyboard into a KLE json `str`.

        Arguments:
            keyboard {Keyboard} -- The keyboard to serialize.

        Returns:
            str -- The KLE json.
        """
        pass

    @classmethod
    def reorder_labels(cls, items: list, align: int) -> list:
        """Reorders the items in the labels to properly match.

        Arguments:
            items {list} -- items to be reordered.
            align {int} -- The alignment option.

        Returns:
            list -- The reordered labels.
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
        current_rotation: Decimal,
        current_rotation_x: Decimal,
        current_rotation_y: Decimal,
        item: dict,
    # needs to return everything in same order
    ) -> (
        Key,
        int,
        Decimal,
        Decimal,
        Decimal,
    ):
        """Interprets the adjustments (formatted as a `dict`) specified by the
        `dict` keys and returns the appropriate data to the parsing loop.

        Arguments:
            key {Key} -- The copy of the key data tracked in the parsing loop.
            align {int} -- The alignment option.
            current_rotation {Decimal} -- The current rotation angle.
            current_rotation_x {Decimal} -- The current rotation point on the x
                                          axis.
            current_rotation_y {Decimal} -- The current rotation point on the y
                                          axis.

        Returns:
            tuple -- A tuple of all arguments in the same order without the
                     adjustment item. This is used to overwrite the data
                     tracked in the parsing loop.
        """
        # rotation changes can only be speicfied at beginning of row
        if item.get("r"): key.rotation_angle = Decimal(item["r"])
        if item.get("rx"): key.rotation_x = Decimal(item["rx"])
        if item.get("ry"): key.rotation_y = Decimal(item["ry"])
        # check for resets against rotation rows
        if current_rotation != key.rotation_angle or \
            current_rotation_x != key.rotation_x or \
            current_rotation_y != key.rotation_y:

            if current_rotation_x != key.rotation_x or \
                current_rotation_y != key.rotation_y:
                key.y = key.rotation_y

            current_rotation = key.rotation_angle
            current_rotation_x = key.rotation_x
            current_rotation_y = key.rotation_y
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
            key.text_color = cls.reorder_labels(split, align)
        if item.get("x"): key.x += Decimal(item["x"])
        if item.get("y"): key.y += Decimal(item["y"])
        if item.get("w"):
            key.width = Decimal(item["w"])
            key.width2 = Decimal(item["w"])
        if item.get("h"):
            key.height = Decimal(item["h"])
            key.height2 = Decimal(item["h"])
        if item.get("x2"): key.x2 = Decimal(item["x2"])
        if item.get("y2"): key.y2 = Decimal(item["y2"])
        if item.get("w2"): key.width2 = Decimal(item["width2"])
        if item.get("h2"): key.height2 = Decimal(item["height2"])
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
            current_rotation,
            current_rotation_x,
            current_rotation_y
        )

    @classmethod
    def deserialize(cls, rows: list) -> Keyboard:
        """Reformats the rows of a KLE json to an object of `Keyboard` class
        suitable for simple third-party api usage.

        Arguments:
            rows {list} -- The `list` of `list` or `dict` generated by loading
                           the json.

        Raises:
            DeserializeException: Rows should be a `list`.
            DeserializeException: Rotation changes can only be made at the
                                  beginning of each row.
            DeserializeException: An unexpected item in row (not `dict` or
                                  `list`).
            DeserializeException: Keyboard metadata, a `dict`, can only be
                                  the first element in row.

        Returns:
            Keyboard -- The json data parsed into a object of class `Keyboard`.
        """
        if type(rows) != list:
            raise DeserializeException("Expected an array of objects:", rows)

        # track rotation info for reset x/y positions
        # if rotation_angle != 0, it is always specified LAST
        key = cls.key_class() # readies the next key data when str encountered
        keyboard = Keyboard()
        align = 4

        current_rotation = Decimal(0.0)
        current_rotation_x = Decimal(0.0)
        current_rotation_y = Decimal(0.0)

        for r in range(len(rows)):
            if type(rows[r]) == list:
                for k in range(len(rows[r])):
                    item = rows[r][k]
                    if type(item) == str:
                        # create copy of key data
                        new_key = deepcopy(key, {})

                        # calculate generated values
                        new_key.width2 = key.width if new_key.width2 == 0 else key.width
                        new_key.height2 = key.width if new_key.height2 == 0 else key.height
                        new_key.labels = cls.reorder_labels(item.split("\n"), align)
                        new_key.text_size = cls.reorder_labels(new_key.text_size, align)

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
                        key.x += Decimal(key.width)
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
                            current_rotation,
                            current_rotation_x,
                            current_rotation_y
                        ) = cls.deserialize_adjustment(
                            deepcopy(key, {}),
                            align,
                            current_rotation,
                            current_rotation_x,
                            current_rotation_y,
                            item
                        )

                key.y += Decimal(1.0)
                key.x = Decimal(key.rotation_x)
            elif type(rows[r]) == dict:
                if r != 0:
                    raise DeserializeException(
                        f"Keyboard metadata can only be at index 0, is index {r}:",
                        rows[r]
                    )
                # unpack metadata into keyboard metadata
                metadata = rows[r] # aliased
                keyboard.metadata.author = metadata.get("author")
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

        Arguments:
            s {str} -- The KLE formmatted json `str`.

        Returns:
            Keyboard -- Resulting instance of `Keyboard` from the string.
        """
        return cls.deserialize(json.loads(s))

    # parse from file
    @classmethod
    def load(cls, f: TextIO) -> Keyboard:
        """Converts a KLE formatted json file into a `Keyboard`. NOTE: does not
        close the file.

        Arguments:
            file {TextIO} -- An open `file` with read permissions.

        Returns:
            Keyboard -- Resulting instance of `Keyboard` from the file.
        """
        return cls.deserialize(json.load(f))

    @classmethod
    def dumps(cls, keyboard: Keyboard) -> str:
        """Converts a `Keyboard` into a KLE formatted json `str`.

        Arguments:
            keyboard {Keyboard} -- An instance of `Keyboard` to convert.

        Returns:
            str -- The resulting string from the `Keyboard`.
        """
        pass

    @classmethod
    def dump(cls, keyboard: Keyboard, file: TextIO):
        """Converts a `Keyboard` into a KLE formatted json `str` and writes the
        string into a open file. NOTE: Does not close the file.

        Arguments:
            keyboard {Keyboard} -- An instance of `Keyboard` to dump.
            file {TextIO} -- An open `file` with write permissions.
        """
        file.write(cls.dumps(keyboard))