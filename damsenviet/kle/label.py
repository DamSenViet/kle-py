from __future__ import annotations
from typing import Union
from typeguard import typechecked
from .utils import (
    autorepr,
    expected,
    is_valid_css_color,
)

__all__ = ["Label"]


class Label:
    """Class storing Key's Label."""

    def __init__(
        self,
        text: str = "",
        color: str = "#000000",
        size: Union[int, float] = 3,
    ):
        """Instantiates a Label."""
        self.text: str = text
        self.color: str = color
        self.size: Union[int, float] = size

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return autorepr(
            self,
            {
                "text": self.text,
                "color": self.color,
                "size": self.size,
            },
        )

    @property
    def text(self) -> str:
        """Text content.

        :getter: gets text content
        :setter: sets text content
        :type: str
        """
        return self.__text

    @text.setter
    @typechecked
    def text(self, text: str) -> None:
        self.__text = text

    @property
    def color(self) -> str:
        """CSS font color.

        :getter: gets CSS font color
        :setter: sets CSS font color
        :type: str
        """
        return self.__color

    # any valid css color str value
    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        expected(
            "color",
            color,
            "be a valid css color",
            is_valid_css_color,
        )
        self.__color = color

    @property
    def size(self) -> Union[int, float]:
        """Font size scale.

        :getter: gets font size scale
        :setter: sets font size scale
        :type: Union[int, float]
        """
        return self.__size

    @size.setter
    @typechecked
    def size(self, size: Union[int, float]) -> None:
        expected(
            "size",
            size,
            "at least 1 and no more than 9",
            lambda size: size >= 1 and size <= 9,
        )
        self.__size = size
