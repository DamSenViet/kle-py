from typing import (
    Union
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
    :ivar pcb: whether a pcb is used to mount switches, defaults to False
    :vartype pcb: bool
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
        self.pcb = None
        self.plate = None
