import copy
import json
from decimal import Decimal
from typing import (
    Union,
    List,
    Dict,
)


class Key:
    """Class for storing a KLE Key.

    :ivar x: x position of the main shape, defaults to Decimal(0.0)
    :vartype x: Decimal
    :ivar y: y position of the main shape, defaults to Decimal(0.0)
    :vartype y: Decimal
    :ivar width: width of the main shape, defaults to Decimal(1.0)
    :vartype width: Decimal
    :ivar height: height of the main shape, defaults to Decimal(1.0)
    :vartype height: Decimal
    :ivar x2: x position offset of the secondary shape, defaults to Decimal(0.0)
    :vartype x2: Decimal
    :ivar y2: y position offset of the secondary shape, defaults to Decimal(0.0)
    :vartype y2: Decimal
    :ivar width2: width of the secondary shape, defaults to Decimal(1.0)
    :vartype width2: Decimal
    :ivar height2: height of hte secondary shape, defaults to Decimal(1.0)
    :vartype height2: Decimal
    :ivar rotation_x: x position of the origin of rotation, defaults to Decimal(0.0)
    :vartype rotation_x: Decimal
    :ivar rotation_y: y position of the origin of rotation, defaults to Decimal(0.0)
    :vartype rotation_y: Decimal
    :ivar rotation_angle: rotation angle about the origin in degrees, defaults to Decimal(0.0)
    :vartype rotation_angle: Decimal
    :ivar color: fill color, defaults to "#cccccc"
    :vartype color: str
    :ivar text_labels: text labels , defaults to ["" for i in range(12)]
    :vartype text_labels: List[str]
    :ivar text_colors: text colors of the labels, defaults to [None for i in range(12)]
    :vartype text_colors: List[Union[str, None]]
    :ivar text_size: text sizes of the labels, defaults to [None for i in range(12)]
    :vartype text_size: List[Union[int, float, None]]
    :ivar default_text_color: default text color, defaults to "#000000"
    :vartype default_text_color: str
    :ivar default_text_size: default text size, defaults to 3
    :vartype default_text_size: Union[int, float]
    :ivar decal: whether the key is decorative, defaults to False
    :vartype decal: bool
    :ivar ghost: whether the key is invisible, defaults to False
    :vartype ghost: bool
    :ivar stepped: whether the key is stepped, defaults to False
    :vartype stepped: bool
    :ivar nub: whether the key is nubbed, defaults to False
    :vartype nub: bool
    :ivar profile: the profile of the key, defaults to ""
    :vartype profile: str
    :ivar switch_mount: switch mount, defaults to ""
    :vartype switch_mount: str
    :ivar switch_brand: switch brand, defaults to ""
    :vartype switch_brand: str
    :ivar switch_type: switch type, defaults to ""
    :vartype switch_type: str
    """

    def __init__(self):
        self.color = "#cccccc"
        self.text_labels = ["" for i in range(12)]
        self.text_colors = [None for i in range(12)]
        # cannot be 0, either None or positive
        self.text_sizes = [None for i in range(12)]
        self.default_text_color = "#000000"
        self.default_text_size = 3
        self.x = Decimal(0.0)
        self.y = Decimal(0.0)
        self.width = Decimal(1.0)
        self.height = Decimal(1.0)
        self.x2 = Decimal(0.0)
        self.y2 = Decimal(0.0)
        self.width2 = Decimal(1.0)
        self.height2 = Decimal(1.0)
        self.rotation_x = Decimal(0.0)
        self.rotation_y = Decimal(0.0)
        self.rotation_angle = Decimal(0.0)
        self.decal = False
        self.ghost = False
        self.stepped = False
        self.nub = False
        self.profile = ""
        self.switch_mount = ""
        self.switch_brand = ""
        self.switch_type = ""

    def __deepcopy__(self, memo: Dict = None) -> "Key":
        """Creates a deep copy of the key.

        :return: A duplicate of the key.
        :rtype: Key
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.text_labels = copy.deepcopy(self.text_labels, memo)
        new_key.text_colors = copy.deepcopy(self.text_colors, memo)
        new_key.text_sizes = copy.deepcopy(self.text_sizes, memo)
        return new_key

    def __str__(self) -> str:
        d = dict()
        d["color"] = self.color
        d["text_labels"] = self.text_labels
        d["text_colors"] = self.text_colors
        d["text_sizes"] = self.text_sizes
        d["default_text_color"] = self.default_text_color
        d["default_text_size"] = self.default_text_size
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
        d["profile"] = self.profile
        d["nub"] = self.nub
        d["ghost"] = self.ghost
        d["stepped"] = self.stepped
        d["decal"] = self.decal
        d["switch_mount"] = self.switch_mount
        d["switch_brand"] = self.switch_brand
        d["switch_type"] = self.switch_type
        return json.dumps(d)
