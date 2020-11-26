from __future__ import annotations
from copy import (
    deepcopy,
)
from typing import (
    Dict,
)


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
        self.author = ""
        self.background_color = "#eeeeee"
        self.background = Background()
        self.name = ""
        self.notes = ""
        self.radii = ""
        self.css = ""
        self.switch_mount = ""
        self.switch_brand = ""
        self.switch_type = ""
        self.include_pcb = False
        self.pcb = False
        self.include_plate = False
        self.plate = False

    # overriding only bc specific properties need to be ignored
    def __eq__(self, other):
        """Checks for Metadata equality.

        :param other: the other object
        :type other: Any
        :return: whether the objects are equal
        :rtype: bool
        """
        return (
            Metadata is type(other) and
            self.author == other.author and
            self.background_color == other.background_color and
            self.background == other.background and
            self.name == other.name and
            self.notes == other.notes and
            self.radii == other.radii and
            self.css == other.css and
            self.switch_mount == other.switch_mount and
            self.switch_brand == other.switch_brand and
            self.switch_type == other.switch_type and
            self.pcb == other.pcb and
            self.plate == other.plate
        )

    def __ne__(self, other):
        return not other == self

    def __deepcopy__(self, memo: Dict = dict()):
        """Creates a deep copy of the Metadata.

        :param memo: dictionary of objects already copied
        :type memo: Dict
        :return: deep copy of the Metadata
        :rtype: Metadata
        """
        new_metadata = type(self)()
        memo[id(self)] = new_metadata
        new_metadata.__dict__.update(self.__dict__)
        new_metadata.background = deepcopy(self.background)
        return new_metadata
