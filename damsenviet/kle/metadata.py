from __future__ import annotations
from typeguard import typechecked

from .background import Background
from .switch import Switch
from .utils import (
    autorepr,
    expect,
    is_valid_css_stylesheet,
    is_valid_css_color,
    is_valid_css_component_value_list,
)


class Metadata:
    """Class storing Keyboard's Metadata."""

    def __init__(self):
        self.name: str = ""
        self.author: str = ""
        self.notes: str = ""
        self.background: Background = Background()
        self.background_color: str = "#eeeeee"
        self.radii: str = ""
        self.css: str = ""
        self.switch = Switch("", "", "")
        self.is_switches_pcb_mounted: bool = False
        self.include_switches_pcb_mounted: bool = False
        self.is_switches_plate_mounted: bool = False
        self.include_switches_plate_mounted: bool = False

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return autorepr(
            self,
            {
                "name": self.name,
                "author": self.author,
                "notes": self.notes,
                "background": self.background,
                "background_color": self.background_color,
                "radii": self.radii,
                "css": self.css,
                "switch": self.switch,
                "is_switches_pcb_mounted": self.is_switches_pcb_mounted,
                "include_switches_pcb_mounted": self.include_switches_pcb_mounted,
                "is_switches_plate_mounted": self.is_switches_plate_mounted,
                "include_switches_plate_mounted": self.include_switches_plate_mounted,
            },
        )

    @property
    def name(self) -> str:
        """Gets name of the keyboard.

        :return: name of the keyboard
        :rtype: str
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        """Sets name of the keyboard.

        :param name: name of the keyboard
        :type name: str
        """
        self.__name = name

    @property
    def author(self) -> str:
        """Gets author name.

        :return: author name
        :rtype: str
        """
        return self.__author

    @author.setter
    @typechecked
    def author(self, author: str) -> None:
        """Sets author name.

        :param author: author name
        :type author: str
        """
        self.__author = author

    @property
    def notes(self) -> str:
        """Gets notes.

        :return: notes
        :rtype: str
        """
        return self.__notes

    @notes.setter
    @typechecked
    def notes(self, notes: str) -> None:
        """Sets notes.

        :param notes: notes
        :type notes: str
        """
        self.__notes = notes

    @property
    def background(self) -> Background:
        """Gets background of the keyboard.

        :return: background of the keyboard
        :rtype: Background
        """
        return self.__background

    @background.setter
    @typechecked
    def background(self, background: Background) -> None:
        """Sets background of the keyboard.

        :param background: background of the keyboard
        :type background: Background
        """
        self.__background = background

    @property
    def background_color(self) -> str:
        """Gets background color.

        :return: background color
        :rtype: str
        """
        return self.__background_color

    @background_color.setter
    @typechecked
    def background_color(self, background_color: str) -> None:
        """Sets background color.

        :param background_color: background color
        :type background_color: str
        """
        expect(
            "background_color",
            background_color,
            "be a valid css color",
            is_valid_css_color,
        )
        self.__background_color = background_color

    @property
    def radii(self) -> str:
        """Gets radius CSS component values.

        :return: radius CSS component values
        :rtype: str
        """
        return self.__radii

    @radii.setter
    @typechecked
    def radii(self, radii: str) -> None:
        """Sets radius CSS component values.

        :param radii: radius CSS component values
        :type radii: str
        """
        expect(
            "radii",
            radii,
            "be a valid list of css component values",
            is_valid_css_component_value_list,
        )
        self.__radii = radii

    @property
    def css(self) -> str:
        """Gets CSS stylesheet.

        :return: CSS stylehseet
        :rtype: str
        """
        return self.__css

    @css.setter
    @typechecked
    def css(self, css: str) -> None:
        """Sets CSS stylesheet

        :param css: CSS stylesheet
        :type css: str
        """
        expect(
            "css",
            css,
            "to be valid CSS",
            is_valid_css_stylesheet,
        )
        self.__css = css

    @property
    @typechecked
    def switch(self) -> Switch:
        """Gets switch.

        :return: switch
        :rtype: Switch
        """
        return self.__switch

    @switch.setter
    def switch(self, switch: Switch) -> None:
        """Sets switch.

        :param switch: switch
        :type switch: Switch
        """
        self.__switch = switch

    @property
    def is_switches_pcb_mounted(self) -> bool:
        """Gets whether the switches are pcb mounted.

        :return: whether switches are pcb mounted
        :rtype: bool
        """
        return self.__is_switches_pcb_mounted

    @is_switches_pcb_mounted.setter
    @typechecked
    def is_switches_pcb_mounted(self, is_switches_pcb_mounted: bool) -> None:
        """Sets whether switches are pcb mounted.

        :param is_switches_pcb_mounted: whether switches are pcb mounted
        :type is_switches_pcb_mounted: bool
        """
        self.__is_switches_pcb_mounted = is_switches_pcb_mounted

    @property
    def include_switches_pcb_mounted(self) -> bool:
        """Gets whether to force include switch pcb mounting in json.

        :return: whether to force include switch pcb mounting in json
        :rtype: bool
        """
        return self.__include_switches_pcb_mounted

    @include_switches_pcb_mounted.setter
    @typechecked
    def include_switches_pcb_mounted(self, include_switches_pcb_mounted: bool) -> None:
        """Sets whether to force include switch pcb mounting in json.

        :param include_switches_pcb_mounted: whether to include switch pcb mounting in json
        :type include_switches_pcb_mounted: bool
        """
        self.__include_switches_pcb_mounted = include_switches_pcb_mounted

    @property
    def is_switches_plate_mounted(self) -> bool:
        """Gets whether switches are plate mounted.

        :return: whether switches are plate mounted
        :rtype: bool
        """
        return self.__is_switches_plate_mounted

    @is_switches_plate_mounted.setter
    @typechecked
    def is_switches_plate_mounted(self, is_switches_plate_mounted: bool) -> None:
        """Sets whether switches are plate mounted.

        :param is_switches_plate_mounted: whether switches are plate mounted
        :type is_switches_plate_mounted: bool
        """
        self.__is_switches_plate_mounted = is_switches_plate_mounted

    @property
    def include_switches_plate_mounted(self) -> bool:
        """Sets whether to force include switch plate mounting in json.

        :return: whether to force include switch plate mounting in json
        :rtype: bool
        """
        return self.__include_switches_plate_mounted

    @include_switches_plate_mounted.setter
    @typechecked
    def include_switches_plate_mounted(
        self, include_switches_plate_mounted: bool
    ) -> None:
        """Sets whether to force include switch plate mounting in json.

        :param include_switches_plate_mounted: whether to force include switch plate mounting in json
        :type include_switches_plate_mounted: bool
        """
        self.__include_switches_plate_mounted = include_switches_plate_mounted
