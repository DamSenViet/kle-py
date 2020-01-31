from .key import Key
from typing import List
from .metadata import Metadata

class Keyboard:
    def __init__(
        self,
        metadata: Metadata = Metadata(),
        keys: List[Key] = list()
    ):
        self.metadata = metadata
        self.keys = keys