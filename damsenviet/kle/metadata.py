from __future__ import annotations
from typing import Union
from .background import Background
from .switch import Switch

__all__ = ["Metadata"]


class Metadata:
    """Metadata information."""

    def __init__(self):
        """Initializes a Metadata."""
        self.__name: str = ""
        self.__author: str = ""
        self.__notes: str = ""
        self.__background: Background = Background()
        self.__background_color: str = "#eeeeee"
        self.__radii: str = ""
        self.__css: str = ""
        self.__switch: Switch = Switch()
        self.__is_switches_pcb_mounted: bool = False
        self.__include_switches_pcb_mounted: bool = False
        self.__is_switches_plate_mounted: bool = False
        self.__include_switches_plate_mounted: bool = False

    @property
    def name(self) -> str:
        """Keyboard name."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def author(self) -> str:
        """Author's name."""
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        self.__author = author

    @property
    def notes(self) -> str:
        """Author's Notes."""
        return self.__notes

    @notes.setter
    def notes(self, notes: str) -> None:
        self.__notes = notes

    @property
    def background(self) -> Background:
        """Background of the keyboard."""
        return self.__background

    @background.setter
    def background(
        self,
        background: Union[None, Background],
    ) -> Union[None, Background]:
        self.__background = background

    @property
    def background_color(self) -> str:
        """Background CSS color."""
        return self.__background_color

    @background_color.setter
    def background_color(self, background_color: str) -> None:
        self.__background_color = background_color

    @property
    def radii(self) -> str:
        """CSS border-radius value."""
        return self.__radii

    @radii.setter
    def radii(self, radii: str) -> None:
        self.__radii = radii

    @property
    def css(self) -> str:
        """CSS stylesheet."""
        return self.__css

    @css.setter
    def css(self, css: str) -> None:
        self.__css = css

    @property
    def switch(self) -> Switch:
        """Switch information."""
        return self.__switch

    @switch.setter
    def switch(self, switch: Switch) -> None:
        self.__switch = switch

    @property
    def is_switches_pcb_mounted(self) -> bool:
        """Whether the switches are pcb mounted."""
        return self.__is_switches_pcb_mounted

    @is_switches_pcb_mounted.setter
    def is_switches_pcb_mounted(self, is_switches_pcb_mounted: bool) -> None:
        self.__is_switches_pcb_mounted = is_switches_pcb_mounted

    @property
    def include_switches_pcb_mounted(self) -> bool:
        """Whether to force include switch pcb mounting in the KLE JSON."""
        return self.__include_switches_pcb_mounted

    @include_switches_pcb_mounted.setter
    def include_switches_pcb_mounted(self, include_switches_pcb_mounted: bool) -> None:
        self.__include_switches_pcb_mounted = include_switches_pcb_mounted

    @property
    def is_switches_plate_mounted(self) -> bool:
        """Whether switches are plate mounted."""
        return self.__is_switches_plate_mounted

    @is_switches_plate_mounted.setter
    def is_switches_plate_mounted(self, is_switches_plate_mounted: bool) -> None:
        self.__is_switches_plate_mounted = is_switches_plate_mounted

    @property
    def include_switches_plate_mounted(self) -> bool:
        """Whether to force include switch plate mounting in the KLE JSON."""
        return self.__include_switches_plate_mounted

    @include_switches_plate_mounted.setter
    def include_switches_plate_mounted(
        self, include_switches_plate_mounted: bool
    ) -> None:
        self.__include_switches_plate_mounted = include_switches_plate_mounted
