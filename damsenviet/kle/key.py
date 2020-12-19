from __future__ import annotations
from typing import (
    Union,
    List,
)
from typeguard import typechecked
from .label import Label
from .switch import Switch
from .utils import (
    autorepr,
    expect,
    is_valid_css_color,
)

__all__ = ["Key"]


class Key:
    """Class storing Key."""

    def __init__(self):
        self.__color: str = "#cccccc"
        self.__labels: List[Label] = [Label() for i in range(12)]
        self.__default_text_color: str = "#000000"
        self.__default_text_size: str = 3
        self.__x: float = 0.0
        self.__y: float = 0.0
        self.__width: float = 1.0
        self.__height: float = 1.0
        self.__x2: float = 0.0
        self.__y2: float = 0.0
        self.__width2: float = 1.0
        self.__height2: float = 1.0
        self.__rotation_x: float = 0.0
        self.__rotation_y: float = 0.0
        self.__rotation_angle: float = 0.0
        self.__is_ghosted: bool = False
        self.__is_stepped: bool = False
        self.__is_homing: bool = False
        self.__is_decal: bool = False
        self.__profile_and_row: str = ""
        self.__switch = Switch("", "", "")

        self.color: str = "#cccccc"
        self.labels: List[Label] = [Label() for i in range(12)]
        self.default_text_color: str = "#000000"
        self.default_text_size: str = 3
        self.x: float = 0.0
        self.y: float = 0.0
        self.width: float = 1.0
        self.height: float = 1.0
        self.x2: float = 0.0
        self.y2: float = 0.0
        self.width2: float = 1.0
        self.height2: float = 1.0
        self.rotation_x: float = 0.0
        self.rotation_y: float = 0.0
        self.rotation_angle: float = 0.0
        self.is_ghosted: bool = False
        self.is_stepped: bool = False
        self.is_homing: bool = False
        self.is_decal: bool = False
        self.profile_and_row: str = ""
        self.switch = Switch("", "", "")

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        attributes = dict()
        attributes["color"] = self.color
        attributes["labels"] = self.labels
        attributes["default_text_color"] = self.default_text_color
        attributes["default_text_size"] = self.default_text_size
        attributes["x"] = self.x
        attributes["y"] = self.y
        attributes["width"] = self.width
        attributes["height"] = self.height
        attributes["x2"] = self.x2
        attributes["y2"] = self.y2
        attributes["width2"] = self.width2
        attributes["height2"] = self.height2
        attributes["rotation_x"] = self.rotation_x
        attributes["rotation_y"] = self.rotation_y
        attributes["rotation_angle"] = self.rotation_angle
        attributes["is_ghosted"] = self.is_ghosted
        attributes["is_stepped"] = self.is_stepped
        attributes["is_homing"] = self.is_homing
        attributes["is_decal"] = self.is_decal
        attributes["profile_and_row"] = self.profile_and_row
        attributes["switch"] = self.switch
        return autorepr(self, attributes)

    @property
    def color(self) -> str:
        """Gets cap css color.

        :return: cap css color
        :rtype: str
        """
        return self.__color

    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        """Sets cap css color.

        :param color: cap css color
        :type color: str
        """
        expect(
            "color",
            color,
            "be a valid css color",
            is_valid_css_color,
        )
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
        """Sets default css text color.

        Used to optimize the json size.

        :param default_text_color: default css text color
        :type default_text_color: str
        """
        expect(
            "default_text_color",
            default_text_color,
            "be a valid css color",
            is_valid_css_color,
        )
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
        expect(
            "default_text_size",
            default_text_size,
            "be at least 1 and no more than 9",
            lambda size: size >= 1 and size <= 9,
        )
        self.__default_text_size = default_text_size

    @property
    def x(self) -> float:
        """Gets x position of raised primary shape.

        :return: x posiiton of raised primary shape
        :rtype: float
        """
        return self.__x

    @x.setter
    @typechecked
    def x(self, x: float) -> None:
        """Sets x position of raised primary shape in key units.

        :param x: x position of raised primary shape in key units
        :type x: float
        """
        self.__x = x

    @property
    def y(self) -> float:
        """Gets y position of raised primary shape in key units.

        :return: y position of raised primary shape in key units
        :rtype: float
        """
        return self.__y

    @y.setter
    @typechecked
    def y(self, y: float) -> None:
        """Sets y position of raised primary shape in key units.

        :param y: y position of raised primary shape in key units
        :type y: float
        """
        self.__y = y

    @property
    def width(self) -> float:
        """Gets width of raised primary shape in key units .

        :return: width of raised primary shape in key units
        :rtype: float
        """
        return self.__width

    @width.setter
    @typechecked
    def width(self, width: float) -> None:
        """Sets width of raised primary shape in key units.

        :param width: width of raised primary shape in key units
        :type width: float
        """
        expect(
            "width",
            width,
            "be at least 0.5",
            lambda width: width >= 0.5,
        )
        self.__width = width

    @property
    def height(self) -> float:
        """Gets height of raised primary shape in key units.

        :return: height of raised primary shape in key units
        :rtype: float
        """
        return self.__height

    @height.setter
    @typechecked
    def height(self, height: float) -> None:
        """Sets height of raised primary shape in key units.

        :param height: height of raised primary shape in key units
        :type height: float
        """
        expect(
            "height",
            height,
            "be at least 0.5",
            lambda height: height >= 0.5,
        )
        self.__height = height

    @property
    def x2(self) -> float:
        """Gets x position offset of the lowered secondary shape in key units.

        :return: x position offset of the lowered secondary shape in key units
        :rtype: float
        """
        return self.__x2

    @x2.setter
    @typechecked
    def x2(self, x2: float) -> None:
        """Sets x position offset of the lowered secondary shape in key units.

        :param x2: x position offset of the lowered secondary shape in key units
        :type x2: float
        """
        expect(
            "abs(x2)",
            abs(x2),
            "be no more than abs(width - width2)",
            lambda x2: abs(x2) <= abs(self.width - self.width2),
        )
        self.__x2 = x2

    @property
    def y2(self) -> float:
        """Gets y position offset of lowered secondary shape in key units.

        :return: y position offset of lowered secondary shape in key units
        :rtype: float
        """
        return self.__y2

    @y2.setter
    @typechecked
    def y2(self, y2: float) -> None:
        """Sets y position offset of lowered secondary shape in key units.

        :param y2: y position offset of lowered secondary shape in key units
        :type y2: float
        """
        expect(
            "abs(y2)",
            abs(y2),
            "be no more than abs(height - height2)",
            lambda y2: abs(y2) <= abs(self.height - self.height2),
        )
        self.__y2 = y2

    @property
    def width2(self) -> float:
        """Gets width of lowered secondary shape in key units.

        :return: width of lowered secondary shape in key units
        :rtype: float
        """
        return self.__width2

    @width2.setter
    @typechecked
    def width2(self, width2: float) -> None:
        """Sets width of lowered secondary shape in key units.

        :param width2: width of lowered secondary shape in key units
        :type width2: float
        """
        expect(
            "width2",
            width2,
            "be at least 0.5",
            lambda width2: width2 >= 0.5,
        )
        expect(
            "width2",
            width2,
            "be at least abs(x2)",
            lambda width2: width2 >= abs(self.x2),
        )
        self.__width2 = width2

    @property
    def height2(self) -> float:
        """Gets height of lowered secondary shape in key units.

        :return: height of lowered secondary shape in key units
        :rtype: float
        """
        return self.__height2

    @height2.setter
    @typechecked
    def height2(self, height2: float) -> None:
        """Sets height of lowered secondary shape in key units.

        :param height2: height of lowered secondary shape in key units
        :type height2: float
        """
        expect(
            "height2",
            height2,
            "be at least 0.5",
            lambda height2: height2 >= 0.5,
        )
        expect(
            "height2",
            height2,
            "be at least abs(y2)",
            lambda height2: height2 >= abs(self.y2),
        )
        self.__height2 = height2

    @property
    def rotation_x(self) -> float:
        """Gets x position of rotation origin in key units.

        :return: x position of rotation origin in key units
        :rtype: float
        """
        return self.__rotation_x

    @rotation_x.setter
    @typechecked
    def rotation_x(self, rotation_x: float) -> None:
        """Sets x position of rotation origin in key units.

        :param rotation_x: x position of rotation origin in key units
        :type rotation_x: float
        """
        expect(
            "rotation_x",
            rotation_x,
            "be at least 0",
            lambda rotation_x: rotation_x >= 0,
        )
        self.__rotation_x = rotation_x

    @property
    def rotation_y(self) -> float:
        """Gets y position of rotation origin in key units.

        :return: y position of rotation origin in key units
        :rtype: float
        """
        return self.__rotation_y

    @rotation_y.setter
    @typechecked
    def rotation_y(self, rotation_y: float) -> None:
        """Sets y position of rotation origin in key units.

        :param rotation_y: y position of rotation origin in key units
        :type rotation_y: float
        """
        expect(
            "rotation_y",
            rotation_y,
            "be at least 0",
            lambda rotation_y: rotation_y >= 0,
        )
        self.__rotation_y = rotation_y

    @property
    def rotation_angle(self) -> float:
        """Gets rotation angle in degrees.

        :return: rotation angle in degrees
        :rtype: float
        """
        return self.__rotation_angle

    @rotation_angle.setter
    @typechecked
    def rotation_angle(self, rotation_angle: float) -> None:
        """Sets rotation angle in degrees.

        :param rotation_angle: rotation angle in degrees
        :type rotation_angle: float
        """
        expect(
            "rotation_angle",
            rotation_angle,
            "be at least -180 and no more than 180",
            lambda rotation_angle: rotation_angle >= -180 and rotation_angle <= 180,
        )
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
    def switch(self) -> Switch:
        """Gets switch.

        :return: switch
        :rtype: Switch
        """
        return self.__switch

    @switch.setter
    @typechecked
    def switch(self, switch: Switch) -> None:
        """Sets switch.

        :param switch: switch
        :type switch: Switch
        """
        self.__switch = switch
