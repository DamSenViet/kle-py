from typing import (
    Union,
)

from .key import Key
from .metadata import Metadata


class Keyboard:
    """Class for storing KLE Keyboard.

    :ivar metadata: the metadata, defaults to metadata
    :vartype metadata: Metadata
    :ivar keys: defaults to []
    :vartype keys: List[Key]
    """

    def __init__(self):
        self.metadata = Metadata()
        self.keys = []
