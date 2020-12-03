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

from typeguard import typechecked

from .label import Label


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
        self.__color = "#cccccc"
        self.__labels = [Label() for i in range(12)]
        self.__default_text_color = "#000000"
        self.__default_text_size = 3
        self.__x = Decimal(0.0)
        self.__y = Decimal(0.0)
        self.__width = Decimal(1.0)
        self.__height = Decimal(1.0)
        self.__x2 = Decimal(0.0)
        self.__y2 = Decimal(0.0)
        self.__width2 = Decimal(1.0)
        self.__height2 = Decimal(1.0)
        self.__rotation_x = Decimal(0.0)
        self.__rotation_y = Decimal(0.0)
        self.__rotation_angle = Decimal(0.0)
        self.__decal = False
        self.__ghosted = False
        self.__stepped = False
        self.__nubbed = False
        self.__profile = ""
        self.__switch_mount = ""
        self.__switch_brand = ""
        self.__switch_type = ""

    def __str__(self):
        d = dict()
        d["color"] = self.get_color()
        d["labels"] = self.get_labels()
        d["default_text_color"] = self.get_default_text_color()
        d["default_text_size"] = self.get_default_text_size()
        d["x"] = float(self.get_x())
        d["y"] = float(self.get_y())
        d["x2"] = float(self.get_x2())
        d["y2"] = float(self.get_y2())
        d["width"] = float(self.get_width())
        d["height"] = float(self.get_height())
        d["width2"] = float(self.get_width2())
        d["height2"] = float(self.get_height2())
        d["rotation_x"] = float(self.get_rotation_x())
        d["rotation_y"] = float(self.get_rotation_y())
        d["rotation_angle"] = float(self.get_rotation_angle())
        d["decal"] = self.get_decal()
        d["profile"] = self.get_profile()
        d["ghosted"] = self.get_ghosted()
        d["stepped"] = self.get_stepped()
        d["nubbed"] = self.get_nubbed()
        d["switch_mount"] = self.get_switch_mount()
        d["switch_brand"] = self.get_switch_brand()
        d["switch_type"] = self.get_switch_type()
        return str(d)

    def __deepcopy__(self, memo: Dict = dict()):
        """Creates a deep copy of the Key.

        :param memo: dictionary of objects already copied
        :type memo: Dict
        :return: deep copy of the Key
        :rtype: Key
        """
        new_key = Key()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.set_labels(deepcopy(self.get_labels(), memo))
        return new_key

    def get_color(self) -> str:
        return self.__color

    @typechecked
    def set_color(self, color: str) -> Key:
        self.__color = color
        return self

    def get_labels(self) -> List[Label]:
        return self.__labels

    @typechecked
    def set_labels(self, labels: List[Label]) -> Key:
        self.__labels = labels
        return self

    def get_default_text_color(self) -> str:
        return self.__default_text_color

    @typechecked
    def set_default_text_color(self, default_text_color: str) -> Key:
        self.__default_text_color = default_text_color
        return self

    def get_default_text_size(self) -> Union[int, float]:
        return self.__default_text_size

    @typechecked
    def set_default_text_size(self, default_text_size: Union[int, float]) -> Key:
        self.__default_text_size = default_text_size
        return self

    def get_x(self) -> Decimal:
        """Gets the x position of the main shape."""
        return self.__x

    @typechecked
    def set_x(self, x: Decimal) -> Key:
        """Sets the x position of the main shape."""
        self.__x = x
        return self

    def get_y(self) -> Decimal:
        """Gets the y position of the main shape."""
        return self.__y

    @typechecked
    def set_y(self, y: Decimal) -> Key:
        """Sets the y position of the main shape."""
        self.__y = y
        return self

    def get_width(self) -> Decimal:
        """Gets the width of the main shape."""
        return self.__width

    @typechecked
    def set_width(self, width: Decimal) -> Key:
        """Sets the width of the main shape."""
        self.__width = width
        return self

    def get_height(self) -> Decimal:
        """Gets the height of the main shape."""
        return self.__height

    @typechecked
    def set_height(self, height: Decimal) -> Key:
        """Sets the height of the main shape."""
        self.__height = height
        return self

    def get_x2(self) -> Decimal:
        return self.__x2

    @typechecked
    def set_x2(self, x2: Decimal) -> Key:
        self.__x2 = x2
        return self

    def get_y2(self) -> Decimal:
        return self.__y2

    @typechecked
    def set_y2(self, y2: Decimal) -> Key:
        self.__y2 = y2
        return self

    def get_width2(self) -> Decimal:
        return self.__width2

    @typechecked
    def set_width2(self, width2: Decimal) -> Key:
        self.__width2 = width2
        return self

    def get_height2(self) -> Decimal:
        return self.__height2

    @typechecked
    def set_height2(self, height2: Decimal) -> Key:
        self.__height2 = height2
        return self

    def get_rotation_x(self) -> Decimal:
        return self.__rotation_x

    @typechecked
    def set_rotation_x(self, rotation_x: Decimal) -> Key:
        self.__rotation_x = rotation_x
        return self

    def get_rotation_y(self) -> Decimal:
        return self.__rotation_y

    @typechecked
    def set_rotation_y(self, rotation_y: Decimal) -> Key:
        self.__rotation_y = rotation_y
        return self

    def get_rotation_angle(self) -> Decimal:
        return self.__rotation_angle

    @typechecked
    def set_rotation_angle(self, rotation_angle: Decimal) -> Key:
        self.__rotation_angle = rotation_angle
        return self

    def get_decal(self) -> bool:
        return self.__decal

    @typechecked
    def set_decal(self, decal: bool) -> Key:
        self.__decal = decal
        return self

    def get_ghosted(self) -> bool:
        return self.__ghosted

    @typechecked
    def set_ghosted(self, ghosted: bool) -> Key:
        self.__ghosted = ghosted
        return self

    def get_stepped(self) -> bool:
        return self.__stepped

    @typechecked
    def set_stepped(self, stepped: bool) -> Key:
        self.__stepped = stepped
        return self

    def get_nubbed(self) -> bool:
        return self.__nubbed

    @typechecked
    def set_nubbed(self, nub: bool) -> Key:
        self.__nubbed = nub
        return self

    def get_profile(self) -> str:
        return self.__profile

    @typechecked
    def set_profile(self, profile: str) -> Key:
        self.__profile = profile
        return self

    def get_switch_mount(self) -> str:
        return self.__switch_mount

    @typechecked
    def set_switch_mount(self, switch_mount: str) -> Key:
        self.__switch_mount = switch_mount
        return self

    def get_switch_brand(self) -> str:
        return self.__switch_brand

    @typechecked
    def set_switch_brand(self, switch_brand: str) -> Key:
        self.__switch_brand = switch_brand
        return self

    def get_switch_type(self) -> str:
        return self.__switch_type

    @typechecked
    def set_switch_type(self, switch_type: str) -> Key:
        self.__switch_type = switch_type
        return self
