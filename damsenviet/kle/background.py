from __future__ import annotations
from typeguard import typechecked

from .utils import autorepr


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
        """Gets CSS style rule.

        No validation is applied, KLE doesn't validate the CSS rule.

        :return: CSS style rule
        :rtype: str
        """
        return self.__style

    @style.setter
    @typechecked
    def style(self, style: str) -> None:
        """Sets CSS style rule.

        :param style: CSS style rule
        :type style: str
        """
        self.__style = style
