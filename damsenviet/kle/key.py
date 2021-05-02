from __future__ import annotations
from typing import (
    Union,
    List,
)
from .label import Label
from .switch import Switch

__all__ = ["Key"]


class Key:
    """Key information."""

    def __init__(self):
        """Initializes a Key."""
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
        self.__switch: Switch = Switch()

    @property
    def color(self) -> str:
        """Keycap CSS color."""
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    @property
    def labels(self) -> List[Label]:
        """12 Labels.

        Index to position mapping is displayed below.

        .. image:: /_static/label_positions.svg
            :width: 150
            :alt: Label Positions
        """
        return self.__labels

    @labels.setter
    def labels(self, labels: List[Label]) -> None:
        self.__labels = labels

    @property
    def default_text_color(self) -> str:
        """Default CSS text color.

        Only used to optimize the KLE JSON size.
        """
        return self.__default_text_color

    @default_text_color.setter
    def default_text_color(self, default_text_color: str) -> None:
        self.__default_text_color = default_text_color

    @property
    def default_text_size(self) -> Union[int, float]:
        """Default text size.

        Only used to optimize the KLE JSON size.
        """
        return self.__default_text_size

    @default_text_size.setter
    def default_text_size(self, default_text_size: Union[int, float]) -> None:
        self.__default_text_size = default_text_size

    @property
    def x(self) -> float:
        """X position of raised primary shape in key units."""
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        """Y position of raised primary shape in key units."""
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        self.__y = y

    @property
    def width(self) -> float:
        """Width of raised primary shape in key units."""
        return self.__width

    @width.setter
    def width(self, width: float) -> None:
        self.__width = width

    @property
    def height(self) -> float:
        """Height of raised primary shape in key units."""
        return self.__height

    @height.setter
    def height(self, height: float) -> None:
        self.__height = height

    @property
    def x2(self) -> float:
        """X position offset of the lowered secondary shape in key units."""
        return self.__x2

    @x2.setter
    def x2(self, x2: float) -> None:
        self.__x2 = x2

    @property
    def y2(self) -> float:
        """Y position offset of lowered secondary shape in key units."""
        return self.__y2

    @y2.setter
    def y2(self, y2: float) -> None:
        self.__y2 = y2

    @property
    def width2(self) -> float:
        """Width of lowered secondary shape in key units."""
        return self.__width2

    @width2.setter
    def width2(self, width2: float) -> None:
        self.__width2 = width2

    @property
    def height2(self) -> float:
        """Height of lowered secondary shape in key units."""
        return self.__height2

    @height2.setter
    def height2(self, height2: float) -> None:
        self.__height2 = height2

    @property
    def rotation_x(self) -> float:
        """X position of rotation origin in key units."""
        return self.__rotation_x

    @rotation_x.setter
    def rotation_x(self, rotation_x: float) -> None:
        self.__rotation_x = rotation_x

    @property
    def rotation_y(self) -> float:
        """Y position of rotation origin in key units."""
        return self.__rotation_y

    @rotation_y.setter
    def rotation_y(self, rotation_y: float) -> None:
        self.__rotation_y = rotation_y

    @property
    def rotation_angle(self) -> float:
        """Rotation angle in degrees."""
        return self.__rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle: float) -> None:
        self.__rotation_angle = rotation_angle

    @property
    def is_ghosted(self) -> bool:
        """Whether the key is rendered partially transparent."""
        return self.__is_ghosted

    @is_ghosted.setter
    def is_ghosted(self, is_ghosted: bool) -> None:
        self.__is_ghosted = is_ghosted

    @property
    def is_stepped(self) -> bool:
        """Whether the key is stepped."""
        return self.__is_stepped

    @is_stepped.setter
    def is_stepped(self, is_stepped: bool) -> None:
        self.__is_stepped = is_stepped

    @property
    def is_homing(self) -> bool:
        """Whether the key is a homing key."""
        return self.__is_homing

    @is_homing.setter
    def is_homing(self, is_homing: bool) -> None:
        self.__is_homing = is_homing

    @property
    def is_decal(self) -> bool:
        """Whether the key is purely decorative."""
        return self.__is_decal

    @is_decal.setter
    def is_decal(self, is_decal: bool) -> None:
        self.__is_decal = is_decal

    @property
    def profile_and_row(self) -> str:
        """Keycap profile and row."""
        return self.__profile_and_row

    @profile_and_row.setter
    def profile_and_row(self, profile_and_row: str) -> None:
        self.__profile_and_row = profile_and_row

    @property
    def switch(self) -> Switch:
        """Switch information."""
        return self.__switch

    @switch.setter
    def switch(self, switch: Switch) -> None:
        self.__switch = switch
