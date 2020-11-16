from typing import List
from .key import Key
from .metadata import Metadata

class Keyboard:
    """Class that holds data of a `Keyboard` for KLE formatted json data."""

    def __init__(
        self,
        metadata: Metadata = Metadata(),
        keys: List[Key] = list()
    ):
        """Construct a new `Keyboard`. Default arguments provided.

        :param metadata: A metadata instance, defaults to Metadata().
        :type metadata: Metadata
        :param keys: A `list` of `Key`, defaults to list().
        :type keys: List[Key]
        """
        self.metadata = metadata
        self.keys = keys