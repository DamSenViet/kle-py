from copy import deepcopy
from decimal import Decimal

class Key:
    """Class that holds data of a `Key` instance for a `Keyboard`.

    Attributes:
        color {str} -- Background color of the key in hex.
        labels {list} -- The list of legends.
        text_color {list} -- The text color for the legends.
        text_size {list} -- The text size for the legends.
        default {dict} -- The defaults used when label in default position.
        x {Decimal} -- The x coordinate of the key before rotation.
        y {Decimal} -- The y coordinate of the key before rotation.
        width {Decimal} -- Width of the key.
        height {Decimal} -- Height of the key.
        x2 {Decimal} -- Duplicate x coordinate of the key???
        y2 {Decimal} -- Duplicate y coordinate of the key???
        width2 {Decimal} -- Duplicate width of the key???
        height2 {Decimal} -- Duplicate height of the key???
        rotation_x {Decimal} -- X coordinate of the rotation origin.
        rotation_y {Decimal} -- Y coordinate of the rotation origin
        rotation_angle {Decimal} -- Rotation angle about the rotation origin
        decal {bool} -- Specifies whether key is treated as a decoration.
        ghost {bool} -- Specifies whether key should be rendered transparently.
        stepped {bool} -- Specifies whether part of key is lower than rest.
        nub {bool} -- Specifies whether key is a homing key.
        profile {str} -- Specifies the profile of the key.
        sm {str} -- Switch mount.
        sb {str} -- Switch brand.
        st {str} -- Switch type.
    """

    def __init__(
        self,
        color: str = "#cccccc",
        labels: list = list(),
        text_color: list = [None for i in range(12)],
        text_size: list = [None for i in range(12)],
        default: dict = {
            "text_color": "#000000",
            "text_size": 3
        },
        x: Decimal = Decimal(0.0),
        y: Decimal = Decimal(0.0),
        width: Decimal = Decimal(1.0),
        height: Decimal = Decimal(1.0),
        x2: Decimal  = Decimal(0.0),
        y2: Decimal = Decimal(0.0),
        width2: Decimal = Decimal(1.0),
        height2: Decimal = Decimal(1.0),
        rotation_x: Decimal = Decimal(0.0),
        rotation_y: Decimal = Decimal(0.0),
        rotation_angle: Decimal = Decimal(0.0),
        decal: bool = False,
        ghost: bool = False,
        stepped: bool = False,
        nub: bool = False,
        profile: str = None,
        sm: str = None,
        sb: str = None,
        st: str = None
    ) -> None:
        """Construct a new `Key`. Default arguments provided.

        Keyword Arguments:
            color {str} -- Background color of the key in hex.
                           (default: {`"#cccccc"`})
            labels {list} -- The list of legends.
                             (default: {`list()`})
            text_color {list} -- The text color for the legends.
                                (default: {`[None for i in range(12)]`})
            text_size {list} -- The text size for the legends.
                               (default: {`[None for i in range(12)]`})
            default {dict} -- The defaults used when label in default position.
                              (default: {`{"text_color": "#000000","text_size": 3}`})
            x {Decimal} -- The x coordinate of the key before rotation.
                           (default: {`Decimal(0.0)`})
            y {Decimal} -- The y coordinate of the key before rotation.
                           (default: {`Decimal(0.0)`})
            width {Decimal} -- Width of the key. (default: {`Decimal(1.0)`})
            height {Decimal} -- Height of the key. (default: {`Decimal(1.0)`})
            x2 {Decimal} -- Duplicate x coordinate of the key???
                            (default: {`Decimal(0.0)`})
            y2 {Decimal} -- Duplicate y coordinate of the key???
                            (default: {`Decimal(0.0)`})
            width2 {Decimal} -- Duplicate width of the key???
                                (default: {`Decimal(1.0)`})
            height2 {Decimal} -- Duplicate height of the key???
                                 (default: {`Decimal(1.0)`})
            rotation_x {Decimal} -- X coordinate of the rotation origin.
                                    (default: {`Decimal(0.0)`})
            rotation_y {Decimal} -- Y coordinate of the rotation origin
                                    (default: {`Decimal(0.0)`})
            rotation_angle {Decimal} -- Rotation angle about the rotation origin
                                        (default: {`Decimal(0.0)`})
            decal {bool} -- Specifies whether key is treated as a decoration.
                            (default: {`False`})
            ghost {bool} -- Specifies whether key should be rendered transparently.
                            (default: {`False`})
            stepped {bool} -- Specifies whether part of key is lower than rest.
                              (default: {`False`})
            nub {bool} -- Specifies whether key is a homing key.
                          (default: {`False`})
            profile {str} -- Specifies the profile of the key.
                             (default: {`None`})
            sm {str} -- Switch mount. (default: {`None`})
            sb {str} -- Switch brand. (default: {`None`})
            st {str} -- Switch type. (default: {`None`})
        """
        self.color = color
        self.labels = labels
        self.text_color = text_color
        self.text_size = text_size
        self.default = default
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

    def __deepcopy__(self, memo: dict = None) -> "Key":
        """Creates a deepcopy of the key.

        Arguments:
            memo {dict} -- A dict of references for deep copy process.
                           (default: {`None`})

        Returns:
            Key -- A duplicate of the key.
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.labels = deepcopy(self.labels, memo)
        new_key.text_color = deepcopy(self.text_color, memo)
        new_key.text_size = deepcopy(self.text_size, memo)
        return new_key
