from __future__ import annotations
from typeguard import typechecked
from .utils import autorepr

__all__ = ["Background"]


class Background:
    """Background information."""

    def __init__(self):
        """Initializes a Background."""
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
        """Name of the background option."""
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def style(self) -> str:
        """Background CSS style declaration."""
        return self.__style

    @style.setter
    @typechecked
    def style(self, style: str) -> None:
        self.__style = style
