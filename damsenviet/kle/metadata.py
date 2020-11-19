from typing import (
    Union
)

from .background import Background


class Metadata:
    """Class for storing KLE Metadata.

    :ivar author: author, defaults to ""
    :vartype author: str
    :ivar backcolor: background color, defaults to "#eeeeee"
    :vartype backcolor: str
    :ivar background: the background, defaults to Background()
    :vartype background: Background
    :ivar name: the Keyboard name, defaults to ""
    :vartype name: str
    :ivar notes: notes, defaults to ""
    :vartype notes: str
    :ivar radii: a CSS size value, defaults to ""
    :vartype radii: Union[str, None]
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
        self.backcolor = "#eeeeee"
        self.background = Background()
        self.name = ""
        self.notes = ""
        self.radii = None
        self.switch_mount = ""
        self.switch_brand = ""
        self.switch_type = ""
        self.pcb = False
        self.plate = False
