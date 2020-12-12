from __future__ import annotations
from typing import Union
from typeguard import typechecked


class Label:
    """Class storing Key's Label."""

    def __init__(self):
        """Instantiates a Label."""
        self.text: str = ""
        self.color: str = "#000000"
        self.size: Union[int, float] = 3

    def __str__(self):
        d = dict()
        d["text"] = self.__text
        d["color"] = self.__color
        d["size"] = self.__size
        return str(d)

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
        """Gets font color.

        :return: font color
        :rtype: str
        """
        return self.__color

    # any valid css color str value
    @color.setter
    @typechecked
    def color(self, color: str) -> None:
        """Sets font color.

        :param color: font color
        :type color: str
        """
        # KLE can't enforce invariants when loading
        # but this is true assuming no breach of contract
        # if color == "":
        #     raise TypeError("cannot be empty")
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
        # if size < 0.5:
        #     raise TypeError("not at least 0.5")
        self.__size = size
