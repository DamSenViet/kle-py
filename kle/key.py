import copy
import decimal as dec

class Key:
    """Class that holds data of a `Key` instance for a `Keyboard`."""

    def __init__(
        self,
        color: str = "#cccccc",
        labels: list = [None for i in range(12)],
        text_color: list = [None for i in range(12)],
        text_size: list = [None for i in range(12)],
        default: dict = {
            "text_color": "#000000",
            "text_size": 3
        },
        x: dec.Decimal = dec.Decimal(0.0),
        y: dec.Decimal = dec.Decimal(0.0),
        width: dec.Decimal = dec.Decimal(1.0),
        height: dec.Decimal = dec.Decimal(1.0),
        x2: dec.Decimal  = dec.Decimal(0.0),
        y2: dec.Decimal = dec.Decimal(0.0),
        width2: dec.Decimal = dec.Decimal(1.0),
        height2: dec.Decimal = dec.Decimal(1.0),
        rotation_x: dec.Decimal = dec.Decimal(0.0),
        rotation_y: dec.Decimal = dec.Decimal(0.0),
        rotation_angle: dec.Decimal = dec.Decimal(0.0),
        decal: bool = False,
        ghost: bool = False,
        stepped: bool = False,
        nub: bool = False,
        profile: str = None,
        sm: str = None,
        sb: str = None,
        st: str = None
    ):
        """Construct a new `Key`. Default arguments provided.

        :param color: The background color (hex code) of the key, defaults to
            "#cccccc".
        :type color: str
        :param labels: The list of legends, defaults to
            [None for i in range(12)].
        :type labels: list
        :param text_color: The text color (hex code) for the legends, defaults
            to [None for i in range(12)].
        :type text_color: list
        :param text_size: The text size for the legends, defaults to
            [None for i in range(12)].
        :type text_size: list
        :param default: The defaults used when label in default position,
            defaults to {"text_color": "#000000", "text_size": 3}.
        :type default: dict
        :param x: The x coordinate of the key before rotation.
        :type x: dec.Decimal
        :param y: The y coordinate of the key before rotation.
        :type y: dec.Decimal
        :param width: Width of the key.
        :type width: dec.Decimal
        :param height: Height of the key.
        :type height: dec.Decimal
        :param x2: Duplicate x coordinate of the key???
        :type x2: dec.Decimal
        :param y2: Duplicate y coordinate of the key???
        :type y2: dec.Decimal
        :param width2: Duplicate width of the key???
        :type width2: dec.Decimal
        :param height2: Duplicate height of the key???
        :type height2: dec.Decimal
        :param rotation_x: X coordinate of the rotation origin.
        :type rotation_x: dec.Decimal
        :param rotation_y: Y coordinate of the rotation origin.
        :type rotation_y: dec.Decimal
        :param rotation_angle: Rotation angle about the rotation origin.
        :type rotation_angle: dec.Decimal
        :param decal: Specifies whether key is treated as a decoration.
        :type decal: bool
        :param ghost: Specifies whether key should be rendered transparently.
        :type ghost: bool
        :param stepped: Specifies whether part of key is lower than rest.
        :type stepped: bool
        :param nub: Specifies whether key is a homing key.
        :type nub: bool
        :param profile: The profile/sculpt of the key.
        :type profile: str
        :param sm: The switch mount of the key.
        :type sm: str
        :param sb: The switch brand of the key.
        :type sb: str
        :param st: The switch mount of the key.
        :type st: str
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
        """Creates a deep copy of the key.

        :return: A duplicate of the key.
        :rtype: Key
        """
        new_key = type(self)()
        memo[id(self)] = new_key
        new_key.__dict__.update(self.__dict__)
        new_key.labels = copy.deepcopy(self.labels, memo)
        new_key.text_color = copy.deepcopy(self.text_color, memo)
        new_key.text_size = copy.deepcopy(self.text_size, memo)
        return new_key
