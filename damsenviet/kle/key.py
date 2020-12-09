from __future__ import annotations
from decimal import Decimal
from typing import (
    Union,
    List,
)
from typeguard import typechecked

from .label import Label


class Key:
    """Class storing Key."""

    def __init__(self):
        self.color: str = "#cccccc"
        self.labels: List[Label] = [Label() for i in range(12)]
        self.default_text_color: str = "#000000"
        self.default_text_size: str = 3
        self.x: Decimal = Decimal(0.0)
        self.y: Decimal = Decimal(0.0)
        self.width: Decimal = Decimal(1.0)
        self.height: Decimal = Decimal(1.0)
        self.x2: Decimal = Decimal(0.0)
        self.y2: Decimal = Decimal(0.0)
        self.width2: Decimal = Decimal(1.0)
        self.height2: Decimal = Decimal(1.0)
        self.rotation_x: Decimal = Decimal(0.0)
        self.rotation_y: Decimal = Decimal(0.0)
        self.rotation_angle: Decimal = Decimal(0.0)
        self.is_ghosted: bool = False
        self.is_stepped: bool = False
        self.is_homing: bool = False
        self.is_decal: bool = False
        self.profile_and_row: str = ""
        self.switch_mount: str = ""
        self.switch_brand: str = ""
        self.switch_type: str = ""

    def __str__(self) -> str:
        d = dict()
        d["color"] = self.color
        d["labels"] = self.labels
        d["default_text_color"] = self.default_text_color
        d["default_text_size"] = self.default_text_size
        d["x"] = float(self.x)
        d["y"] = float(self.y)
        d["width"] = float(self.width)
        d["height"] = float(self.height)
        d["x2"] = float(self.x2)
        d["y2"] = float(self.y2)
        d["width2"] = float(self.width2)
        d["height2"] = float(self.height2)
        d["rotation_x"] = float(self.rotation_x)
        d["rotation_y"] = float(self.rotation_y)
        d["rotation_angle"] = float(self.rotation_angle)
        d["is_ghosted"] = self.is_ghosted
        d["is_stepped"] = self.is_stepped
        d["is_homing"] = self.is_homing
        d["is_decal"] = self.is_decal
        d["profile_and_row"] = self.profile_and_row
        d["switch_mount"] = self.switch_mount
        d["switch_brand"] = self.switch_brand
        d["switch_type"] = self.switch_type
        return str(d)

    def __repr__(self) -> str:
        d = dict()
        d["color"] = self.color
        d["labels"] = self.labels
        d["default_text_color"] = self.default_text_color
        d["default_text_size"] = self.default_text_size
        d["x"] = float(self.x)
        d["y"] = float(self.y)
        d["width"] = float(self.width)
        d["height"] = float(self.height)
        d["x2"] = float(self.x2)
        d["y2"] = float(self.y2)
        d["width2"] = float(self.width2)
        d["height2"] = float(self.height2)
        d["rotation_x"] = float(self.rotation_x)
        d["rotation_y"] = float(self.rotation_y)
        d["rotation_angle"] = float(self.rotation_angle)
        d["is_ghosted"] = self.is_ghosted
        d["is_stepped"] = self.is_stepped
        d["is_homing"] = self.is_homing
        d["is_decal"] = self.is_decal
        d["profile_and_row"] = self.profile_and_row
        d["switch_mount"] = self.switch_mount
        d["switch_brand"] = self.switch_brand
        d["switch_type"] = self.switch_type
        return f"Key(**{repr(d)})"

    @property
    def color(self) -> str:
        """Gets fill color.

        :return: fill color
        :rtype: str
        """
        return self.__color

    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        """Sets fill color.

        :param color: fill color
        :type color: str
        """
        self.__color = color

    @property
    def labels(self) -> List[Label]:
        """Gets the 12 labels.

        :return: 12 labels
        :rtype: List[Label]
        """
        return self.__labels

    @labels.setter
    @typechecked
    def labels(self, labels: List[Label]) -> None:
        """Sets the 12 labels.

        :param labels: 12 labels
        :type labels: List[Label]
        """
        self.__labels = labels

    @property
    def default_text_color(self) -> str:
        """Gets default text color.

        Used to optimize the json size.

        :return: default text color
        :rtype: str
        """
        return self.__default_text_color

    @default_text_color.setter
    @typechecked
    def default_text_color(self, default_text_color: str) -> None:
        """Sets default text color.

        Used to optimize the json size.

        :param default_text_color: default text color
        :type default_text_color: str
        """
        self.__default_text_color = default_text_color

    @property
    def default_text_size(self) -> Union[int, float]:
        """Sets default text size

        Used to optimize the json size.

        :return: default text size
        :rtype: Union[int, float]
        """
        return self.__default_text_size

    @default_text_size.setter
    @typechecked
    def default_text_size(self, default_text_size: Union[int, float]) -> None:
        """Sets default text size.

        Used to optimize the json size.

        :param default_text_size: the default text size
        :type default_text_size: Union[int, float]
        """
        self.__default_text_size = default_text_size

    @property
    def x(self) -> Decimal:
        """Gets x position of raised primary shape.

        :return: x posiiton of raised primary shape
        :rtype: Decimal
        """
        return self.__x

    @x.setter
    @typechecked
    def x(self, x: Decimal) -> None:
        """Sets x position of raised primary shape in key units.

        :param x: x position of raised primary shape in key units
        :type x: Decimal
        """
        self.__x = x

    @property
    def y(self) -> Decimal:
        """Gets y position of raised primary shape in key units.

        :return: y position of raised primary shape in key units
        :rtype: Decimal
        """
        return self.__y

    @y.setter
    @typechecked
    def y(self, y: Decimal) -> None:
        """Sets y position of raised primary shape in key units.

        :param y: y position of raised primary shape in key units
        :type y: Decimal
        """
        self.__y = y

    @property
    def width(self) -> Decimal:
        """Gets width of raised primary shape in key units .

        :return: width of raised primary shape in key units
        :rtype: Decimal
        """
        return self.__width

    @width.setter
    @typechecked
    def width(self, width: Decimal) -> None:
        """Sets width of raised primary shape in key units.

        :param width: width of raised primary shape in key units
        :type width: Decimal
        """
        self.__width = width

    @property
    def height(self) -> Decimal:
        """Gets height of raised primary shape in key units.

        :return: height of raised primary shape in key units
        :rtype: Decimal
        """
        return self.__height

    @height.setter
    @typechecked
    def height(self, height: Decimal) -> None:
        """Sets height of raised primary shape in key units.

        :param height: height of raised primary shape in key units
        :type height: Decimal
        """
        self.__height = height

    @property
    def x2(self) -> Decimal:
        """Gets x position offset of the lowered secondary shape in key units.

        :return: x position offset of the lowered secondary shape in key units
        :rtype: Decimal
        """
        return self.__x2

    @x2.setter
    @typechecked
    def x2(self, x2: Decimal) -> None:
        """Sets x position offset of the lowered secondary shape in key units.

        :param x2: x position offset of the lowered secondary shape in key units
        :type x2: Decimal
        """
        self.__x2 = x2

    @property
    def y2(self) -> Decimal:
        """Gets y position offset of lowered secondary shape in key units.

        :return: y position offset of lowered secondary shape in key units
        :rtype: Decimal
        """
        return self.__y2

    @y2.setter
    @typechecked
    def y2(self, y2: Decimal) -> None:
        """Sets y position offset of lowered secondary shape in key units.

        :param y2: y position offset of lowered secondary shape in key units
        :type y2: Decimal
        """
        self.__y2 = y2

    @property
    def width2(self) -> Decimal:
        """Gets width of lowered secondary shape in key units.

        :return: width of lowered secondary shape in key units
        :rtype: Decimal
        """
        return self.__width2

    @width2.setter
    @typechecked
    def width2(self, width2: Decimal) -> None:
        """Sets width of lowered secondary shape in key units.

        :param width2: width of lowered secondary shape in key units
        :type width2: Decimal
        """
        self.__width2 = width2

    @property
    def height2(self) -> Decimal:
        """Gets height of lowered secondary shape in key units.

        :return: height of lowered secondary shape in key units
        :rtype: Decimal
        """
        return self.__height2

    @height2.setter
    @typechecked
    def height2(self, height2: Decimal) -> None:
        """Sets height of lowered secondary shape in key units.

        :param height2: height of lowered secondary shape in key units
        :type height2: Decimal
        """
        self.__height2 = height2

    @property
    def rotation_x(self) -> Decimal:
        """Gets x position of rotation origin in key units.

        :return: x position of rotation origin in key units
        :rtype: Decimal
        """
        return self.__rotation_x

    @rotation_x.setter
    @typechecked
    def rotation_x(self, rotation_x: Decimal) -> None:
        """Sets x position of rotation origin in key units.

        :param rotation_x: x position of rotation origin in key units
        :type rotation_x: Decimal
        """
        self.__rotation_x = rotation_x

    @property
    def rotation_y(self) -> Decimal:
        """Gets y position of rotation origin in key units.

        :return: y position of rotation origin in key units
        :rtype: Decimal
        """
        return self.__rotation_y

    @rotation_y.setter
    @typechecked
    def rotation_y(self, rotation_y: Decimal) -> None:
        """Sets y position of rotation origin in key units.

        :param rotation_y: y position of rotation origin in key units
        :type rotation_y: Decimal
        """
        self.__rotation_y = rotation_y

    @property
    def rotation_angle(self) -> Decimal:
        """Gets rotation angle in degrees.

        :return: rotation angle in degrees
        :rtype: Decimal
        """
        return self.__rotation_angle

    @rotation_angle.setter
    @typechecked
    def rotation_angle(self, rotation_angle: Decimal) -> None:
        """Sets rotation angle in degrees.

        :param rotation_angle: rotation angle in degrees
        :type rotation_angle: Decimal
        """
        self.__rotation_angle = rotation_angle

    @property
    def is_ghosted(self) -> bool:
        """Gets whether the key is rendered partially transparent.

        :return: whether the key is rendered partially transparent
        :rtype: bool
        """
        return self.__is_ghosted

    @is_ghosted.setter
    @typechecked
    def is_ghosted(self, is_ghosted: bool) -> None:
        """Sets whether the key is rendered partially transparent.

        :param is_ghosted: whether the key is rendered partially transparent
        :type is_ghosted: bool
        """
        self.__is_ghosted = is_ghosted

    @property
    def is_stepped(self) -> bool:
        """Gets whether the key is stepped.

        :return: whether the key is stepped
        :rtype: bool
        """
        return self.__is_stepped

    @is_stepped.setter
    @typechecked
    def is_stepped(self, is_stepped: bool) -> None:
        """Sets whether the key is stepepd.

        In kle this typically decrements keys by 0.5 or 0.25, but kle doesn't normalize.
        the mismatch if it occurs, and therefore can be set without side effects.

        :param is_stepped: whether the key is stepped
        :type is_stepped: bool
        """
        self.__is_stepped = is_stepped

    @property
    def is_homing(self) -> bool:
        """Gets whether the key is a homing key.

        :return: whether the key is a homing key
        :rtype: bool
        """
        return self.__is_homing

    @is_homing.setter
    @typechecked
    def is_homing(self, is_homing: bool) -> None:
        """Sets whether the keycap is a homing key.

        :param is_homing: whether the key is a homing key
        :type is_homing: bool
        """
        self.__is_homing = is_homing

    @property
    def is_decal(self) -> bool:
        """Gets whether the key is purely decorative.

        :return: whether the key is purely decorative
        :rtype: bool
        """
        return self.__is_decal

    @is_decal.setter
    @typechecked
    def is_decal(self, is_decal: bool) -> None:
        """Sets whether the key is purely decorative.

        In KLE this typically disables is_ghosted, stepped, homing but doesn't normalize.
        the mismatch if it occurs, and therefore can be set without side effects.

        :param is_decal: whether the key is purely decorative
        :type is_decal: bool
        """
        self.__is_decal = is_decal

    @property
    def profile_and_row(self) -> str:
        """Gets keycap profile and row.

        e.g. "DCS R1"

        :return: keycap profile and row
        :rtype: str
        """
        return self.__profile_and_row

    @profile_and_row.setter
    @typechecked
    def profile_and_row(self, profile_and_row: str) -> None:
        """Sets keycap profile and row.

        :param profile_and_row: keycap profile and row
        :type profile_and_row_and_row: str
        """
        self.__profile_and_row = profile_and_row

    @property
    def switch_mount(self) -> str:
        """Gets switch mounting type.

        e.g. "CherryMX", "Alps", etc (based on pin cutouts).

        :return: switch mount type
        :rtype: str
        """
        return self.__switch_mount

    @switch_mount.setter
    @typechecked
    def switch_mount(self, switch_mount: str) -> None:
        """Sets switch mount type.

        :param switch_mount: switch mount type
        :type switch_mount: str
        """
        self.__switch_mount = switch_mount

    @property
    def switch_brand(self) -> str:
        """Gets switch brand.

        :return: switch brand
        :rtype: str
        """
        return self.__switch_brand

    @switch_brand.setter
    @typechecked
    def switch_brand(self, switch_brand: str) -> None:
        """Sets switch brand.

        :param switch_brand: switch brand
        :type switch_brand: str
        """
        self.__switch_brand = switch_brand

    @property
    def switch_type(self) -> str:
        """Gets switch type.

        :return: switch type
        :rtype: str
        """
        return self.__switch_type

    @switch_type.setter
    @typechecked
    def switch_type(self, switch_type: str) -> None:
        """Sets switch type.

        :param switch_type: switch type
        :type switch_type: str
        """
        self.__switch_type = switch_type
