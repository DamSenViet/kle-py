from __future__ import annotations
from typing import (
    Union,
    List,
)
from typeguard import typechecked
from .label import Label
from .switch import Switch
from .utils import autorepr

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
        self.__switch = Switch()

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
        self.switch = Switch()

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
        """Keycap CSS color.

        :getter: gets keycap CSS color
        :setter: sets keycap CSS color
        :type: str
        """
        return self.__color

    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        self.__color = color

    @property
    def labels(self) -> List[Label]:
        """The 12 labels.

        :getter: gets the 12 labels
        :setter: sets the 12 labels
        :type: List[Label]
        """
        return self.__labels

    @labels.setter
    @typechecked
    def labels(self, labels: List[Label]) -> None:
        self.__labels = labels

    @property
    def default_text_color(self) -> str:
        """Default CSS text color.

        Used to optimize the json size.

        :getter: gets default CSS text color
        :setter: sets default CSS text color
        :type: str
        """
        return self.__default_text_color

    @default_text_color.setter
    @typechecked
    def default_text_color(self, default_text_color: str) -> None:
        self.__default_text_color = default_text_color

    @property
    def default_text_size(self) -> Union[int, float]:
        """Default text size

        Used to optimize the json size.

        :getter: gets default text size
        :setter: sets default text size
        :type: Union[int, float]
        """
        return self.__default_text_size

    @default_text_size.setter
    @typechecked
    def default_text_size(self, default_text_size: Union[int, float]) -> None:
        self.__default_text_size = default_text_size

    @property
    def x(self) -> float:
        """X position of raised primary shape in key units.

        :getter: gets x posiiton of raised primary shape in key units
        :setter: sets x position of raised primary shape in key units
        :type: float
        """
        return self.__x

    @x.setter
    @typechecked
    def x(self, x: float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        """Y position of raised primary shape in key units.

        :getter: gets y position of raised primary shape in key units
        :getter: sets y position of raised primary shape in key units
        :type: float
        """
        return self.__y

    @y.setter
    @typechecked
    def y(self, y: float) -> None:
        self.__y = y

    @property
    def width(self) -> float:
        """Width of raised primary shape in key units.

        :getter: gets width of raised primary shape in key units
        :setter: sets width of raised primary shape in key units
        :type: float
        """
        return self.__width

    @width.setter
    @typechecked
    def width(self, width: float) -> None:
        self.__width = width

    @property
    def height(self) -> float:
        """Height of raised primary shape in key units.

        :getter: gets height of raised primary shape in key units
        :setter: sets height of raised primary shape in key units
        :type: float
        """
        return self.__height

    @height.setter
    @typechecked
    def height(self, height: float) -> None:
        self.__height = height

    @property
    def x2(self) -> float:
        """X position offset of the lowered secondary shape in key units.

        :getter: gets x position offset of the lowered secondary shape in key units
        :setter: sets x position offset of the lowered secondary shape in key units
        :type: float
        """
        return self.__x2

    @x2.setter
    @typechecked
    def x2(self, x2: float) -> None:
        self.__x2 = x2

    @property
    def y2(self) -> float:
        """Y position offset of lowered secondary shape in key units.

        :getter: gets y position offset of lowered secondary shape in key units
        :setter: sets y position offset of lowered secondary shape in key units
        :type: float
        """
        return self.__y2

    @y2.setter
    @typechecked
    def y2(self, y2: float) -> None:
        self.__y2 = y2

    @property
    def width2(self) -> float:
        """Width of lowered secondary shape in key units.

        :getter: gets width of lowered secondary shape in key units
        :setter: sets width of lowered secondary shape in key units
        :type: float
        """
        return self.__width2

    @width2.setter
    @typechecked
    def width2(self, width2: float) -> None:
        self.__width2 = width2

    @property
    def height2(self) -> float:
        """Height of lowered secondary shape in key units.

        :getter: gets height of lowered secondary shape in key units
        :setter: sets height of lowered secondary shape in key units
        :type: float
        """
        return self.__height2

    @height2.setter
    @typechecked
    def height2(self, height2: float) -> None:
        self.__height2 = height2

    @property
    def rotation_x(self) -> float:
        """X position of rotation origin in key units.

        :getter: gets x position of rotation origin in key units
        :setter: sets x position of rotation origin in key units
        :type: float
        """
        return self.__rotation_x

    @rotation_x.setter
    @typechecked
    def rotation_x(self, rotation_x: float) -> None:
        self.__rotation_x = rotation_x

    @property
    def rotation_y(self) -> float:
        """Y position of rotation origin in key units.

        :getter: gets y position of rotation origin in key units
        :setter: sets y position of rotation origin in key units
        :type: float
        """
        return self.__rotation_y

    @rotation_y.setter
    @typechecked
    def rotation_y(self, rotation_y: float) -> None:
        self.__rotation_y = rotation_y

    @property
    def rotation_angle(self) -> float:
        """Rotation angle in degrees.

        :getter: gets rotation angle in degrees
        :setter: sets rotation angle in degrees
        :type: float
        """
        return self.__rotation_angle

    @rotation_angle.setter
    @typechecked
    def rotation_angle(self, rotation_angle: float) -> None:
        self.__rotation_angle = rotation_angle

    @property
    def is_ghosted(self) -> bool:
        """Whether the key is rendered partially transparent.

        :getter: gets whether the key is rendered partially transparent
        :setter: sets whether the key is rendered partially transparent
        :type: bool
        """
        return self.__is_ghosted

    @is_ghosted.setter
    @typechecked
    def is_ghosted(self, is_ghosted: bool) -> None:
        self.__is_ghosted = is_ghosted

    @property
    def is_stepped(self) -> bool:
        """Whether the key is stepped.

        :getter: gets whether the key is stepped
        :setter: sets whether the key is stepped
        :type: bool
        """
        return self.__is_stepped

    @is_stepped.setter
    @typechecked
    def is_stepped(self, is_stepped: bool) -> None:
        self.__is_stepped = is_stepped

    @property
    def is_homing(self) -> bool:
        """Whether the key is a homing key.

        :getter: gets whether the key is a homing key
        :setter: sets whether the key is a homing key
        :type: bool
        """
        return self.__is_homing

    @is_homing.setter
    @typechecked
    def is_homing(self, is_homing: bool) -> None:
        self.__is_homing = is_homing

    @property
    def is_decal(self) -> bool:
        """Whether the key is purely decorative.

        :getter: gets whether the key is purely decorative
        :setter: sets whether the key is purely decorative
        :type: bool
        """
        return self.__is_decal

    @is_decal.setter
    @typechecked
    def is_decal(self, is_decal: bool) -> None:
        self.__is_decal = is_decal

    @property
    def profile_and_row(self) -> str:
        """Keycap profile and row.

        :getter: gets keycap profile and row
        :setter: sets keycap profile and row
        :type: str
        """
        return self.__profile_and_row

    @profile_and_row.setter
    @typechecked
    def profile_and_row(self, profile_and_row: str) -> None:
        self.__profile_and_row = profile_and_row

    @property
    def switch(self) -> Switch:
        """Switch.

        :getter: gets switch
        :setter: sets switch
        :type: Switch
        """
        return self.__switch

    @switch.setter
    @typechecked
    def switch(self, switch: Switch) -> None:
        self.__switch = switch
