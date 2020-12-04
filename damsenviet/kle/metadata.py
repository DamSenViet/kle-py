from __future__ import annotations
from copy import (
    deepcopy,
)
from typing import (
    Dict,
)

from typeguard import typechecked

from .background import Background


class Metadata:
    """Class for storing KLE Metadata.

    :ivar author: author, defaults to ""
    :vartype author: str
    :ivar background_color: background color, defaults to "#eeeeee"
    :vartype background_color: str
    :ivar background: the background, defaults to Background()
    :vartype background: Background
    :ivar name: the Keyboard name, defaults to ""
    :vartype name: str
    :ivar notes: notes, defaults to ""
    :vartype notes: str
    :ivar css: custom css rules
    :vartype css: str
    :ivar radii: a CSS size value, defaults to ""
    :vartype radii: str
    :ivar switch_mount: the switch mount, defaults to ""
    :vartype switch_mount: str
    :ivar switch_brand: the switch brand, defaults to ""
    :vartype switch_brand: str
    :ivar switch_type: the switch type, defaults to ""
    :vartype switch_type: str
    :ivar include_pcb: whether to include the pcb value in json, true when
        loaded from json
    :vartype include_pcb: bool
    :ivar pcb: whether a pcb is used to mount switches, defaults to False
    :vartype pcb: bool
    :ivar include_plate: whether to include the plate value in json true when
        loaded from json
    :vartype include_plate: bool
    :ivar plate: whether a plate is used to mount switches, defaults to False
    :vartype plate: bool
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

    def __deepcopy__(self, memo: Dict = dict()):
        """Creates a deep copy of the Metadata.

        :param memo: dictionary of objects already copied
        :type memo: Dict
        :return: deep copy of the Metadata
        :rtype: Metadata
        """
        new_metadata: Metadata = Metadata()
        memo[id(self)] = new_metadata
        new_metadata.__dict__.update(self.__dict__)
        new_metadata.set_background(deepcopy(self.__background))
        return new_metadata

    def get_author(self) -> str:
        return self.__author

    @typechecked
    def set_author(self, author: str) -> Metadata:
        self.__author = author
        return self

    def get_background_color(self) -> str:
        return self.__background_color

    @typechecked
    def set_background_color(self, background_color: str) -> Metadata:
        self.__background_color = background_color
        return self

    def get_background(self) -> Background:
        return self.__background

    @typechecked
    def set_background(self, background: Background) -> Metadata:
        self.__background = background
        return self

    def get_name(self) -> str:
        return self.__name

    @typechecked
    def set_name(self, name: str) -> Metadata:
        self.__name = name
        return self

    def get_notes(self) -> str:
        return self.__notes

    @typechecked
    def set_notes(self, notes: str) -> Metadata:
        self.__notes = notes
        return self

    def get_radii(self) -> str:
        return self.__radii

    @typechecked
    def set_radii(self, radii: str) -> Metadata:
        self.__radii = radii
        return self

    def get_css(self) -> str:
        return self.__css

    @typechecked
    def set_css(self, css: str) -> Metadata:
        self.__css = css
        return self

    def get_switch_mount(self) -> str:
        return self.__switch_mount

    @typechecked
    def set_switch_mount(self, switch_mount: str) -> Metadata:
        self.__switch_mount = switch_mount
        return self

    def get_switch_brand(self) -> str:
        return self.__switch_brand

    @typechecked
    def set_switch_brand(self, switch_brand: str) -> Metadata:
        self.__switch_brand = switch_brand
        return self

    def get_switch_type(self) -> str:
        return self.__switch_type

    @typechecked
    def set_switch_type(self, switch_type: str) -> Metadata:
        self.__switch_type = switch_type
        return self

    def get_include_pcb(self) -> bool:
        return self.__include_pcb

    @typechecked
    def set_include_pcb(self, include_pcb: bool) -> Metadata:
        self.__include_pcb = include_pcb
        return self

    def get_pcb(self) -> bool:
        return self.__pcb

    @typechecked
    def set_pcb(self, pcb: bool) -> Metadata:
        self.__pcb = pcb
        return self

    def get_include_plate(self) -> bool:
        return self.__include_plate

    @typechecked
    def set_include_plate(self, include_plate: bool) -> Metadata:
        self.__include_plate = include_plate
        return self

    def get_plate(self) -> bool:
        return self.__plate

    @typechecked
    def set_plate(self, plate: bool) -> Metadata:
        self.__plate = plate
        return self
