from __future__ import annotations
from typing import Union

__all__ = ["Label"]


class Label:
    """Label information."""

    def __init__(self):
        """Initializes a Label."""
        self.__text: str = ""
        self.__color: str = "#000000"
        self.__size: Union[int, float] = 3

    @property
    def text(self) -> str:
        """Text content."""
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text

    @property
    def color(self) -> str:
        """CSS text color."""
        return self.__color

    # any valid css color str value
    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    @property
    def size(self) -> Union[int, float]:
        """Font size scale."""
        return self.__size

    @size.setter
    def size(self, size: Union[int, float]) -> None:
        self.__size = size
