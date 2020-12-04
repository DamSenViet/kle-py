from __future__ import annotations
from typing import (
    Union,
)

from typeguard import typechecked


class Background:
    """Class for storing KLE Metadata Background.

    :ivar name: name of the background style, defaults to None.
    :vartype name: Union[str, None]
    :ivar style: a CSS rule for background, defaults to None.
    :vartype style: Union[str, None]
    """

    def __init__(self):
        self.__name: str = ""
        self.__style: str = ""

    def get_name(self) -> str:
        """Gets the name of the background.
        """
        return self.__name

    @typechecked
    def set_name(self, name: str) -> Background:
        """Sets the name of the background.

        :param name: the name of the background
        :type name: str
        :return: the invoking background
        :rtype: Background
        """
        self.__name = name
        return self

    def get_style(self) -> str:
        """Gets the CSS style rule for the background.

        :return: the CSS style rule
        :rtype: str
        """
        return self.__style

    @typechecked
    def set_style(self, style: str) -> Background:
        """Sets the CSS style rule for the background.

        :param style: the CSS style rule
        :type style: str
        :return: the invoking background
        :rtype: Background
        """
        self.__style = style
        return self
