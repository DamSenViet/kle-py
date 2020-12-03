from __future__ import annotations
from copy import (
    deepcopy,
)
from typing import(
    Union,
)
from typeguard import(
    typechecked,
)


class Label:
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

    def __copy__(self):
        """Creates a shallow copy of the Label.

        :return: shallow copy of the Label
        :rtype: Label
        """
        new_label = type(self)()
        return new_label

    def __deepcopy__(self, memo):
        """Creates a deepcopy of the Label.

        :param memo: dictionary of objects already copied
        :type memo: Dict
        :return: deep copy of the Label
        :rtype: Label
        """
        new_label: Label = type(self)()
        memo[id(self)] = new_label
        new_label.__dict__.update(self.__dict__)
        return new_label

    def get_text(self) -> str:
        return self.__text

    @typechecked
    def set_text(self, text: str) -> Label:
        self.__text = text
        return self

    def get_color(self) -> str:
        return self.__color

    @typechecked
    def set_color(self, color: str) -> Label:
        self.__color = color
        return self

    def get_size(self) -> Union[int, float]:
        return self.__size

    @typechecked
    def set_size(self, size: Union[int, float]) -> Label:
        self.__size = size
        return self
