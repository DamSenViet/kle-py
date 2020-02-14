class Background:
    """Class for storing Metadata background info.

    Attributes:
        name {str} -- Name of the background style.
        style {str} -- CSS rule for background resource.
    """
    def __init__(
        self,
        name: str = None,
        style: str = None
    ):
        """Construct a new `Background`. Default arguments provided.

        Keyword Arguments:\n
            name {str} -- Name of the background style. (default: {None})
            style {str} -- CSS rule for background resource. (default: {None})
        """
        self.name = name
        self.style = style

class Metadata:
    """Class for storing Metadata

    Attributes:
        author {str} -- Name/Username of the author.
        backcolor {str} -- Background color.
        background {Background} -- Background style.
        name {str} -- Name of the keyboard.
        notes {str} -- Additional notes.
        radii {str} -- Keyboard corner radii.
        switch_brand {str} -- Switch brand.
        switch_mount {str} -- Switch mount.
        switch_type {str} -- Switch type.
    """
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
        switch_type: str = None
    ):
        """Construct a a new `Metadata`. Default arguments provided.

        Keyword Arguments:
            author {str} -- Name/Username of the author. (default: {None})
            backcolor {str} -- Background color. (default: {"#eeeeee"})
            background {Background} -- Background style. (default: {None})
            name {str} -- Name of the keyboard. (default: {None})
            notes {str} -- Additional notes. (default: {None})
            radii {str} -- Keyboard corner radii. (default: {None})
            switch_brand {str} -- Switch brand. (default: {None})
            switch_mount {str} -- Switch mount. (default: {None})
            switch_type {str} -- Switch type. (default: {None})
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