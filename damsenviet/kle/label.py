from __future__ import annotations
from typing import Union
from typeguard import typechecked


class Label:
    """Class storing Key's Label.
    """

    def __init__(self):
        """Instantiates a Label.
        """
        self.__text: str = ""
        self.__color: str = ""
        self.__size: Union[int, float] = 0

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
    def text(self, text: str) -> Label:
        """Sets text content.

        :param text: text content
        :type text: str
        :return: invoker
        :rtype: Label
        """
        self.__text = text
        return self

    @property
    def color(self) -> str:
        """Gets font color.

        :return: font color
        :rtype: str
        """
        return self.__color

    @color.setter
    @typechecked
    def color(self, color: str) -> Label:
        """Sets font color.

        :param color: font color
        :type color: str
        :return: invoker
        :rtype: Label
        """
        self.__color = color
        return self

    @property
    def size(self) -> Union[int, float]:
        """Gets font size.

        :return: font size
        :rtype: Union[int, float]
        """
        return self.__size

    @size.setter
    @typechecked
    def size(self, size: Union[int, float]) -> Label:
        """Sets font size.

        :param size: font size
        :type size: Union[int, float]
        :return: invoker
        :rtype: Label
        """
        self.__size = size
        return self
