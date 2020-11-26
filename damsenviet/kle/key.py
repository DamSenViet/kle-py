from __future__ import annotations
from copy import (
    deepcopy,
)
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
    :ivar text_colors: text colors of the labels, defaults to ["" for i in range(12)]
    :vartype text_colors: List[str]
    :ivar text_size: text sizes of the labels, defaults to [0 for i in range(12)]
    :vartype text_size: List[Union[int, float]
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
    :ivar nub: whether the key has a nub, defaults to False
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
        self.text_colors = ["" for i in range(12)]
        # cannot be 0, either None or positive
        self.text_sizes = [0 for i in range(12)]
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

    def __str__(self):
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

    def __deepcopy__(self, memo: Dict = dict()):
        """Creates a deep copy of the Key.

        :param memo: dictionary of objects already copied
        :type memo: Dict
        :return: deep copy of the Key
        :rtype: Key
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.text_labels = deepcopy(self.text_labels, memo)
        new_key.text_colors = deepcopy(self.text_colors, memo)
        new_key.text_sizes = deepcopy(self.text_sizes, memo)
        return new_key

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str) -> Key:
        return self

    def get_text_labels(self) -> List[str]:
        return deepcopy(self.text_labels)

    def set_text_labels(self, text_labels: List[str]) -> Key:
        return self

    def get_text_colors(self) -> List[str]:
        return deepcopy(self.text_colors)

    def set_text_colors(self, text_colors: List[str]) -> Key:
        return self.text_colors

    def get_text_sizes(self) -> List[Union[int, float]]:
        return deepcopy(self.text_sizes)

    def set_text_sizes(self, text_sizes: List[Union[int, float]]) -> Key:
        return self

    def get_default_text_color(self) -> str:
        return self.default_text_color

    def set_default_text_color(self, default_text_color: str) -> Key:
        return self

    def get_default_text_size(self) -> Union[int, float]:
        return self.default_text_size

    def set_default_text_size(self, default_text_size: Union[int, float]) -> Key:
        return self

    def get_x(self) -> Decimal:
        return self.x

    def set_x(self, x: Decimal) -> Key:
        return self

    def get_y(self) -> Decimal:
        return self.y

    def set_y(self, y: Decimal) -> Key:
        return self

    def get_width(self) -> Decimal:
        return self.width

    def set_width(self, width: Decimal) -> Key:
        return self

    def get_height(self) -> Decimal:
        return self.height

    def set_height(self, height: Decimal) -> Key:
        return self

    def get_x2(self) -> Decimal:
        return self.x2

    def set_x2(self, x2: Decimal) -> Key:
        return self

    def get_y2(self) -> Decimal:
        return self.y2

    def set_y2(self, y2: Decimal) -> Key:
        return self

    def get_width2(self) -> Decimal:
        return self.width2

    def set_width2(self, width2: Decimal) -> Key:
        return self

    def get_height2(self) -> Decimal:
        return self.height2

    def set_height2(self, height2: Decimal) -> Key:
        return self

    def get_rotation_x(self) -> Decimal:
        return self.rotation_x

    def set_rotation_x(self, rotation_x: Decimal) -> Key:
        return self

    def get_rotation_y(self) -> Decimal:
        return self.rotation_y

    def set_rotation_y(self, rotation_y: Decimal) -> Key:
        return self

    def get_rotation_angle(self) -> Decimal:
        return self.rotation_angle

    def set_rotation_angle(self, rotation_angle: Decimal) -> Key:
        return self

    def get_decal(self) -> bool:
        pass

    def set_decal(self, decal: bool) -> Key:
        pass

    def get_ghost(self) -> bool:
        pass

    def set_ghost(self, ghost: bool) -> Key:
        pass

    def get_stepped(self) -> bool:
        pass

    def set_stepped(self, stepped: bool) -> Key:
        pass

    def get_nub(self) -> bool:
        pass

    def set_nub(self, nub: bool) -> Key:
        pass

    def get_profile(self) -> str:
        pass

    def set_profile(self, profile: str) -> Key:
        pass

    def get_switch_mount(self) -> str:
        pass

    def set_switch_mount(self, switch_mount: str) -> Key:
        return self

    def get_switch_brand(self) -> str:
        pass

    def set_switch_brand(self, switch_brand: str) -> Key:
        return self

    def get_switch_type(self) -> str:
        pass

    def set_switch_type(self, switch_type: str) -> Key:
        return self
