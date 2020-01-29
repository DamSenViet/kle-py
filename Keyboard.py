from typing import List, Dict, Optional, TextIO
from typing_extensions import TypedDict
from collections import defaultdict
import json
import copy

### TypedDict Definitions
# tuple syntax for backwards compatibility
Key = TypedDict("Key", {
    "color": str,
    "labels": List[str],
    "textColor": List[str],
    "textSize": List[float],
    "x": float,
    "y": float,
    "width": float,
    "height": float,
    "x2": float,
    "y2": float,
    "width2": float,
    "height2": float,
    "rotation_x": float,
    "rotation_y": float,
    "rotation_angle": float,
    "decal": bool,
    "ghost": bool,
    "stepped": bool,
    "nub": bool,
    "profile": str,
    "sm": str,
    "sb": str,
    "st": str
}, total = True)

MetadataBackground = TypedDict("MetadataBackground", {
    "name": str,
    "style": str
}, total = True)

Metadata = TypedDict("Metadata", {
    "author": str,
    "backcolor": str,
    "background": MetadataBackground
}, total = True)

Keyboard = TypedDict("Keyboard", {
    "meta": Metadata,
    "keys": List[Key]
})

class KLE:
    # parse from json object
    @staticmethod
    def deserialize(rows: List) -> Keyboard:
        current = Key({
            "color": "#cccccc",
            "x": 0,
            "y": 0,
            "width": 1.0,
            "height": 1.0,
            "x2": 0.0,
            "y2": 0.0,
            "width2": 1.0,
            "height2": 1.0,
            "rotation_x": 0.0,
            "rotation_y": 0.0,
            "rotation_angle": 0.0,
            "decal": False,
            "ghost": False,
            "stepped": False,
            "nub": False,
            "profile":  None,
            "sm": None,
            "sb": None,
            "st": None
        })
        kbd = Keyboard({
            "meta": Metadata({
                "author": None,
                "backcolor": None,
                "background": MetadataBackground({

                }),
                "name": None,
                "notes": None,
                "radii": None,
                "switchBrand": None,
                "switchMount": None,
                "switchType": None
            }),
            "keys": []
        })

        for r in range(len(rows)):
            if type(rows[r]) == list:
                for k in range(len(rows[r])):
                    item = rows[r][k]
                    if type(item) == str:
                        newKey = dict.copy(current)
                        kbd["keys"].append(newKey)
                        current["x"] += current["width"]
                        current["width"] = current["height"] = 1
                        current["x2"] = current["y2"] = current["width2"] = current["height2"] = 0
                        current["nub"] = current["stepped"] = current["decal"] = False

                    else:
                        if k != 0 and (item.get("r") or item.get("rx") or item.get("ry")): pass
                        if item.get("r"): current["rotation_angle"] = item["r"]
                        if item.get("rx"): current["rotation_x"] = item["rx"]
                        if item.get("ry"): current["rotation_y"] = item["ry"]
                        if item.get("a"): pass
                        if item.get("f"): pass
                        if item.get("f2"): pass
                        if item.get("fa"): pass
                        if item.get("p"): current["profile"] = item["p"]
                        if item.get("c"): current["color"] = item["c"]
                        if item.get("t"): pass
                        if item.get("x"): current["x"] += item["x"]
                        if item.get("y"): current["y"] += item["y"]
                        if item.get("w"): current["width"] = current["width2"] = item["w"]
                        if item.get("h"): current["height"] = current["height2"] = item["h"]
                        if item.get("x2"): current["x2"] = item["x2"]
                        if item.get("y2"): current["y2"] = item["y2"]
                        if item.get("w2"): current["width2"] = item["width2"]
                        if item.get("h2"): current["height2"] = item["height2"]
                        if item.get("n"): current["nub"] = item["n"]
                        if item.get("l"): current["stepped"] = item["l"]
                        if item.get("d"): current["decal"] = item["d"]
                        if item.get("g"): current["ghost"] = item["g"]
                        if item.get("sm"): current["sm"] = item["sm"]
                        if item.get("sb"): current["sb"] = item["sb"]
                        if item.get("st"): current["st"] = item["st"]
                current["y"] += 1
                current["x"] = current["rotation_x"]
            elif type(rows[r]) == dict:
                kbd["meta"] = rows[r]
            else:
                pass
        return kbd

    # parse from file
    @staticmethod
    def parse(f: TextIO) -> Keyboard:
        return KLE.deserialize(json.load(f))

# keyboard = KLE.parse(open("test.json"))
# print(keyboard["keys"])