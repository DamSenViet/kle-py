import copy
from decimal import Decimal
import json
from typing import List, Dict

class Key:
    """Class that holds data of a `Key` instance for a `Keyboard`."""

    def __init__(
        self,
        color: str = "#cccccc",
        labels: List = None,
        text_color: List = None,
        text_size: List = None,
        default: Dict = None,
        x: Decimal = Decimal(0.0),
        y: Decimal = Decimal(0.0),
        width: Decimal = Decimal(1.0),
        height: Decimal = Decimal(1.0),
        x2: Decimal  = Decimal(0.0),
        y2: Decimal = Decimal(0.0),
        width2: Decimal = Decimal(1.0),
        height2: Decimal = Decimal(1.0),
        rotation_x: Decimal = Decimal(0.0),
        rotation_y: Decimal = Decimal(0.0),
        rotation_angle: Decimal = Decimal(0.0),
        decal: bool = False,
        ghost: bool = False,
        stepped: bool = False,
        nub: bool = False,
        profile: str = "",
        sm: str = "",
        sb: str = "",
        st: str = ""
    ):
        """Construct a new `Key`. Default arguments provided.

        :param color: The background color (hex code) of the key, defaults to
            "#cccccc".
        :type color: str
        :param labels: The list of legends, defaults to
            [None for i in range(12)].
        :type labels: list
        :param text_color: The text color (hex code) for the legends, defaults
            to [None for i in range(12)].
        :type text_color: list
        :param text_size: The text size for the legends, defaults to
            [None for i in range(12)].
        :type text_size: list
        :param default: The defaults used when label in default position,
            defaults to {"text_color": "#000000", "text_size": 3}.
        :type default: dict
        :param x: The x coordinate of the key before rotation.
        :type x: Decimal
        :param y: The y coordinate of the key before rotation.
        :type y: Decimal
        :param width: Width of the key.
        :type width: Decimal
        :param height: Height of the key.
        :type height: Decimal
        :param x2: Duplicate x coordinate of the key???
        :type x2: Decimal
        :param y2: Duplicate y coordinate of the key???
        :type y2: Decimal
        :param width2: Duplicate width of the key???
        :type width2: Decimal
        :param height2: Duplicate height of the key???
        :type height2: Decimal
        :param rotation_x: X coordinate of the rotation origin.
        :type rotation_x: Decimal
        :param rotation_y: Y coordinate of the rotation origin.
        :type rotation_y: Decimal
        :param rotation_angle: Rotation angle about the rotation origin.
        :type rotation_angle: Decimal
        :param decal: Specifies whether key is treated as a decoration.
        :type decal: bool
        :param ghost: Specifies whether key should be rendered transparently.
        :type ghost: bool
        :param stepped: Specifies whether part of key is lower than rest.
        :type stepped: bool
        :param nub: Specifies whether key is a homing key.
        :type nub: bool
        :param profile: The profile/sculpt of the key.
        :type profile: str
        :param sm: The switch mount of the key.
        :type sm: str
        :param sb: The switch brand of the key.
        :type sb: str
        :param st: The switch mount of the key.
        :type st: str
        """
        self.color = color
        self.labels = [None for i in range(12)]
        if labels is not None:
            self.labels = labels
        self.text_color = [None for i in range(12)]
        if text_color is not None:
            self.text_color = text_color
        self.text_size = [None for i in range(12)]
        if text_size is not None:
            self.text_size = text_size
        self.default = {
            "text_color": "#000000",
            "text_size": 3
        }
        if default is not None:
            self.default = default
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x2
        self.y2 = y2
        self.width2 = width2
        self.height2 = height2
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_angle = rotation_angle
        self.decal = decal
        self.ghost = ghost
        self.stepped = stepped
        self.nub = nub
        self.profile = profile
        self.sm = sm
        self.sb = sb
        self.st = st

    def __deepcopy__(self, memo: dict = None) -> "Key":
        """Creates a deep copy of the key.

        :return: A duplicate of the key.
        :rtype: Key
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.labels = copy.deepcopy(self.labels, memo)
        new_key.text_color = copy.deepcopy(self.text_color, memo)
        new_key.text_size = copy.deepcopy(self.text_size, memo)
        new_key.default = copy.deepcopy(self.default, memo)
        return new_key

    def __str__(self) -> str:
        d = dict()
        d["x"] = float(self.x)
        d["y"] = float(self.y)
        d["x2"] = float(self.x2)
        d["y2"] = float(self.y2)
        d["width"] = float(self.width)
        d["height"] = float(self.height)
        d["width2"] = float(self.width2)
        d["height2"] = float(self.height2)
        d["rotation_angle"] = float(self.rotation_angle)
        d["rotation_x"] = float(self.rotation_x)
        d["rotation_y"] = float(self.rotation_y)
        d["labels"] = self.labels
        d["text_color"] = self.text_color
        d["text_size"] = self.text_size
        d["default"] = self.default
        d["color"] = self.color
        d["profile"] = self.profile
        d["nub"] = self.nub
        d["ghost"] = self.ghost
        d["stepped"] = self.stepped
        d["decal"] = self.decal
        d["sm"] = self.sm
        d["sb"] = self.sb
        d["st"] = self.st
        return json.dumps(d, indent=4)