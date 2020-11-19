from typing import (
    Union,
)


class Background:
    """Class for storing KLE Metadata Background.

    :ivar name: name of the background style, defaults to None.
    :vartype name: Union[str, None]
    :ivar style: a CSS rule for background, defaults to None.
    :vartype style: Union[str, None]
    """

    def __init__(self):
        self.name = None
        self.style = None
