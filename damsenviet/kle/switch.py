from typeguard import typechecked
from .utils import autorepr

__all__ = ["Switch"]


class Switch:
    """Class storing Switch."""

    def __init__(self) -> None:
        """Instantiates a switch."""
        self.__mount: str = ""
        self.__brand: str = ""
        self.__type: str = ""

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return autorepr(
            self,
            {
                "mount": self.mount,
                "brand": self.brand,
                "type": self.type,
            },
        )

    @property
    def mount(self) -> str:
        """Switch mount.

        :getter: gets switch mount
        :setter: sets switch mount
        :type: str
        """
        return self.__mount

    @mount.setter
    @typechecked
    def mount(self, mount: str) -> None:
        self.__mount = mount

    @property
    def brand(self) -> str:
        """Switch brand.

        :getter: gets switch brand
        :setter: sets switch brand
        :rtype: str
        """
        return self.__brand

    @brand.setter
    @typechecked
    def brand(self, brand: str) -> None:
        self.__brand = brand

    @property
    def type(self) -> str:
        """Switch type part id.

        :getter: gets switch type part id
        :setter: gets switch type part id
        :rtype: str
        """
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type
