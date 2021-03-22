from __future__ import annotations
from typeguard import typechecked
from .utils import autorepr

__all__ = ["Background"]


class Background:
    """Class storing Metadata's Background."""

    def __init__(self):
        self.__name: str = ""
        self.__style: str = ""

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
        """Name of the background option.

        :getter: gets the name of the background
        :setter: sets the name of the background
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def style(self) -> str:
        """Background CSS style declaration.

        :getter: gets CSS style declaration of the background
        :setter: sets CSS style declaration of the background
        """
        return self.__style

    @style.setter
    @typechecked
    def style(self, style: str) -> None:
        self.__style = style
