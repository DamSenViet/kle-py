from __future__ import annotations
from typing import Union
from typeguard import typechecked
from .utils import autorepr

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
        """CSS text color.

        :getter: gets CSS text color
        :setter: sets CSS tex color
        :type: strt
        """
        return self.__color

    # any valid css color str value
    @color.setter
    @typechecked
    def color(self, color: str) -> None:
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
        self.__size = size
