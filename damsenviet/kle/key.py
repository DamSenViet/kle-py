from __future__ import annotations
from decimal import Decimal
from typing import (
    Union,
    List,
)
from typeguard import typechecked

from .label import Label


class Key:
    """Class storing Key.
    """

    def __init__(self):
        self.__color: str = "#cccccc"
        self.__labels: List[Label] = [Label() for i in range(12)]
        self.__default_text_color: str = "#000000"
        self.__default_text_size: str = 3
        self.__x: Decimal = Decimal(0.0)
        self.__y: Decimal = Decimal(0.0)
        self.__width: Decimal = Decimal(1.0)
        self.__height: Decimal = Decimal(1.0)
        self.__x2: Decimal = Decimal(0.0)
        self.__y2: Decimal = Decimal(0.0)
        self.__width2: Decimal = Decimal(1.0)
        self.__height2: Decimal = Decimal(1.0)
        self.__rotation_x: Decimal = Decimal(0.0)
        self.__rotation_y: Decimal = Decimal(0.0)
        self.__rotation_angle: Decimal = Decimal(0.0)
        self.__decal: bool = False
        self.__ghosted: bool = False
        self.__stepped: bool = False
        self.__nubbed: bool = False
        self.__profile: str = ""
        self.__switch_mount: str = ""
        self.__switch_brand: str = ""
        self.__switch_type: str = ""

    def __str__(self):
        d = dict()
        d["color"] = self.color
        d["labels"] = self.labels
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
        d["rotation_x"] = float(self.rotation_x)
        d["rotation_y"] = float(self.rotation_y)
        d["rotation_angle"] = float(self.rotation_angle)
        d["decal"] = self.get_decal()
        d["profile"] = self.get_profile()
        d["ghosted"] = self.get_ghosted()
        d["stepped"] = self.get_stepped()
        d["nubbed"] = self.get_nubbed()
        d["switch_mount"] = self.get_switch_mount()
        d["switch_brand"] = self.get_switch_brand()
        d["switch_type"] = self.get_switch_type()
        return str(d)

    @property
    def color(self) -> str:
        """Gets fill color.

        :return: fill color
        :rtype: str
        """
        return self.__color

    @color.setter
    @typechecked
    def color(self, color: str) -> Key:
        """Sets fill color.

        :param color: fill color
        :type color: str
        :return: invoker
        :rtype: Key
        """
        self.__color = color
        return self

    @property
    def labels(self) -> List[Label]:
        """Gets the 12 labels.

        :return: 12 labels
        :rtype: List[Label]
        """
        return self.__labels

    @labels.setter
    @typechecked
    def labels(self, labels: List[Label]) -> Key:
        """Sets the 12 labels.

        :param labels: 12 labels
        :type labels: List[Label]
        :return: invoker
        :rtype: Key
        """
        self.__labels = labels
        return self

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
    def default_text_color(self, default_text_color: str) -> Key:
        """Sets default text color.

        Used to optimize the json size.

        :param default_text_color: default text color
        :type default_text_color: str
        :return: invoker
        :rtype: Key
        """
        self.__default_text_color = default_text_color
        return self

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
    def default_text_size(self, default_text_size: Union[int, float]) -> Key:
        """Sets default text size.

        Used to optimize the json size.

        :param default_text_size: the default text size
        :type default_text_size: Union[int, float]
        :return: invoker
        :rtype: Key
        """
        self.__default_text_size = default_text_size
        return self

    @property
    def x(self) -> Decimal:
        """Gets x position of raised primary shape.

        :return: x posiiton of raised primary shape
        :rtype: Decimal
        """
        return self.__x

    @x.setter
    @typechecked
    def x(self, x: Decimal) -> Key:
        """Sets x position of raised primary shape.

        :param x: x position of raised primary shape
        :type x: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__x = x
        return self

    @property
    def y(self) -> Decimal:
        """Gets y position of raised primary shape

        :return: [description]
        :rtype: Decimal
        """
        return self.__y

    @y.setter
    @typechecked
    def y(self, y: Decimal) -> Key:
        """Sets y position of raised primary shape.

        :param y: y position of raised primary shape
        :type y: Decimal
        """
        self.__y = y
        return self

    @property
    def width(self) -> Decimal:
        """Gets width of raised primary shape.

        :return: width of raised primary shape
        :rtype: Decimal
        """
        return self.__width

    @width.setter
    @typechecked
    def width(self, width: Decimal) -> Key:
        """Sets width of raised primary shape.

        :param width: width of raised primary shape
        :type width: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__width = width
        return self

    @property
    def height(self) -> Decimal:
        """Gets height of raised primary shape.

        :return: height of raised primary shape
        :rtype: Decimal
        """
        return self.__height

    @height.setter
    @typechecked
    def height(self, height: Decimal) -> Key:
        """Sets height of raised primary shape.

        :param height: height of raised primary shape
        :type height: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__height = height
        return self

    @property
    def x2(self) -> Decimal:
        """Gets x position offset of the lowered secondary shape.

        :return: x position offset of the lowered secondary shape
        :rtype: Decimal
        """
        return self.__x2

    @x2.setter
    @typechecked
    def x2(self, x2: Decimal) -> Key:
        """Sets x position offset of the lowered secondary shape.

        :param x2: x position offset of the lowered secondary shape
        :type x2: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__x2 = x2
        return self

    @property
    def y2(self) -> Decimal:
        """Gets y position offset of lowered secondary shape.

        :return: y position offset of lowered secondary shape
        :rtype: Decimal
        """
        return self.__y2

    @y2.setter
    @typechecked
    def y2(self, y2: Decimal) -> Key:
        """Sets y position offset of lowered secondary shape.

        :param y2: y position offset of lowered secondary shape
        :type y2: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__y2 = y2
        return self

    @property
    def width2(self) -> Decimal:
        """Gets width of lowered secondary shape.

        :return: width of lowered secondary shape
        :rtype: Decimal
        """
        return self.__width2

    @width2.setter
    @typechecked
    def width2(self, width2: Decimal) -> Key:
        """Sets width of lowered secondary shape.

        :param width2: width of lowered secondary shape
        :type width2: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__width2 = width2
        return self

    @property
    def height2(self) -> Decimal:
        """Gets height of lowered secondary shape.

        :return: height of lowered secondary shape.
        :rtype: Decimal
        """
        return self.__height2

    @height2.setter
    @typechecked
    def height2(self, height2: Decimal) -> Key:
        """Sets height of lowered secondary shape.

        :param height2: height of lowered secondary shape
        :type height2: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__height2 = height2
        return self

    @property
    def rotation_x(self) -> Decimal:
        """Gets x position of rotation origin.

        :return: x position of rotation origin
        :rtype: Decimal
        """
        return self.__rotation_x

    @rotation_x.setter
    @typechecked
    def rotation_x(self, rotation_x: Decimal) -> Key:
        """Sets x position of rotation origin.

        :param rotation_x: x position of rotation origin
        :type rotation_x: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__rotation_x = rotation_x
        return self

    @property
    def rotation_y(self) -> Decimal:
        """Gets y position of rotation origin

        :return: y position of rotation origin
        :rtype: Decimal
        """
        return self.__rotation_y

    @rotation_y.setter
    @typechecked
    def rotation_y(self, rotation_y: Decimal) -> Key:
        """Sets y position of rotation origin.

        :param rotation_y: y position of rotation origin
        :type rotation_y: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__rotation_y = rotation_y
        return self

    @property
    def rotation_angle(self) -> Decimal:
        """Gets rotation angle in degrees.

        :return: rotation angle in degrees
        :rtype: Decimal
        """
        return self.__rotation_angle

    @rotation_angle.setter
    @typechecked
    def rotation_angle(self, rotation_angle: Decimal) -> Key:
        """Sets rotation angle in degrees.

        :param rotation_angle: rotation angle in degrees
        :type rotation_angle: Decimal
        :return: invoker
        :rtype: Key
        """
        self.__rotation_angle = rotation_angle
        return self

    @property
    def decal(self) -> bool:
        """Gets whether the key is decorative.

        :return: whether the key is decorative
        :rtype: bool
        """
        return self.__decal

    @decal.setter
    @typechecked
    def decal(self, decal: bool) -> Key:
        """Sets whether the key is decorative.

        :param decal: whether the key is decorative
        :type decal: bool
        :return: invoker
        :rtype: Key
        """
        self.__decal = decal
        return self

    @property
    def ghosted(self) -> bool:
        """Gets whether the key is ghosted.

        :return: whether the key is ghosted
        :rtype: bool
        """
        return self.__ghosted

    @ghosted.setter
    @typechecked
    def ghosted(self, ghosted: bool) -> Key:
        """Sets whether the key is ghosted.

        :param ghosted: whether the key is ghosted
        :type ghosted: bool
        :return: invoker
        :rtype: Key
        """
        self.__ghosted = ghosted
        return self

    @property
    def stepped(self) -> bool:
        """Gets whether the key is stepped.

        :return: whether the key is stepped
        :rtype: bool
        """
        return self.__stepped

    @stepped.setter
    @typechecked
    def stepped(self, stepped: bool) -> Key:
        """Sets whether the key is stepepd.

        :param stepped: whether the key is stepped
        :type stepped: bool
        :return: invoker
        :rtype: Key
        """
        self.__stepped = stepped
        return self

    @property
    def nubbed(self) -> bool:
        """Gets whether the keycap is nubbed.

        :return: whether the keycap is nubbed
        :rtype: bool
        """
        return self.__nubbed

    @nubbed.setter
    @typechecked
    def nubbed(self, nub: bool) -> Key:
        """Sets whether the keycap is nubbed.

        :param nub: whether the key is nubbed
        :type nub: bool
        :return: invoker
        :rtype: Key
        """
        self.__nubbed = nub
        return self

    @property
    def profile(self) -> str:
        """Gets keycap profile.

        :return: keycap profile
        :rtype: str
        """
        return self.__profile

    @profile.setter
    @typechecked
    def profile(self, profile: str) -> Key:
        """Sets keycap profile.

        :param profile: keycap profile
        :type profile: str
        :return: invoker
        :rtype: Key
        """
        self.__profile = profile
        return self

    @property
    def switch_mount(self) -> str:
        """Gets switch mount.

        :return: switch mount
        :rtype: str
        """
        return self.__switch_mount

    @switch_mount.setter
    @typechecked
    def switch_mount(self, switch_mount: str) -> Key:
        """Sets switch mount.

        :param switch_mount: switch mount
        :type switch_mount: str
        :return: invoker
        :rtype: Key
        """
        self.__switch_mount = switch_mount
        return self

    @property
    def switch_brand(self) -> str:
        """Gets switch brand.

        :return: switch brand
        :rtype: str
        """
        return self.__switch_brand

    @switch_brand.setter
    @typechecked
    def switch_brand(self, switch_brand: str) -> Key:
        """Sets switch brand.

        :param switch_brand: switch brand
        :type switch_brand: str
        :return: invoker
        :rtype: Key
        """
        self.__switch_brand = switch_brand
        return self

    @property
    def switch_type(self) -> str:
        """Gets switch type.

        :return: switch type
        :rtype: str
        """
        return self.__switch_type

    @switch_type.setter
    @typechecked
    def switch_type(self, switch_type: str) -> Key:
        """Sets switch type.

        :param switch_type: switch type
        :type switch_type: str
        :return: invoker
        :rtype: Key
        """
        self.__switch_type = switch_type
        return self
