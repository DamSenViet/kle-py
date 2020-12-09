from __future__ import annotations
from copy import deepcopy
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
    """Class storing Keyboard."""

    def __init__(self):
        """Initializes a Keyboard."""
        self.metadata: Metadata = Metadata()
        self.keys: List[Key] = []

    @property
    def metadata(self) -> Metadata:
        """Gets metadata.

        :return: metadata reference
        :rtype: Metadata
        """
        return self.__metadata

    @metadata.setter
    @typechecked
    def metadata(self, metadata: Metadata) -> None:
        """Sets metadata.

        :param metadata: metadata reference
        :type metadata: Metadata
        """
        self.__metadata = metadata

    @property
    @typechecked
    def keys(self) -> List[Key]:
        """Gets key references.

        :return: list of Key references
        :rtype: List[Key]
        """
        return self.__keys

    @keys.setter
    @typechecked
    def keys(self, keys: List[Key]) -> None:
        """Sets keys references.

        :param keys: list of Key references
        :type keys: List[Key]
        """
        self.__keys = keys

    @classmethod
    def from_json(cls, keyboard_json: Keyboard_JSON) -> Keyboard:
        """Deserializes a KLE json array into a keyboard.

        :param keyboard_json: the KLE formatted json
        :type keyboard_json: List[Union[Dict, List[Union[str, Dict]]]]
        :raises DeserializeException: keyboard_json is not an array
        :raises DeserializeException: rotation changes not at beginning of row
        :raises DeserializeException: metadata specified but not as first item
        :raises DeserializeException: item not expected type
        :return: the Keyboard
        :rtype: Keyboard
        """
        if type(keyboard_json) != list:
            raise DeserializeException(
                message="Expected an array of objects:",
                payload=keyboard_json,
            )

        keyboard: Keyboard = Keyboard()

        # tracks the key with accumulated changes
        current: Key = Key()
        # allows for non-KLE defaults for label initializer
        current_labels_size = [0 for label in current.labels]
        current_labels_color = ["" for label in current.labels]
        # tmp variables to construct final labels
        alignment: int = 4
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
                        if new_key.width2 != 0:
                            new_key.width2 = current.width2
                        else:
                            new_key.width2 = current.width
                        if new_key.height2 != 0:
                            new_key.height2 = current.height2
                        else:
                            new_key.height2 = current.height
                        for i, text in enumerate(
                            unaligned(
                                labels.split("\n"),
                                alignment,
                                "",
                            )
                        ):
                            new_key.labels[i].text = text

                        for i, size in enumerate(
                            unaligned(current_labels_size, alignment, 0)
                        ):
                            if size == 0:
                                new_key.labels[i].size = new_key.default_text_size
                            else:
                                new_key.labels[i].size = size

                        for i, color in enumerate(current_labels_color):
                            if color == "":
                                new_key.labels[i].color = new_key.default_text_color
                            else:
                                new_key.labels[i].color = color

                        # add key
                        keyboard.keys.append(new_key)

                        # adjustments for the next key
                        current.x = current.x + Decimal(current.width)
                        current.width = Decimal(1)
                        current.height = Decimal(1)
                        current.x2 = Decimal(0)
                        current.y2 = Decimal(0)
                        current.width2 = Decimal(0)
                        current.height2 = Decimal(0)
                        current.is_homing = False
                        current.is_stepped = False
                        current.is_decal = False

                    elif type(item) is dict:
                        key_changes = item
                        if k != 0 and (
                            "r" in key_changes
                            or "rx" in key_changes
                            or "ry" in key_changes
                        ):
                            message = (
                                "rotataion changes can only be made at the"
                                + "beginning of the row"
                            )
                            raise DeserializeException(
                                message=message,
                                payload=keyboard_json[r],
                            )
                        # rotation changes can only be specified at beginning
                        # at the start of the row
                        (
                            current_labels_color,
                            current_labels_size,
                            alignment,
                            cluster_rotation_x,
                            cluster_rotation_y,
                        ) = playback_key_changes(
                            current,
                            key_changes,
                            current_labels_color,
                            current_labels_size,
                            alignment,
                            cluster_rotation_x,
                            cluster_rotation_y,
                        )
                    else:
                        message = (
                            "expected an object specifying key changes or"
                            "text labels for a key"
                        )
                        raise DeserializeException(
                            message=message,
                            payload=item,
                        )
                current.y = current.y + Decimal(1.0)
            elif type(keyboard_json[r]) is dict:
                metadata_changes = keyboard_json[r]
                if r != 0:
                    raise DeserializeException(
                        "metadata can only be specified as first item",
                        keyboard_json[r],
                    )
                playback_metadata_changes(keyboard.metadata, metadata_changes)
            else:
                message = (
                    "encountered unexpected type of "
                    f"{type(keyboard_json[r]).__name__}"
                )
                raise DeserializeException(message=message, payload=keyboard_json[r])
            current.x = Decimal(current.rotation_x)
        return keyboard

    def to_json(self) -> Keyboard_JSON:
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
        current_labels_color: List[str] = current.default_text_color
        # allows for non-KLE defaults for label initializer, can maintain value invariants
        current_labels_size: List[Union[int, float]] = [0 for label in current.labels]
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
            self.__metadata.background.style,
            default_background.style,
        )
        if len(background_changes) > 0:
            record_change(metadata_changes, "background", background_changes, None)
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
        if self.metadata.include_switches_plate_mounted or (
            self.metadata.is_switches_plate_mounted
            != default_metadata.is_switches_plate_mounted
        ):
            record_change(
                metadata_changes,
                "plate",
                self.metadata.is_switches_plate_mounted,
                None,
            )
        if self.metadata.include_switches_pcb_mounted or (
            self.metadata.is_switches_pcb_mounted
            != default_metadata.is_switches_pcb_mounted
        ):
            record_change(
                metadata_changes,
                "pcb",
                self.metadata.is_switches_pcb_mounted,
                None,
            )
        if len(metadata_changes) > 0:
            keyboard_json.append(metadata_changes)

        is_new_row: bool = True
        # will be incremented on first row
        current.y = current.y - Decimal(1)

        sorted_keys: List[Key] = list(sorted(self.__keys, key=key_sort_criteria))
        for key in sorted_keys:
            key_changes = dict()
            (
                alignment,
                aligned_text_labels,
                aligned_text_color,
                aligned_text_size,
            ) = aligned_key_properties(
                key,
                current_labels_size,
            )

            # start a new row when necessary
            is_cluster_changed: bool = (
                (key.rotation_angle != cluster_rotation_angle)
                or (key.rotation_x != cluster_rotation_x)
                or (key.rotation_y != cluster_rotation_y)
            )
            is_row_changed: bool = key.y != current.y
            if len(row) > 0 and (is_row_changed or is_cluster_changed):
                # set up for the new row
                keyboard_json.append(row)
                row = list()
                is_new_row = True

            if is_new_row:
                current.y = current.y + Decimal(1.0)

                # set up for the new row
                # y is reset if either rx or ry are changed
                if (
                    key.rotation_y != cluster_rotation_y
                    or key.rotation_x != cluster_rotation_x
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
            current.y = current.y + record_change(
                key_changes,
                "y",
                key.y - current.y,
                Decimal(0.0),
            )
            current.x = (
                current.x
                + record_change(
                    key_changes,
                    "x",
                    key.x - current.x,
                    Decimal(0.0),
                )
                + key.width
            )
            current.color = record_change(
                key_changes,
                "c",
                key.color,
                current.color,
            )
            # if statement for ordered color
            if not aligned_text_color[0]:
                aligned_text_color[0] = key.default_text_color
            else:
                for i in range(2, 12):
                    if (
                        aligned_text_color[i] != ""
                        and aligned_text_color[i] != aligned_text_color[0]
                    ):
                        aligned_text_color[i] = key.default_text_color
            current_labels_color = record_change(
                key_changes,
                "t",
                "\n".join(aligned_text_color).rstrip(),
                current_labels_color,
            )
            current.is_ghosted = record_change(
                key_changes,
                "g",
                key.is_ghosted,
                current.is_ghosted,
            )
            current.profile_and_row = record_change(
                key_changes,
                "p",
                key.profile_and_row,
                current.profile_and_row,
            )
            current.switch_mount = record_change(
                key_changes,
                "sm",
                key.switch_mount,
                current.switch_mount,
            )
            current.switch_brand = record_change(
                key_changes,
                "sb",
                key.switch_brand,
                current.switch_brand,
            )
            current.switch_type = record_change(
                key_changes,
                "st",
                key.switch_type,
                current.switch_type,
            )
            align = record_change(
                key_changes,
                "a",
                alignment,
                align,
            )
            current.default_text_size = record_change(
                key_changes,
                "f",
                key.default_text_size,
                current.default_text_size,
            )
            if "f" in key_changes:
                current_labels_size = [0 for i in range(12)]
            # if text sizes arent already optimized, optimize it
            if not compare_text_sizes(
                current_labels_size, aligned_text_size, aligned_text_labels
            ):
                if len(reduced_text_sizes(aligned_text_size)) == 0:
                    # force f to be written
                    record_change(
                        key_changes,
                        "f",
                        key.default_text_size,
                        -1,
                    )
                else:
                    optimizeF2: bool = not bool(aligned_text_size[0])
                    for i in range(2, len(reduced_text_sizes(aligned_text_size))):
                        if not optimizeF2:
                            break
                        optimizeF2 = aligned_text_size[i] == aligned_text_size[1]
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
            record_change(key_changes, "w", key.width, Decimal(1.0))
            record_change(key_changes, "h", key.height, Decimal(1.0))
            record_change(key_changes, "w2", key.width2, key.width)
            record_change(key_changes, "h2", key.height2, key.height)
            record_change(key_changes, "x2", key.x2, Decimal(0.0))
            record_change(key_changes, "y2", key.y2, Decimal(0.0))
            record_change(key_changes, "n", key.is_homing, False)
            record_change(key_changes, "l", key.is_stepped, False)
            record_change(key_changes, "d", key.is_decal, False)
            if len(key_changes) > 0:
                row.append(key_changes)
            row.append("\n".join(aligned_text_labels).rstrip())
        if len(row) > 0:
            keyboard_json.append(row)
        return keyboard_json
