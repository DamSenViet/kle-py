from __future__ import annotations
from typeguard import typechecked


class Background:
    """Class storing Metadata's Background.
    """

    def __init__(self):
        self.__name: str = ""
        self.__style: str = ""

    @property
    def name(self) -> str:
        """Gets name.

        :return: name
        :rtype: str
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> Background:
        """Sets name.

        :param name: name
        :type name: str
        :return: invoker
        :rtype: Background
        """
        self.__name = name
        return self

    @property
    def style(self) -> str:
        """Gets CSS style rule.

        :return: CSS style rule
        :rtype: str
        """
        return self.__style

    @style.setter
    @typechecked
    def style(self, style: str) -> Background:
        """Sets CSS style rule.

        :param style: CSS style rule
        :type style: str
        :return: invoker
        :rtype: Background
        """
        self.__style = style
        return self
