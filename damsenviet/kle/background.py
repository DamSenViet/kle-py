from __future__ import annotations

__all__ = ["Background"]


class Background:
    """Background information."""

    def __init__(self):
        """Initializes a Background."""
        self.__name: str = ""
        self.__style: str = ""

    @property
    def name(self) -> str:
        """Name of the background option."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def style(self) -> str:
        """Background CSS style declaration."""
        return self.__style

    @style.setter
    def style(self, style: str) -> None:
        self.__style = style
