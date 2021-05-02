__all__ = ["Switch"]


class Switch:
    """Switch information."""

    def __init__(self) -> None:
        """Initializes a Switch."""
        self.__mount: str = ""
        self.__brand: str = ""
        self.__type: str = ""

    @property
    def mount(self) -> str:
        """Switch mount."""
        return self.__mount

    @mount.setter
    def mount(self, mount: str) -> None:
        self.__mount = mount

    @property
    def brand(self) -> str:
        """Switch brand."""
        return self.__brand

    @brand.setter
    def brand(self, brand: str) -> None:
        self.__brand = brand

    @property
    def type(self) -> str:
        """Switch type part id."""
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type
