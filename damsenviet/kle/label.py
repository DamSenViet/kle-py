from __future__ import annotations
from typing import Union
from typeguard import typechecked
from .utils import (
    autorepr,
    expect,
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
        """Gets text content.

        :return: text content
        :rtype: str
        """
        return self.__text

    @text.setter
    @typechecked
    def text(self, text: str) -> None:
        """Sets text content.

        :param text: text content
        :type text: str
        """
        self.__text = text

    @property
    def color(self) -> str:
        """Gets css font color.

        :return: css font color
        :rtype: str
        """
        return self.__color

    # any valid css color str value
    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        """Sets css font color.

        :param color: css font color
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
    def size(self) -> Union[int, float]:
        """Gets font size scale.

        :return: font size scale
        :rtype: Union[int, float]
        """
        return self.__size

    @size.setter
    @typechecked
    def size(self, size: Union[int, float]) -> None:
        """Sets font size scale.

        :param size: font size scale
        :type size: Union[int, float]
        """
        # KLE can't enforce invariants when loading
        # but this is true assuming no breach of contract
        expect(
            "size",
            size,
            "at least 1 and no more than 9",
            lambda size: size >= 1 and size <= 9,
        )
        self.__size = size
