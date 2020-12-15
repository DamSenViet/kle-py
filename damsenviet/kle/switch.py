from typeguard import typechecked

from .utils import autorepr, expect

_switches_data = {
    "cherry": {
        "mount": "cherry",
        "name": "Cherry MX Mount",
        "brands": {
            "aula": {
                "brand": "aula",
                "name": "AULA (HiDeep Inc.)",
                "switches": {
                    "Blue": {
                        "part": "Blue",
                        "name": "AULA Blue",
                        "feel": "clicky",
                        "weight": 50,
                    }
                },
            },
            "cherry": {
                "brand": "cherry",
                "name": "Cherry Electrical Products",
                "switches": {
                    "MX1A-A1xx": {
                        "part": "MX1A-A1xx",
                        "name": "MX White",
                        "feel": "clicky",
                        "weight": 70,
                    },
                    "MX1A-11xx": {
                        "part": "MX1A-11xx",
                        "name": "MX Black",
                        "feel": "linear",
                        "weight": 60,
                    },
                    "MX1A-C1xx": {
                        "part": "MX1A-C1xx",
                        "name": "MX Clear",
                        "feel": "tactile",
                        "weight": 55,
                    },
                    "MX1A-D1xx": {
                        "part": "MX1A-D1xx",
                        "name": "MX Tactile Grey",
                        "feel": "tactile",
                        "weight": 80,
                    },
                    "MX1A-E1xx": {
                        "part": "MX1A-E1xx",
                        "name": "MX Blue",
                        "feel": "clicky",
                        "weight": 50,
                    },
                    "MX1A-F1xx": {
                        "part": "MX1A-F1xx",
                        "name": "MX Green",
                        "feel": "clicky",
                        "weight": 70,
                    },
                    "MX1A-G1xx": {
                        "part": "MX1A-G1xx",
                        "name": "MX Brown",
                        "feel": "tactile",
                        "weight": 45,
                    },
                    "MX1A-L1xx": {
                        "part": "MX1A-L1xx",
                        "name": "MX Red",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "MX1A-11Nx": {
                        "part": "MX1A-11Nx",
                        "name": "MX RGB Black",
                        "feel": "linear",
                        "weight": 60,
                    },
                    "MX1A-E1Nx": {
                        "part": "MX1A-E1Nx",
                        "name": "MX RGB Blue",
                        "feel": "clicky",
                        "weight": 50,
                    },
                    "MX1A-G1Nx": {
                        "part": "MX1A-G1Nx",
                        "name": "MX RGB Brown",
                        "feel": "tactile",
                        "weight": 45,
                    },
                    "MX1A-L1Nx": {
                        "part": "MX1A-L1Nx",
                        "name": "MX RGB Red",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "MX1A-21xx": {
                        "part": "MX1A-21xx",
                        "name": "MX Linear Grey",
                        "feel": "linear",
                        "weight": 80,
                    },
                    "MX1A-31xx": {
                        "part": "MX1A-31xx",
                        "name": "MX Lock",
                        "feel": "linear",
                        "weight": 60,
                        "lock": True,
                    },
                    "MX3A-11Nx": {
                        "part": "MX3A-11Nx",
                        "name": "MX Silent RGB Black",
                        "feel": "linear",
                        "weight": 60,
                    },
                    "MX3A-L1Nx": {
                        "part": "MX3A-L1Nx",
                        "name": "MX Silent RGB Red",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "MX3A-L1xx": {
                        "part": "MX3A-L1xx",
                        "name": "MX Silent Red",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "MX3A-11xx": {
                        "part": "MX3A-11xx",
                        "name": "MX Silent Black",
                        "feel": "linear",
                        "weight": 60,
                    },
                },
            },
            "outemu": {
                "brand": "outemu",
                "name": "Outemu (Gaote Electronics)",
                "switches": {
                    "PG150B01-1": {
                        "part": "PG150B01-1",
                        "name": "Clear, Black Shaft",
                        "weight": 65,
                    },
                    "PG150R01-1": {
                        "part": "PG150R01-1",
                        "name": "Clear, Red Shaft",
                        "weight": 50,
                    },
                    "PG150Q01-1": {
                        "part": "PG150Q01-1",
                        "name": "Clear, Blue Shaft",
                        "weight": 55,
                    },
                    "PG150T01-1": {
                        "part": "PG150T01-1",
                        "name": "Clear, Brown Shaft",
                        "weight": 50,
                    },
                    "PG150B01": {
                        "part": "PG150B01",
                        "name": "Black, Black Shaft",
                        "weight": 65,
                    },
                    "PG150R01": {
                        "part": "PG150R01",
                        "name": "Black, Red Shaft",
                        "weight": 50,
                    },
                    "PG150Q01": {
                        "part": "PG150Q01",
                        "name": "Black, Blue Shaft",
                        "weight": 60,
                    },
                    "PG150T01": {
                        "part": "PG150T01",
                        "name": "Black, Brown Shaft",
                        "weight": 55,
                    },
                },
            },
            "gateron": {
                "brand": "gateron",
                "name": "Gateron (Huizhou Jia Electronic Technology Co.)",
                "switches": {
                    "KS-3-Black": {
                        "part": "KS-3-Black",
                        "name": "KS-3 Black Shaft (black)",
                        "feel": "linear",
                        "weight": 50,
                    },
                    "KS-3-Green": {
                        "part": "KS-3-Green",
                        "name": "KS-3 Green Axis (blue)",
                        "feel": "clicky",
                        "weight": 55,
                    },
                    "KS-3-Red": {
                        "part": "KS-3-Red",
                        "name": "KS-3 Red Axis (red)",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "KS-3-Tea": {
                        "part": "KS-3-Tea",
                        "name": "KS-3 Tea Axis (brown)",
                        "feel": "tactile",
                        "weight": 45,
                    },
                    "KS-3-Yellow": {
                        "part": "KS-3-Yellow",
                        "name": "KS-3 Yellow (yellow)",
                        "feel": "linear",
                        "weight": 50,
                    },
                    "KS-3-White": {
                        "part": "KS-3-White",
                        "name": "KS-3 White Shaft (translucent white)",
                        "feel": "linear",
                        "weight": 35,
                    },
                },
            },
            "greetech": {
                "brand": "greetech",
                "name": "Greetech (Huizhou Greetech Electronics Co.)",
                "switches": {
                    "GT02A1Exx": {
                        "part": "GT02A1Exx",
                        "name": "GT02 Red stem",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "GT02A1Dxx": {
                        "part": "GT02A1Dxx",
                        "name": "GT02 Blue stem",
                        "feel": "clicky",
                        "weight": 55,
                    },
                    "GT02A1Bxx": {
                        "part": "GT02A1Bxx",
                        "name": "GTO2 Brown stem",
                        "feel": "tactile",
                        "weight": 50,
                    },
                    "GT02A2Axx": {
                        "part": "GT02A2Axx",
                        "name": "GTO2 Black stem",
                        "feel": "linear",
                        "weight": 65,
                    },
                },
            },
            "hua-jie": {
                "brand": "hua-jie",
                "name": "Hua-Jie (Hua-Jie (Taiwan) Corp)",
                "switches": {
                    "AX01-B": {
                        "part": "AX01-B",
                        "name": "Black stem",
                        "feel": "linear",
                        "weight": 60,
                    },
                    "AX01-R": {
                        "part": "AX01-R",
                        "name": "Red stem",
                        "feel": "linear",
                        "weight": 45,
                    },
                    "AX01-T": {
                        "part": "AX01-T",
                        "name": "Tea/Brown stem",
                        "feel": "tactile",
                        "weight": 55,
                    },
                    "AX01-C": {
                        "part": "AX01-C",
                        "name": "Cyan/Blue stem",
                        "feel": "clicky",
                        "weight": 60,
                    },
                },
            },
            "kailh": {
                "brand": "kailh",
                "name": "Kailh (Kaihua Electronics Co.)",
                "switches": {
                    "PG151101D01/D15": {
                        "part": "PG151101D01/D15",
                        "name": "Kailh Black",
                        "feel": "linear",
                        "weight": 60,
                    },
                    "PG151101D64/D10": {
                        "part": "PG151101D64/D10",
                        "name": "Kailh Blue",
                        "feel": "clicky",
                        "weight": 60,
                    },
                    "PG151101D49/D09": {
                        "part": "PG151101D49/D09",
                        "name": "Kailh Brown",
                        "feel": "tactile",
                        "weight": 55,
                    },
                    "PG151101D05/D43": {
                        "part": "PG151101D05/D43",
                        "name": "Kailh Red",
                        "feel": "linear",
                        "weight": 50,
                    },
                },
            },
            "nimxo": {
                "brand": "nimxo",
                "name": "NIMXO (Ni Mosuo)",
                "switches": {
                    "Gray": {
                        "part": "Gray",
                        "name": "NIMXO Gray",
                        "feel": "clicky",
                        "weight": 60,
                    }
                },
            },
            "razor": {
                "brand": "razor",
                "name": "Razor Inc.",
                "switches": {
                    "Green": {
                        "part": "Green",
                        "name": "Razor Green",
                        "feel": "clicky",
                        "weight": 50,
                    },
                    "Orange": {
                        "part": "Orange",
                        "name": "Razor Orange",
                        "feel": "tactile",
                        "weight": 45,
                    },
                },
            },
        },
    },
    "alps": {
        "mount": "alps",
        "name": "Alps Mount",
        "brands": {
            "alps": {
                "brand": "alps",
                "name": "Alps Electric Co.",
                "switches": {
                    "SKCL/SKCM": {
                        "part": "SKCL/SKCM",
                        "name": "SKCL/SKCM (Complicated Alps)",
                    },
                    "SKBL/SKBM": {
                        "part": "SKBL/SKBM",
                        "name": "SKBL/SKBM (Simplified Alps)",
                    },
                },
            },
            "matias": {
                "brand": "matias",
                "name": "Matias Corporation",
                "switches": {
                    "PG155B02": {
                        "part": "PG155B02",
                        "name": "Click",
                        "feel": "clicky",
                        "weight": 60,
                    },
                    "KS102Q": {
                        "part": "KS102Q",
                        "name": "Quiet Linear",
                        "feel": "linear",
                        "weight": 35,
                    },
                    "PG155B01": {
                        "part": "PG155B01",
                        "name": "Quiet Click",
                        "feel": "tactile",
                        "weight": 60,
                    },
                },
            },
        },
    },
}


class Switch:
    """Class storing incremental Switch."""

    def __init__(
        self,
        mount: str = "",
        brand: str = "",
        type: str = "",
    ) -> None:
        """Instantiates a switch.

        :param mount: the switch mount, defaults to ""
        :type mount: str, optional
        :param brand: the switch brand of a switch mount, defaults to ""
        :type brand: str, optional
        :param type: the switch type part id of a switch brand, defaults to ""
        :type type: str, optional
        """
        self.__mount = ""
        self.__brand = ""
        self.__type = ""
        self.mount = mount
        self.brand = brand
        self.type = type

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
        """Gets switch mount.

        :return: switch mount
        :rtype: str
        """
        return self.__mount

    @mount.setter
    @typechecked
    def mount(self, mount: str) -> None:
        """Sets switch mount.

        :param mount: switch mount
        :type mount: str
        """
        if mount == self.mount:
            return
        if mount != "":
            expect(
                value_name="mount",
                value=mount,
                condition_description="be a valid mount",
                condition=lambda mount: mount in _switches_data,
            )
        self.__mount = mount
        self.brand = ""
        self.type = ""

    @property
    def brand(self) -> str:
        """Gets switch brand.

        :return: switch brand
        :rtype: str
        """
        return self.__brand

    @brand.setter
    @typechecked
    def brand(self, brand: str) -> None:
        """Sets switch brand.

        :param brand: switch brand
        :type brand: str
        """
        if brand == self.brand:
            return
        if brand != "":
            expect(
                value_name="brand",
                value=brand,
                condition_description="be a valid brand in the mount",
                condition=lambda brand: brand in _switches_data[self.mount]["brands"],
            )
        self.__brand = brand
        self.type = ""

    @property
    def type(self) -> str:
        """Gets switch type part id.

        :return: switch type part id
        :rtype: str
        """
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        """Sets switch type part id.

        :param type: switch type
        :type type: str
        """
        if type == self.type:
            return
        if type != "":
            expect(
                value_name="type",
                value=type,
                condition_description="be a valid type in the brand",
                condition=lambda type: type
                in _switches_data[self.mount]["brands"][self.brand]["switches"],
            )
        self.__type = type