from typing import List, Dict, Optional, TextIO
from collections import defaultdict
from copy import deepcopy
import json

from .key import Key
from .metadata import Metadata, Background
from .keyboard import Keyboard

class DeserializeException(Exception):
    def __init__(self, message: str, payload: dict = None) -> None:
        super().__init__(message + (json.dumps(payload) if payload else ""))

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
