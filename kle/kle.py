from typing import List, Dict, Optional, TextIO
from collections import defaultdict
from copy import copy, deepcopy
import json


class DeserializeException(Exception):
    def __init__(self, message: str, payload: dict = None) -> None:
        super().__init__(message + (json.dumps(payload) if payload else ""))

class Key:
    def __init__(
        self,
        color: str = "#cccccc",
        labels: list = list(),
        textColor: str = "#000000",
        textSize: float = 3.0,
        x: float = 0.0,
        y: float = 0.0,
        width: float = 1.0,
        height: float = 1.0,
        x2: float  = 0.0,
        y2: float = 0.0,
        width2: float = 1.0,
        height2: float = 1.0,
        rotation_x: float = 0.0,
        rotation_y: float = 0.0,
        rotation_angle: float = 0.0,
        decal: bool = False,
        ghost: bool = False,
        stepped: bool = False,
        nub: bool = False,
        profile: str = None,
        sm: str = None,
        sb: str = None,
        st: str = None
    ) -> None:
        self.color = color
        self.labels = labels
        self.textColor = textColor
        self.textSize = textSize
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x2
        self.y2 = y2
        self.width2 = width2
        self.height2 = height2
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_angle = rotation_angle
        self.decal = decal
        self.ghost = ghost
        self.stepped = stepped
        self.nub = nub
        self.profile = profile
        self.sm = sm
        self.sb = sb
        self.st = st

    def __deepcopy__(self, memo):
        newKey = type(self)()
        memo[id(self)] = newKey
        newKey.__dict__.update(self.__dict__)
        newKey.labels = deepcopy(self.labels, memo)
        return newKey


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


class Keyboard:
    def __init__(
        self,
        metadata: Metadata = Metadata(),
        keys: list = list()
    ):
        self.metadata = metadata
        self.keys = keys


class KLE:
    @staticmethod
    def deserialize(rows: List) -> Keyboard:

        # track rotation info for reset x/y positions
        # if rotation_angle != 0, it is always specified LAST
        key = Key() # readies the next key data when str encountered
        keyboard = Keyboard()
        align = 4

        current_rotation = 0.0
        current_rotation_x = 0.0
        current_rotation_y = 0.0

        for r in range(len(rows)):
            if type(rows[r]) == list:
                for k in range(len(rows[r])):
                    item = rows[r][k]
                    if type(item) == str:
                        newKey = deepcopy(key, {})
                        keyboard.keys.append(newKey)

                        key.x += key.width
                        key.width = 1
                        key.height = 1
                        key.x2 = 0
                        key.y2 = 0
                        key.width2 = 0
                        key.height2 = 0
                        key.nub = False
                        key.stepped = False
                        key.decal = False

                    else:
                        if k != 0 and (item.get("r") or item.get("rx") or item.get("ry")):
                            raise DeserializeException("")

                        if item.get("r"): key.rotation_angle = item["r"]
                        if item.get("rx"): key.rotation_x = item["rx"]
                        if item.get("ry"): key.rotation_y = item["ry"]

                        if current_rotation != key.rotation_angle or \
                            current_rotation_x != key.rotation_x or \
                            current_rotation_y != key.rotation_y:

                            if current_rotation_x != key.rotation_x or \
                                current_rotation_y != key.rotation_y:
                                key.y = key.rotation_y

                            current_rotation = key.rotation_angle
                            current_rotation_x = key.rotation_x
                            current_rotation_y = key.rotation_y
                            key.x = key.rotation_x

                        if item.get("a"): pass
                        if item.get("f"): pass
                        if item.get("f2"): pass
                        if item.get("fa"): key.textSize = item["fa"]
                        if item.get("p"): key.profile = item["p"]
                        if item.get("c"): key.color = item["c"]
                        if item.get("t"): pass
                        if item.get("x"): key.x += item["x"]
                        if item.get("y"): key.y += item["y"]
                        if item.get("w"):
                            key.width = item["w"]
                            key.width2 = item["w"]
                        if item.get("h"):
                            key.height = item["h"]
                            key.height2 = item["h"]
                        if item.get("x2"): key.x2 = item["x2"]
                        if item.get("y2"): key.y2 = item["y2"]
                        if item.get("w2"): key.width2 = item["width2"]
                        if item.get("h2"): key.height2 = item["height2"]
                        if item.get("n"): key.nub = item["n"]
                        if item.get("l"): key.stepped = item["l"]
                        if item.get("d"): key.decal = item["d"]
                        if item.get("g"): key.ghost = item["g"]
                        if item.get("sm"): key.sm = item["sm"]
                        if item.get("sb"): key.sb = item["sb"]
                        if item.get("st"): key.st = item["st"]
                key.y += 1
                key.x = key.rotation_x
            elif type(rows[r]) == dict:
                # unpack metadata into keyboard metadata
                metadata = rows[r] # aliased
                keyboard.metadata.author = metadata.get("author")
                keyboard.metadata.backcolor = metadata.get("backcolor")
                if metadata.get("background"):
                    keyboard.metadata.background = Background(
                        metadata["background"].get("name"),
                        metadata["background"].get("style")
                    )
                keyboard.metadata.name = metadata.get("name")
                keyboard.metadata.notes = metadata.get("notes")
                keyboard.metadata.radii = metadata.get("radii")
                keyboard.metadata.switchBrand = metadata.get("switchBrand")
                keyboard.metadata.switchMount = metadata.get("switchMount")
                keyboard.metadata.switchType = metadata.get("switchType")
            else:
                raise DeserializeException
        return keyboard

    # parse from file
    @staticmethod
    def parse(f: TextIO) -> Keyboard:
        return KLE.deserialize(json.load(f))
