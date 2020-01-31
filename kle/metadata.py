class Background:
    def __init__(
        self,
        name: str = None,
        style: str = None
    ):
        self.name = name
        self.style = style

class Metadata:
    def __init__(
        self,
        author: str = None,
        backcolor: str = "#eeeeee",
        background: Background =  None,
        name: str = None,
        notes: str = None,
        radii: str = None,
        switchBrand: str = None,
        switchMount: str = None,
        switchType: str = None
    ):
        self.author = author
        self.backcolor = backcolor
        self.background = background
        self.name = None
        self.notes = None
        self.radii = None
        self.switchBrand = switchBrand
        self.switchMount = switchMount
        self.switchMount = switchType