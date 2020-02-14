from .key import Key
from typing import List
from .metadata import Metadata

class Keyboard:
    """Class that holds data of a `Keyboard` for KLE formatted json data.

    Attributes:
        metadata {Metadata} -- Metadata (like name, author).
        keys {List[Key]} -- List of keys.
    """

    def __init__(
        self,
        metadata: Metadata = Metadata(),
        keys: List[Key] = list()
    ):
        """Construct a new `Keyboard`. Default arguments provided.

        Keyword Arguments:
            metadata {Metadata} -- A metadata instance. (default: {Metadata()})
            keys {List[Key]} -- A `list` of `Key` (default: {list()})
        """
        self.metadata = metadata
        self.keys = keys