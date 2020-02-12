from typing import TextIO
from collections import OrderedDict
from copy import deepcopy
import json

from .key import Key
from .metadata import Metadata, Background
from .keyboard import Keyboard

class DeserializeException(Exception):
    def __init__(self, message: str, payload: dict = None) -> None:
        super().__init__(message + ("\n" + json.dumps(payload) if payload else ""))

class KLE:
    """A class for serializing and deserializing a KLE formatted json."""
    # default Key, use this variable to allow for easy extensions
    key_class = Key

    labelMap = [
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
    def reorderLabelsIn(cls, labels: list, align: int) -> list:
        """Reorders the items in the labels to properly match.

        Arguments:
            labels {list} -- Labels to be reordered.
            align {int} -- The alignment option.

        Returns:
            list -- The reordered labels.
        """
        ret = [None for i in range(12)]
        for i, label in enumerate(labels):
            if label: ret[cls.labelMap[align][i]] = label
        return ret

    @classmethod
    def deserialize_adjustment(
        cls,
        key: Key,
        align: int,
        current_rotation: float,
        current_rotation_x: float,
        current_rotation_y: float,
        item: dict,
    # needs to return everything in same order
    ) -> (
        Key,
        int,
        float,
        float,
        float,
    ):
        """Interprets the adjustments (formatted as a `dict`) specified by the
        `dict` keys and returns the appropriate data to the parsing loop.

        Arguments:
            key {Key} -- The copy of the key data tracked in the parsing loop.
            align {int} -- The alignment option.
            current_rotation {float} -- The current rotation angle.
            current_rotation_x {float} -- The current rotation point on the x
                                          axis.
            current_rotation_y {float} -- The current rotation point on the y
                                          axis.

        Returns:
            tuple -- A tuple of all arguments in the same order without the
                     adjustment item. This is used to overwrite the data
                     tracked in the parsing loop.
        """
        # rotation changes can only be speicfied at beginning of row
        if item.get("r"): key.rotation_angle = item["r"]
        if item.get("rx"): key.rotation_x = item["rx"]
        if item.get("ry"): key.rotation_y = item["ry"]
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
            key.textSize = [None for i in range(12)]
            key.textColor = [None for i in range(12)]
        if item.get("f2"):
            for i in range(12):
                key.textSize[i] = item["f2"]
        if item.get("fa"): key.textSize = item["fa"]
        if item.get("p"): key.profile = item["p"]
        if item.get("c"): key.color = item["c"]
        if item.get("t"):
            split = item["t"].split("\n")
            if len(split[0]) == 0: key.default["textColor"] = split[0]
            key.textColor = cls.reorderLabelsIn(split, align)
        if item.get("x"): key.x += item["x"]
        if item.get("y"): key.y += item["y"]
        if item.get("w"):
            key.width = item["w"]
            key.width2 = item["w"]
        if item.get("h"):
            key.height = item["h"]
            key.height2 = item["h"]
        if item.get("x2"): key.x2 = item["x2"]
        if item.get("y2"): key.y2 = item["y2"]
        if item.get("w2"): key.width2 = item["width2"]
        if item.get("h2"): key.height2 = item["height2"]
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

        current_rotation = 0.0
        current_rotation_x = 0.0
        current_rotation_y = 0.0

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
                        new_key.labels = cls.reorderLabelsIn(item.split("\n"), align)
                        new_key.textSize = cls.reorderLabelsIn(new_key.textSize, align)

                        # clean up generated data
                        for i in range(12):
                            if not new_key.labels[i]:
                                new_key.textSize[i] = None
                                new_key.textColor[i] = None
                            if new_key.textSize[i] == new_key.default["textSize"]:
                                new_key.textSize[i] = None
                            if new_key.textColor[i] == new_key.default["textColor"]:
                                new_key.textColor = None

                        # add key
                        keyboard.keys.append(new_key)

                        # adjustments for next key gen
                        key.x += key.width
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

                key.y += 1
                key.x = key.rotation_x
            elif type(rows[r]) == dict:
                if r != 0:
                    raise DeserializeException(
                        "Keyboard metadata must be the first element:",
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
                keyboard.metadata.switchBrand = metadata.get("switchBrand")
                keyboard.metadata.switchMount = metadata.get("switchMount")
                keyboard.metadata.switchType = metadata.get("switchType")
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
            s {str} -- The KLE formmatted json string.

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
        """Converts a `Keyboard` into a KLE formatted json `str` and dumps the
        string into a open file. NOTE: Does not close the file.

        Arguments:
            keyboard {Keyboard} -- An instance of `Keyboard` to dump.
            file {TextIO} -- An open `file` with write permissions.
        """
        file.write(cls.dumps(keyboard))