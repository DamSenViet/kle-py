from __future__ import annotations
from typing import Union
from typeguard import typechecked
from .background import Background
from .switch import Switch
from .utils import autorepr

__all__ = ["Metadata"]


class Metadata:
    """Class storing Keyboard's Metadata."""

    def __init__(self):
        self.__name: str = ""
        self.__author: str = ""
        self.__notes: str = ""
        self.__background: Background = None
        self.__background_color: str = "#eeeeee"
        self.__radii: str = ""
        self.__css: str = ""
        self.__switch: Switch = Switch()
        self.__is_switches_pcb_mounted: bool = False
        self.__include_switches_pcb_mounted: bool = False
        self.__is_switches_plate_mounted: bool = False
        self.__include_switches_plate_mounted: bool = False

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
        """Name of the keyboard.

        :getter: gets name of the keyboard
        :setter: sets name of the keyboard
        :type: str
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def author(self) -> str:
        """Author name.

        :getter: gets author name
        :setter: sets author name
        :type: str
        """
        return self.__author

    @author.setter
    @typechecked
    def author(self, author: str) -> None:
        self.__author = author

    @property
    def notes(self) -> str:
        """Notes.

        :getter: gets notes
        :setter: sets notes
        :type: str
        """
        return self.__notes

    @notes.setter
    @typechecked
    def notes(self, notes: str) -> None:
        self.__notes = notes

    @property
    def background(self) -> Union[None, Background]:
        """Background of the keyboard.

        :getter: gets background of the keyboard
        :setter: sets background of the keyboard
        :type: Background
        """
        return self.__background

    @background.setter
    @typechecked
    def background(
        self,
        background: Union[None, Background],
    ) -> Union[None, Background]:
        self.__background = background

    @property
    def background_color(self) -> str:
        """Background CSS color.

        :getter: gets background CSS color
        :setter: sets background CSS color
        :type: str
        """
        return self.__background_color

    @background_color.setter
    @typechecked
    def background_color(self, background_color: str) -> None:
        self.__background_color = background_color

    @property
    def radii(self) -> str:
        """Border-Radius CSS component values.

        :getter: gets border-radius CSS component values
        :setter: sets border-radius CSS component values
        :type: str
        """
        return self.__radii

    @radii.setter
    @typechecked
    def radii(self, radii: str) -> None:
        self.__radii = radii

    @property
    def css(self) -> str:
        """CSS stylesheet.

        :getter: gets CSS stylehseet
        :setter: sets CSS stylehseet
        :type: str
        """
        return self.__css

    @css.setter
    @typechecked
    def css(self, css: str) -> None:
        self.__css = css

    @property
    def switch(self) -> Switch:
        """Switch.

        :getter: gets switch
        :setter: sets switch
        :type: Switch
        """
        return self.__switch

    @switch.setter
    @typechecked
    def switch(self, switch: Switch) -> None:
        self.__switch = switch

    @property
    def is_switches_pcb_mounted(self) -> bool:
        """Whether the switches are pcb mounted.

        :getter: gets whether switches are pcb mounted
        :setter: sets whether switches are pcb mounted
        :type: bool
        """
        return self.__is_switches_pcb_mounted

    @is_switches_pcb_mounted.setter
    @typechecked
    def is_switches_pcb_mounted(self, is_switches_pcb_mounted: bool) -> None:
        self.__is_switches_pcb_mounted = is_switches_pcb_mounted

    @property
    def include_switches_pcb_mounted(self) -> bool:
        """Whether to force include switch pcb mounting in json.

        :getter: gets whether to force include switch pcb mounting in json
        :setter: sets whether to force include switch pcb mounting in json
        :type: bool
        """
        return self.__include_switches_pcb_mounted

    @include_switches_pcb_mounted.setter
    @typechecked
    def include_switches_pcb_mounted(self, include_switches_pcb_mounted: bool) -> None:
        self.__include_switches_pcb_mounted = include_switches_pcb_mounted

    @property
    def is_switches_plate_mounted(self) -> bool:
        """Whether switches are plate mounted.

        :getter: gets whether switches are plate mounted
        :setter: sets whether switches are plate mounted
        :type: bool
        """
        return self.__is_switches_plate_mounted

    @is_switches_plate_mounted.setter
    @typechecked
    def is_switches_plate_mounted(self, is_switches_plate_mounted: bool) -> None:
        self.__is_switches_plate_mounted = is_switches_plate_mounted

    @property
    def include_switches_plate_mounted(self) -> bool:
        """Whether to force include switch plate mounting in json.

        :getter: gets whether to force include switch plate mounting in json
        :setter: sets whether to force include switch plate mounting in json
        :type: bool
        """
        return self.__include_switches_plate_mounted

    @include_switches_plate_mounted.setter
    @typechecked
    def include_switches_plate_mounted(
        self, include_switches_plate_mounted: bool
    ) -> None:
        self.__include_switches_plate_mounted = include_switches_plate_mounted
