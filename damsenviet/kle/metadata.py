from __future__ import annotations
from typeguard import typechecked

from .background import Background


class Metadata:
    """Class storing Keyboard's Metadata.
    """

    def __init__(self):
        self.__author: str = ""
        self.__background_color: str = "#eeeeee"
        self.__background: Background = Background()
        self.__name: str = ""
        self.__notes: str = ""
        self.__radii: str = ""
        self.__css: str = ""
        self.__switch_mount: str = ""
        self.__switch_brand: str = ""
        self.__switch_type: str = ""
        self.__include_pcb: bool = False
        self.__pcb: bool = False
        self.__include_plate: bool = False
        self.__plate: bool = False

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
    def background_color(self) -> str:
        """Get author name.

        :return: get author name
        :rtype: str
        """
        return self.__background_color

    @background_color.setter
    @typechecked
    def background_color(self, background_color: str) -> None:
        """Sets background color.

        :param background_color: background color
        :type background_color: str
        :return: invoker
        :rtype: Metadata
        """
        self.__background_color = background_color

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
        :return: invoker
        :rtype: Metadata
        """
        self.__background = background

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
        :return: invoker
        :rtype: Metadata
        """
        self.__name = name

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
        :return: invoker
        :rtype: Metadata
        """
        self.__notes = notes

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
        :return: invoker
        :rtype: Metadata
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
        :return: invoker
        :rtype: Metadata
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
        :return: invoker
        :rtype: Metadata
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
        :return: invoker
        :rtype: Metadata
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
        :return: invoker
        :rtype: Metadata
        """
        self.__switch_type = switch_type

    @property
    def include_pcb(self) -> bool:
        """Gets whether to include default pcb setting in json.

        :return: whether to include default pcb setting in json
        :rtype: bool
        """
        return self.__include_pcb

    @include_pcb.setter
    @typechecked
    def include_pcb(self, include_pcb: bool) -> None:
        """Sets whether to include default pcb setting in json.

        :param include_pcb: whether to include default pcb setting in json
        :type include_pcb: bool
        :return: invoker
        :rtype: Metadata
        """
        self.__include_pcb = include_pcb

    @property
    def pcb(self) -> bool:
        """Gets whether the switches are pcb mounted.

        :return: whether switches are pcb mounted
        :rtype: bool
        """
        return self.__pcb

    @pcb.setter
    @typechecked
    def pcb(self, pcb: bool) -> None:
        """Sets whether switches are pcb mounted.

        :param pcb: whether switches are pcb mounted
        :type pcb: bool
        :return: invoker
        :rtype: Metadata
        """
        self.__pcb = pcb

    @property
    def include_plate(self) -> bool:
        """Sets whether to include default plate setting in json.
        :return: whether to include default plate setting in json
        :rtype: bool
        """
        return self.__include_plate

    @include_plate.setter
    @typechecked
    def include_plate(self, include_plate: bool) -> None:
        """Sets whether to include default plate setting in json.

        :param include_plate: whether to include default plate setting in json
        :type include_plate: bool
        :return: invoker
        :rtype: Metadata
        """
        self.__include_plate = include_plate

    @property
    def plate(self) -> bool:
        """Gets whether switches are plate mounted.

        :return: whether switches are plate mounted
        :rtype: bool
        """
        return self.__plate

    @plate.setter
    @typechecked
    def plate(self, plate: bool) -> None:
        """Sets whether switches are plate mounted.

        :param plate: whether switches are plate mounted
        :type plate: bool
        :return: invoker
        :rtype: Metadata
        """
        self.__plate = plate
