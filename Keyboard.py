from typing import TypedDict, List
import json

class Key(TypedDict):
    color: str
    labels: List[str]

class Metadata(TypedDict):
    def __init__(self, metadata: dict):
        pass

class Keyboard(TypedDict):
    def __init__(self, list):
        self.meta = Metadata()
        self.keys = list()
