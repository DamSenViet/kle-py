from __future__ import annotations
from typeguard import typechecked

from .utils import autorepr, expect, is_valid_css_declaration


class Background:
    """Class storing Metadata's Background."""

    def __init__(self, name: str = "", style: str = ""):
        self.name: str = name
        self.style: str = style

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return autorepr(
            self,
            {
                "name": self.name,
                "style": self.style,
            },
        )

    @property
    def name(self) -> str:
        """Gets name.

        :return: name
        :rtype: str
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        """Sets name.

        :param name: name
        :type name: str
        """
        self.__name = name

    @property
    def style(self) -> str:
        """Gets CSS style declaration.

        :return: CSS style declaration
        :rtype: str
        """
        return self.__style

    @style.setter
    @typechecked
    def style(self, style: str) -> None:
        """Sets CSS declaration.

        :param style: CSS declaration
        :type style: str
        """
        expect(
            "style",
            style,
            "to be a valid css declaration",
            is_valid_css_declaration,
        )
        self.__style = style
