from __future__ import annotations
from copy import (
    deepcopy,
)
from decimal import (
    Decimal,
    getcontext,
)
from typing import (
    cast,
    Union,
    List,
    Dict,
)

from typeguard import typechecked

from .metadata import Metadata
from .background import Background
from .key import Key
from .label import Label
from .utils import (
    key_sort_criteria,
    record_change,
    aligned_key_properties,
    reduced_text_sizes,
    unaligned,
    compare_text_sizes,
    playback_key_changes,
    playback_metadata_changes,
)
from .exceptions import (
    DeserializeException,
)

getcontext().prec = 64

Keyboard_JSON = List[Union[Dict, List[Union[str, Dict]]]]


class Keyboard:
    """Class for storing KLE Keyboard.

    :ivar metadata: the metadata, defaults to metadata
    :vartype metadata: Metadata
    :ivar keys: defaults to []
    :vartype keys: List[Key]
    """

    @classmethod
    def from_json(cls, keyboard_json: Keyboard_JSON) -> Keyboard:
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

        keyboard: Keyboard = Keyboard()

        # tracks the key with accumulated changes
        current: Key = Key()
        # tmp variables to construct final labels
        align: int = 4
        # keys are row separated by clusters
        # track rotation info for reset x/y positions
        cluster_rotation_x: Decimal = Decimal(0.0)
        cluster_rotation_y: Decimal = Decimal(0.0)

        # for object in list
        for r in range(len(keyboard_json)):
            if type(keyboard_json[r]) is list:
                # for item in list
                for k in range(len(keyboard_json[r])):
                    item: Union[str, dict] = cast(
                        Union[str, dict],
                        keyboard_json[r][k],
                    )
                    if type(item) is str:
                        labels: str = item
                        # create copy of key data
                        new_key: Key = deepcopy(current)
                        if new_key.get_width2() != 0:
                            new_key.set_width2(current.get_width2())
                        else:
                            new_key.set_width2(current.get_width())
                        if new_key.get_height2() != 0:
                            new_key.set_height2(current.get_height2())
                        else:
                            new_key.set_height2(current.get_height())
                        for i, text in enumerate(unaligned(
                            labels.split("\n"),
                            align,
                            "",
                        )):
                            new_key.get_labels()[i].set_text(text)

                        for i, size in enumerate(unaligned(
                            [
                                label.get_size()
                                for label in new_key.get_labels()
                            ],
                            align,
                            0,
                        )):
                            new_key.get_labels()[i].set_size(size)
                        # clean up generated data
                        for label in new_key.get_labels():
                            if label.get_text() == "":
                                label.set_color("")
                                label.set_size(0)
                            if label.get_color() == new_key.get_default_text_color():
                                label.set_color("")
                            if label.get_size() == new_key.get_default_text_size():
                                label.set_size(0)
                        # add key
                        keyboard.keys.append(new_key)

                        # adjustments for the next key
                        current.set_x(current.get_x() +
                                      Decimal(current.get_width()))
                        current.set_width(Decimal(1))
                        current.set_height(Decimal(1))
                        current.set_x2(Decimal(0))
                        current.set_y2(Decimal(0))
                        current.set_width2(Decimal(0))
                        current.set_height2(Decimal(0))
                        current.set_nubbed(False)
                        current.set_stepped(False)
                        current.set_decal(False)
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
                            f"Expected an object specifying key changes or labels \
                            for a key",
                            item
                        )
                current.set_y(current.get_y() + Decimal(1.0))
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
            current.set_x(Decimal(current.get_rotation_x()))
        return keyboard

    def __init__(self):
        self.metadata = Metadata()
        self.keys = []

    def to_json(self: Keyboard) -> Keyboard_JSON:
        """Serializes the Keyboard to a KLE formatted json.

        :param keyboard: the keyboard to deserialize
        :type keyboard: Keyboard
        :return: the KLE formatted json
        :rtype: List[Union[Dict, List[Union[str, Dict]]]]
        """
        keyboard_json: Keyboard_JSON = list()
        row: List[Union[str, Dict]] = list()
        current: Key = Key()
        align: int = 4
        current_labels_color: List[str] = current.get_default_text_color()
        current_labels_size: List[Union[int, float]] = [
            label.get_size()
            for label
            in current.get_labels()
        ]
        cluster_rotation_angle: Decimal = Decimal(0.0)
        cluster_rotation_x: Decimal = Decimal(0.0)
        cluster_rotation_y: Decimal = Decimal(0.0)

        metadata_changes: Dict = dict()
        default_metadata: Metadata = Metadata()
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
        background_changes: Dict = dict()
        default_background: Background = Background()
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
            self.metadata.include_plate
        ):
            record_change(
                metadata_changes,
                "plate",
                self.metadata.plate,
                None,
            )
        if (
            self.metadata.pcb != default_metadata.pcb or
            self.metadata.include_pcb
        ):
            record_change(
                metadata_changes,
                "pcb",
                self.metadata.pcb,
                None,
            )
        if len(metadata_changes) > 0:
            keyboard_json.append(metadata_changes)

        is_new_row: bool = True
        # will be incremented on first row
        current.set_y(current.get_y() - Decimal(1))

        sorted_keys: List[Key] = list(sorted(self.keys, key=key_sort_criteria))
        for key in sorted_keys:
            key_changes = dict()
            (
                alignment,
                aligned_text_labels,
                aligned_text_color,
                aligned_text_size,
            ) = aligned_key_properties(
                key,
                current_labels_size
            )

            # start a new row when necessary
            is_cluster_changed: bool = (
                (key.get_rotation_angle() != cluster_rotation_angle) or
                (key.get_rotation_x() != cluster_rotation_x) or
                (key.get_rotation_y() != cluster_rotation_y)
            )
            is_row_changed: bool = (key.get_y() != current.get_y())
            if len(row) > 0 and (is_row_changed or is_cluster_changed):
                # set up for the new row
                keyboard_json.append(row)
                row = list()
                is_new_row = True

            if is_new_row:
                current.set_y(current.get_y() + Decimal(1.0))

                # set up for the new row
                # y is reset if either rx or ry are changed
                if (
                    key.get_rotation_y() != cluster_rotation_y or
                    key.get_rotation_x() != cluster_rotation_x
                ):
                    current.set_y(key.get_rotation_y())
                # always reset x to rx (which defaults to zero)
                current.set_x(key.get_rotation_x())

                # update current cluster
                cluster_rotation_angle = key.get_rotation_angle()
                cluster_rotation_x = key.get_rotation_x()
                cluster_rotation_y = key.get_rotation_y()

                is_new_row = False

            current.set_rotation_angle(record_change(
                key_changes,
                "r",
                key.get_rotation_angle(),
                current.get_rotation_angle(),
            ))
            current.set_rotation_x(record_change(
                key_changes,
                "rx",
                key.get_rotation_x(),
                current.get_rotation_x(),
            ))
            current.set_rotation_y(record_change(
                key_changes,
                "ry",
                key.get_rotation_y(),
                current.get_rotation_y(),
            ))
            current.set_y(current.get_y() + record_change(
                key_changes,
                "y",
                key.get_y() - current.get_y(),
                Decimal(0.0),
            ))
            current.set_x(current.get_x() + record_change(
                key_changes,
                "x",
                key.get_x() - current.get_x(),
                Decimal(0.0),
            ) + key.get_width())
            current.set_color(record_change(
                key_changes,
                "c",
                key.get_color(),
                current.get_color(),
            ))
            # if statement for ordered color
            if not aligned_text_color[0]:
                aligned_text_color[0] = key.get_default_text_color()
            else:
                for i in range(2, 12):
                    if (
                        aligned_text_color[i] != "" and
                        aligned_text_color[i] != aligned_text_color[0]
                    ):
                        aligned_text_color[i] = key.get_default_text_color()
            current_labels_color = record_change(
                key_changes,
                "t",
                "\n".join(aligned_text_color).rstrip(),
                current_labels_color,
            )
            current.set_ghosted(record_change(
                key_changes,
                "g",
                key.get_ghosted(),
                current.get_ghosted(),
            ))
            current.set_profile(record_change(
                key_changes,
                "p",
                key.get_profile(),
                current.get_profile(),
            ))
            current.set_switch_mount(record_change(
                key_changes,
                "sm",
                key.get_switch_mount(),
                current.get_switch_mount(),
            ))
            current.set_switch_brand(record_change(
                key_changes,
                "sb",
                key.get_switch_brand(),
                current.get_switch_brand(),
            ))
            current.set_switch_type(record_change(
                key_changes,
                "st",
                key.get_switch_type(),
                current.get_switch_type(),
            ))
            align = record_change(
                key_changes,
                "a",
                alignment,
                align,
            )
            current.set_default_text_size(record_change(
                key_changes,
                "f",
                key.get_default_text_size(),
                current.get_default_text_size(),
            ))
            if "f" in key_changes:
                current_labels_size = [0 for i in range(12)]
            # if text sizes arent already optimized, optimize it
            if not compare_text_sizes(
                current_labels_size,
                aligned_text_size,
                aligned_text_labels
            ):
                if (len(reduced_text_sizes(aligned_text_size)) == 0):
                    # force f to be written
                    record_change(
                        key_changes,
                        "f",
                        key.get_default_text_size(),
                        -1,
                    )
                else:
                    optimizeF2: bool = not bool(aligned_text_size[0])
                    for i in range(2, len(reduced_text_sizes(aligned_text_size))):
                        if not optimizeF2:
                            break
                        optimizeF2 = (
                            aligned_text_size[i] == aligned_text_size[1]
                        )
                    if optimizeF2:
                        f2: Union[int, float] = aligned_text_size[1]
                        # current.f2 not ever used
                        # removed current.f2 = serializeProp(props, "f2", f2, -1);
                        record_change(key_changes, "f2", f2, -1)
                        current_labels_size = [0] + [f2 for i in range(11)]
                    else:
                        current_labels_size = aligned_text_size
                        record_change(
                            key_changes,
                            "fa",
                            reduced_text_sizes(aligned_text_size),
                            [],
                        )
            record_change(key_changes, "w", key.get_width(), Decimal(1.0))
            record_change(key_changes, "h", key.get_height(), Decimal(1.0))
            record_change(key_changes, "w2", key.get_width2(), key.get_width())
            record_change(key_changes, "h2",
                          key.get_height2(), key.get_height())
            record_change(key_changes, "x2", key.get_x2(), Decimal(0.0))
            record_change(key_changes, "y2", key.get_y2(), Decimal(0.0))
            record_change(key_changes, "n", key.get_nubbed(), False)
            record_change(key_changes, "l", key.get_stepped(), False)
            record_change(key_changes, "d", key.get_decal(), False)
            if len(key_changes) > 0:
                row.append(key_changes)
            row.append("\n".join(aligned_text_labels).rstrip())
        if len(row) > 0:
            keyboard_json.append(row)
        return keyboard_json
