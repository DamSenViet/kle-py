from __future__ import annotations
from typeguard import typechecked

from .background import Background


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
        self.switch_mount: str = ""
        self.switch_brand: str = ""
        self.switch_type: str = ""
        self.is_switches_pcb_mounted: bool = False
        self.include_switches_pcb_mounted: bool = False
        self.is_switches_plate_mounted: bool = False
        self.include_switches_plate_mounted: bool = False

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
        self.__background_color = background_color

    @property
    def radii(self) -> str:
        """Gets radius CSS size value.

        :return: radius CSS size value.
        :rtype: str
        """
        return self.__radii

    @radii.setter
    @typechecked
    def radii(self, radii: str) -> None:
        """Sets radius CSS size value.

        :param radii: radius CSS size value
        :type radii: str
        """
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
        self.__css = css

    @property
    def switch_mount(self) -> str:
        """Gets switch mount.

        :return: switch mount
        :rtype: str
        """
        return self.__switch_mount

    @switch_mount.setter
    @typechecked
    def switch_mount(self, switch_mount: str) -> None:
        """Sets switch mount.

        :param switch_mount: switch mount
        :type switch_mount: str
        """
        self.__switch_mount = switch_mount

    @property
    def switch_brand(self) -> str:
        """Gets switch brand.

        :return: switch brand
        :rtype: str
        """
        return self.__switch_brand

    @switch_brand.setter
    @typechecked
    def switch_brand(self, switch_brand: str) -> None:
        """Sets switch brand.

        :param switch_brand: switch  brand
        :type switch_brand: str
        """
        self.__switch_brand = switch_brand

    @property
    def switch_type(self) -> str:
        """Gets switch type.

        :return: switch type
        :rtype: str
        """
        return self.__switch_type

    @switch_type.setter
    @typechecked
    def switch_type(self, switch_type: str) -> None:
        """Sets switch type.

        :param switch_type: switch type
        :type switch_type: str
        """
        self.__switch_type = switch_type

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
