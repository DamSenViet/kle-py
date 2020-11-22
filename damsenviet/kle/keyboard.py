from __future__ import annotations
from copy import (
    deepcopy,
)
from decimal import (
    Decimal,
    getcontext,
)
from collections import (
    OrderedDict,
)
from typing import (
    Union,
    List,
    Dict,
)

from .key import Key
from .metadata import Metadata
from .background import Background
from .utils import (
    key_sort_criteria,
    record_change,
    reorder_labels,
    reduced_text_sizes,
    undo_align,
    compare_text_sizes,
    playback_key_changes,
    playback_metadata_changes,
)
from .exceptions import (
    DeserializeException,
)

getcontext().prec = 64


class Keyboard:
    """Class for storing KLE Keyboard.

    :ivar metadata: the metadata, defaults to metadata
    :vartype metadata: Metadata
    :ivar keys: defaults to []
    :vartype keys: List[Key]
    """

    @classmethod
    def from_json(cls, keyboard_json: List[Union[Dict, List[Union[str, Dict]]]]) -> Keyboard:
        """Deserializes a KLE json array into a keyboard.

        :param keyboard_json: the KLE formatted json
        :type keyboard_json: List[Union[Dict, List[Union[str, Dict]]]]
        :raises DeserializeException: keyboard_json is not an array
        :raises DeserializeException: rotation changes not made at beginning of row
        :raises DeserializeException: metadata specified but not first item in keyboard_json
        :raises DeserializeException: a row in the json is not an expected type
        :return: the Keyboard
        :rtype: Keyboard
        """
        if type(keyboard_json) != list:
            raise DeserializeException(
                "Expected an array of objects:", keyboard_json)

        # track rotation info for reset x/y positions
        # if rotation_angle != 0, it is always specified LAST
        current = Key()  # readies the next key data when str encountered
        keyboard = Keyboard()
        align = 4

        # keys are row separated by clusters, clusters defines
        cluster_rotation_x = Decimal(0.0)
        cluster_rotation_y = Decimal(0.0)

        # for object in list
        for r in range(len(keyboard_json)):
            if type(keyboard_json[r]) is list:
                # for item in list
                for k in range(len(keyboard_json[r])):
                    item = keyboard_json[r][k]
                    if type(item) is str:
                        label = item
                        # create copy of key data
                        new_key = deepcopy(current, {})

                        # calculate generated values
                        new_key.width2 = (
                            current.width
                            if new_key.width2 == 0
                            else current.width2
                        )
                        new_key.height2 = (
                            current.height
                            if new_key.height2 == 0
                            else current.height2
                        )
                        new_key.text_labels = undo_align(
                            label.split("\n"),
                            align,
                            ""
                        )
                        new_key.text_sizes = undo_align(
                            new_key.text_sizes,
                            align,
                            None
                        )
                        # clean up generated data
                        for i in range(12):
                            if not new_key.text_labels[i]:
                                new_key.text_sizes[i] = None
                                new_key.text_colors[i] = None
                            if new_key.text_sizes[i] == new_key.default_text_size:
                                new_key.text_sizes[i] = None
                            if new_key.text_colors[i] == new_key.default_text_color:
                                new_key.text_colors[i] = None
                        # add key
                        keyboard.keys.append(new_key)

                        # adjustments for next key gen
                        current.x += Decimal(current.width)
                        current.width = Decimal(1)
                        current.height = Decimal(1)
                        current.x2 = Decimal(0)
                        current.y2 = Decimal(0)
                        current.width2 = Decimal(0)
                        current.height2 = Decimal(0)
                        current.nub = False
                        current.stepped = False
                        current.decal = False
                    elif type(item) is dict:
                        key_changes = item
                        if k != 0 and (
                            "r" in key_changes or
                            "rx" in key_changes or
                            "ry" in key_changes
                        ):
                            raise DeserializeException(
                                "Rotation changes can only be made at the \
                                beginning of the row:",
                                keyboard_json[r]
                            )
                        # rotation changes can only be specified at beginning of row
                        (
                            align,
                            cluster_rotation_x,
                            cluster_rotation_y,
                        ) = playback_key_changes(
                            current,
                            key_changes,
                            align,
                            cluster_rotation_x,
                            cluster_rotation_y
                        )
                    else:
                        raise DeserializeException(
                            f"Expected an object specifying key changes or a label \
                            for a key",
                            item
                        )
                current.y += Decimal(1.0)
            elif type(keyboard_json[r]) is dict:
                metadata_changes = keyboard_json[r]
                if r != 0:
                    raise DeserializeException(
                        f"Keyboard metadata can only be at index 0, is index {r}:",
                        keyboard_json[r]
                    )
                playback_metadata_changes(keyboard.metadata, metadata_changes)
            else:
                raise DeserializeException(
                    f"Unexpected row type: {type(keyboard_json[r])}",
                    keyboard_json[r]
                )
            current.x = Decimal(current.rotation_x)
        return keyboard

    def __init__(self):
        self.metadata = Metadata()
        self.keys = []

    def to_json(self: Keyboard) -> List[Union[Dict, List[Union[str, Dict]]]]:
        """Serializes the Keyboard to a KLE formatted json.

        :param keyboard: the keyboard to deserialize
        :type keyboard: Keyboard
        :return: the KLE formatted json
        :rtype: List[Union[Dict, List[Union[str, Dict]]]]
        """
        # current key that we track
        keyboard_json = list()
        row = list()
        current = Key()
        current.text_colors = current.default_text_color
        align = 4
        cluster_rotation_angle = Decimal(0.0)
        cluster_rotation_x = Decimal(0.0)
        cluster_rotation_y = Decimal(0.0)

        metadata_changes = OrderedDict()
        default_metadata = Metadata()
        record_change(
            metadata_changes,
            "backcolor",
            self.metadata.background_color,
            default_metadata.background_color,
        )
        record_change(
            metadata_changes,
            "name",
            self.metadata.name,
            default_metadata.name,
        )
        record_change(
            metadata_changes,
            "author",
            self.metadata.author,
            default_metadata.author,
        )
        record_change(
            metadata_changes,
            "notes",
            self.metadata.notes,
            default_metadata.notes,
        )
        background_changes = OrderedDict()
        default_background = Background()
        record_change(
            background_changes,
            "name",
            self.metadata.background.name,
            default_background.name,
        )
        record_change(
            background_changes,
            "style",
            self.metadata.background.style,
            default_background.style,
        )
        if len(background_changes) > 0:
            record_change(
                metadata_changes,
                "background",
                background_changes,
                None
            )
        record_change(
            metadata_changes,
            "radii",
            self.metadata.radii,
            default_metadata.radii,
        )
        record_change(
            metadata_changes,
            "switchMount",
            self.metadata.switch_mount,
            default_metadata.switch_mount,
        )
        record_change(
            metadata_changes,
            "switchBrand",
            self.metadata.switch_brand,
            default_metadata.switch_brand,
        )
        record_change(
            metadata_changes,
            "switchType",
            self.metadata.switch_type,
            default_metadata.switch_type,
        )
        record_change(
            metadata_changes,
            "css",
            self.metadata.css,
            default_metadata.css,
        )
        if (
            self.metadata.plate != default_metadata.plate or
            self.metadata._include_plate
        ):
            record_change(
                metadata_changes,
                "plate",
                self.metadata.plate,
                None,
            )
        if (
            self.metadata.pcb != default_metadata.pcb or
            self.metadata._include_pcb
        ):
            record_change(
                metadata_changes,
                "pcb",
                self.metadata.pcb,
                None,
            )
        if len(metadata_changes) > 0:
            keyboard_json.append(metadata_changes)

        is_new_row = True
        current.y -= Decimal(1)  # will be incremented on first row

        sorted_keys = list(sorted(self.keys, key=key_sort_criteria))
        for key in sorted_keys:
            key_changes = OrderedDict()
            ordered = reorder_labels(key, current)

            # start a new row when necessary
            is_cluster_changed = (
                (key.rotation_angle != cluster_rotation_angle) or
                (key.rotation_x != cluster_rotation_x) or
                (key.rotation_y != cluster_rotation_y)
            )
            is_row_changed = (key.y != current.y)
            if len(row) > 0 and (is_row_changed or is_cluster_changed):
                # set up for the new row
                keyboard_json.append(row)
                row = list()
                is_new_row = True

            if is_new_row:
                current.y += Decimal(1.0)

                # set up for the new row
                # y is reset if either rx or ry are changed
                if (
                    key.rotation_y != cluster_rotation_y or
                    key.rotation_x != cluster_rotation_x
                ):
                    current.y = key.rotation_y
                # always reset x to rx (which defaults to zero)
                current.x = key.rotation_x

                # update current cluster
                cluster_rotation_angle = key.rotation_angle
                cluster_rotation_x = key.rotation_x
                cluster_rotation_y = key.rotation_y

                is_new_row = False

            current.rotation_angle = record_change(
                key_changes,
                "r",
                key.rotation_angle,
                current.rotation_angle,
            )
            current.rotation_x = record_change(
                key_changes,
                "rx",
                key.rotation_x,
                current.rotation_x,
            )
            current.rotation_y = record_change(
                key_changes,
                "ry",
                key.rotation_y,
                current.rotation_y,
            )
            current.y += record_change(
                key_changes,
                "y",
                key.y - current.y,
                Decimal(0.0),
            )
            current.x += record_change(
                key_changes,
                "x",
                key.x - current.x,
                Decimal(0.0),
            ) + key.width
            current.color = record_change(
                key_changes,
                "c",
                key.color,
                current.color,
            )
            # if statement for ordered color
            if not ordered["text_color"][0]:
                ordered["text_color"][0] = key.default_text_color
            else:
                for i in range(2, 12):
                    if (
                        ordered["text_color"][i] != "" and
                        ordered["text_color"][i] != ordered["text_color"][0]
                    ):
                        # maybe an error in the original referenced source code here
                        ordered["text_color"][i] = key.default_text_color
            current.text_colors = record_change(
                key_changes,
                "t",
                "\n".join(
                    map(
                        lambda text_color: "" if text_color is None else text_color,
                        ordered["text_color"]
                    )
                ).rstrip(),
                current.text_colors
            )
            current.ghost = record_change(
                key_changes,
                "g",
                key.ghost,
                current.ghost,
            )
            current.profile = record_change(
                key_changes,
                "p",
                key.profile,
                current.profile,
            )
            current.sm = record_change(
                key_changes,
                "sm",
                key.switch_mount,
                current.switch_mount,
            )
            current.sb = record_change(
                key_changes,
                "sb",
                key.switch_brand,
                current.switch_brand,
            )
            current.st = record_change(
                key_changes,
                "st",
                key.switch_type,
                current.switch_type,
            )
            align = record_change(
                key_changes,
                "a",
                ordered["align"],
                align,
            )
            current.default_text_size = record_change(
                key_changes,
                "f",
                key.default_text_size,
                current.default_text_size,
            )
            if "f" in key_changes:
                current.text_sizes = [None for i in range(12)]
            # if text sizes arent already optimized, optimize it
            if not compare_text_sizes(
                current.text_sizes,
                ordered["text_size"],
                ordered["labels"]
            ):
                if (len(reduced_text_sizes(ordered["text_size"])) == 0):
                    # force f to be written
                    record_change(
                        key_changes,
                        "f",
                        key.default_text_size,
                        -1,
                    )
                else:
                    optimizeF2 = not bool(ordered["text_size"][0])
                    for i in range(2, len(reduced_text_sizes(ordered["text_size"]))):
                        if not optimizeF2:
                            break
                        optimizeF2 = (
                            ordered["text_size"][i] == ordered["text_size"][1]
                        )
                    if optimizeF2:
                        f2 = ordered["text_size"][1]
                        # current.f2 not ever used
                        # removed current.f2 = serializeProp(props, "f2", f2, -1);
                        record_change(key_changes, "f2", f2, -1)
                        current.text_sizes = [0] + [f2 for i in range(11)]
                    else:
                        current.text_sizes = ordered["text_size"]
                        record_change(
                            key_changes,
                            "fa",
                            reduced_text_sizes(ordered["text_size"]),
                            [],
                        )
            record_change(key_changes, "w", key.width, Decimal(1.0))
            record_change(key_changes, "h", key.height, Decimal(1.0))
            record_change(key_changes, "w2", key.width2, key.width)
            record_change(key_changes, "h2", key.height2, key.height)
            record_change(key_changes, "x2", key.x2, Decimal(0.0))
            record_change(key_changes, "y2", key.y2, Decimal(0.0))
            record_change(key_changes, "n", key.nub, False)
            record_change(key_changes, "l", key.stepped, False)
            record_change(key_changes, "d", key.decal, False)
            if len(key_changes) > 0:
                row.append(key_changes)
            current.text_labels = ordered["labels"]
            row.append("\n".join(ordered["labels"]).rstrip())
        if len(row) > 0:
            keyboard_json.append(row)
        return keyboard_json
