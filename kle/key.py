from copy import deepcopy

class Key:
    def __init__(
        self,
        color: str = "#cccccc",
        labels: list = list(),
        textColor: list = [None for i in range(12)],
        textSize: list = [None for i in range(12)],
        default: dict = {
            "textColor": "#000000",
            "textSize": 3
        },
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

    def __deepcopy__(self, memo):
        newKey = type(self)()
        memo[id(self)] = newKey
        newKey.__dict__.update(self.__dict__)
        newKey.labels = deepcopy(self.labels, memo)
        newKey.textColor = deepcopy(self.textColor, memo)
        newKey.textSize = deepcopy(self.textSize, memo)
        return newKey
