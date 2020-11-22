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
    :ivar __include_pcb: whether to include the pcb value, true when loaded
    :vartype __include_pcb: bool
    :ivar pcb: whether a pcb is used to mount switches, defaults to False
    :vartype pcb: bool
    :ivar __include_plate: whether to include the plate value, true when loaded
    :vartype __include_plate: bool
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
        self._include_pcb = False
        self.pcb = False
        self._include_plate = False
        self.plate = False

    def __eq__(self, other):
        return (
            type(other) is type(self) and
            other.author == self.author and
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
