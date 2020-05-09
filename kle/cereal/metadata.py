import collections as col

from .util import serialize_prop

class Background:
    """Class for storing Metadata background info."""

    def __init__(
        self,
        name: str = None,
        style: str = None
    ):
        """Construct a new `Background`. Default arguments provided.

        :param name: Name of the background style, defaults to None.
        :type name: str
        :param style: CSS rule for background resources, defaults to None.
        :type style: str
        """
        self.name = name
        self.style = style

class Metadata:
    """Class for storing Metadata."""

    def __init__(
        self,
        author: str = None,
        backcolor: str = "#eeeeee",
        background: Background =  None,
        name: str = None,
        notes: str = None,
        radii: str = None,
        switch_brand: str = None,
        switch_mount: str = None,
        switch_type: str = None,
        pcb: bool = False,
        plate: bool = False
    ):
        """Construct a a new `Metadata`. Default arguments provided.

        :param author: Name/Username of the author, defaults to None.
        :type author: str
        :param backcolor: Background color, defaults to None.
        :type backcolor: str
        :param background: Background style, defaults to None.
        :type background: Background
        :param name: Name of the keyboard, defaults to None.
        :type name: str
        :param notes: Additional notes, defaults to None.
        :type notes: str
        :param radii: Keyboard corner radii, defaults to None.
        :type radii: str
        :param switch_brand: Name of the switch brand.
        :type switch_brand: str
        :param switch_mount: Name of the switch mount.
        :type switch_mount: str
        :param switch_type: Name of the switch type.
        :type switch_type: str
        """
        self.author = author
        self.backcolor = backcolor
        self.background = background
        self.name = name
        self.notes = notes
        self.radii = radii
        self.switch_brand = switch_brand
        self.switch_mount = switch_mount
        self.switch_type = switch_type
        self.pcb = pcb
        self.plate = plate