from __future__ import annotations
from typeguard import typechecked
from .utils import (
    autorepr,
    expected,
    is_valid_css_declaration,
)

__all__ = ["Background"]

background_image_root = "http://www.keyboard-layout-editor.com/"
# fmt: off
backgrounds_json = [
  { 
    "category": "Carbon fibre", "style" : "background: url('/bg/carbonfibre/carbon-slice.jpg'); color: #fff;",
    "content" : [
      { "name": "Carbon fibre 1", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1879.png');" },
      { "name": "Carbon fibre 2", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1874.png');" },
      { "name": "Carbon fibre 3", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1869.png');" },
      { "name": "Carbon fibre 4", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1873.png');" },
      { "name": "Carbon fibre 5", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1876.jpg');" },
      { "name": "Carbon fibre 6", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1882.jpg');" },
      { "name": "Carbon fibre 7", "style" : "background-image: url('/bg/carbonfibre/carbon_texture1877.jpg');" }
    ]
  },
  { 
    "category": "Leather", "style" : "background: url('/bg/leather/leather-slice.jpg'); color: #fff;",
    "content" : [
      { "name": "Black", "style" : "background-image: url('/bg/leather/black.jpg');" },
      { "name": "Black storm", "style" : "background-image: url('/bg/leather/leather_texture1051.jpg');" },
      { "name": "Camel", "style" : "background-image: url('/bg/leather/leather_texture4327.jpg');" },
      { "name": "Brown", "style" : "background-image: url('/bg/leather/brown.jpg');" },
      { "name": "Brown oxblood", "style" : "background-image: url('/bg/leather/leather_texture4337.jpg');" },
      { "name": "Brown shiny", "style" : "background-image: url('/bg/leather/leather_texture404.jpg');" },
      { "name": "Brown suede", "style" : "background-image: url('/bg/leather/leather_texture4315.jpg');" },
      { "name": "Navy", "style" : "background-image: url('/bg/leather/leather_texture4326.jpg');" },
      { "name": "Orange", "style" : "background-image: url('/bg/leather/leather_texture4329.jpg');" },
      { "name": "Red fire", "style" : "background-image: url('/bg/leather/leather_texture394.jpg');" },
      { "name": "White", "style" : "background-image: url('/bg/leather/leather_texture4378.jpg');" }
    ]
  },
  { 
    "category": "Marble", "style" : "background: url('/bg/marble/marble-slice.jpg'); color: #fff;",
    "content" : [
      { "name": "Marble beige", "style" : "background-image: url('/bg/marble/marble_texture4653.jpg');" },
      { "name": "Marble black", "style" : "background-image: url('/bg/marble/marble_texture4510.jpg');" },
      { "name": "Marble brown", "style" : "background-image: url('/bg/marble/marble_texture4512.jpg');" },
      { "name": "Marble green", "style" : "background-image: url('/bg/marble/marble_texture1809.jpg');" },
      { "name": "Marble grey", "style" : "background-image: url('/bg/marble/marble_texture4515.jpg');" },
      { "name": "Marble navy", "style" : "background-image: url('/bg/marble/marble_texture4511.jpg');" },
      { "name": "Marble rose", "style" : "background-image: url('/bg/marble/marble_texture1820.jpg');" },
      { "name": "Marble Prussian blue", "style" : "background-image: url('/bg/marble/marble_texture4509.jpg');" },
      { "name": "Marble red deep", "style" : "background-image: url('/bg/marble/marble_texture4496.jpg');" },
      { "name": "Marble violet", "style" : "background-image: url('/bg/marble/marble_texture4617.jpg');" }
    ]
  },
  { 
    "category": "Metal", "style" : "background: url('/bg/metal/metal-slice.jpg'); color: #fff;",
    "content" : [
      { "name": "Aluminium brushed", "style" : "background-image: url('/bg/metal/aluminum_texture1642.jpg');" },
      { "name": "Aluminium brushed black", "style" : "background-image: url('/bg/metal/aluminum_texture1644.jpg');" },
      { "name": "Aluminium diagonal light", "style" : "background-image: url('/bg/metal/aluminum_texture1645.jpg');" },
      { "name": "Aluminium brassed", "style" : "background-image: url('/bg/metal/aluminum_texture1649.jpg');" },
      { "name": "Aluminium pattern", "style" : "background-image: url('/bg/metal/aluminum_texture1735.jpg');" },
      { "name": "Aluminium brushed wavy", "style" : "background-image: url('/bg/metal/aluminum_texture1738.jpg');" },
      { "name": "Aluminium diagonal dark", "style" : "background-image: url('/bg/metal/aluminum_texture1784.jpg');" },
      { "name": "Steel brushed light", "style" : "background-image: url('/bg/metal/iron_texture1744.jpg');" },
      { "name": "Steel brushed dark", "style" : "background-image: url('/bg/metal/iron_texture1745.jpg');" },
      { "name": "Steel brushed wavy", "style" : "background-image: url('/bg/metal/iron_texture61.jpg');" },
      { "name": "Steel brushed horizontal", "style" : "background-image: url('/bg/metal/iron_texture66.jpg');" },
      { "name": "Titanium wavy", "style" : "background-image: url('/bg/metal/titanium_texture1752.jpg');" }
    ]
  },
  { 
    "category": "Plastic ABS (whites)", "style" : "background: url('/bg/plastic/plastic-slice.jpg'); color: #000;",
    "content" : [
      { "name": "ABS WA", "style" : "background-image: url('/bg/plastic/abs-wa.jpg');" },
      { "name": "ABS WAR", "style" : "background-image: url('/bg/plastic/abs-war.jpg');" },
      { "name": "ABS WBO", "style" : "background-image: url('/bg/plastic/abs-wbo.jpg');" },
      { "name": "ABS WCK", "style" : "background-image: url('/bg/plastic/abs-wck.jpg');" },
      { "name": "ABS WEA", "style" : "background-image: url('/bg/plastic/abs-wea.jpg');" },
      { "name": "ABS WFK", "style" : "background-image: url('/bg/plastic/abs-wfk.jpg');" },
      { "name": "ABS WFM", "style" : "background-image: url('/bg/plastic/abs-wfm.jpg');" },
      { "name": "ABS WFO", "style" : "background-image: url('/bg/plastic/abs-wfo.jpg');" },
      { "name": "ABS WQ", "style" : "background-image: url('/bg/plastic/abs-wq.jpg');" },
      { "name": "ABS WV", "style" : "background-image: url('/bg/plastic/abs-wv.jpg');" },
      { "name": "ABS WW", "style" : "background-image: url('/bg/plastic/abs-ww.jpg');" }
    ]
  },
  { 
    "category": "Plastic PBT (browns & blacks)", "style" : "background: url('/bg/plastic/plastic-slice.jpg'); color: #000;",
    "content" : [
      { "name": "PBT Black", "style" : "background-image: url('/bg/plastic/pbt-black.png');" },
      { "name": "PBT UP", "style" : "background-image: url('/bg/plastic/pbt-up.png');" },
      { "name": "PBT TGJ", "style" : "background-image: url('/bg/plastic/pbt-tgj.png');" },
      { "name": "PBT TT", "style" : "background-image: url('/bg/plastic/pbt-tt.png');" }
    ]
  },
  { 
    "category": "Plastic PBT (whites)", "style" : "background: url('/bg/plastic/plastic-slice.jpg'); color: #000;",
    "content" : [
      { "name": "PBT WAN", "style" : "background-image: url('/bg/plastic/pbt-wan.png');" },
      { "name": "PBT WAS", "style" : "background-image: url('/bg/plastic/pbt-was.png');" },
      { "name": "PBT WAT", "style" : "background-image: url('/bg/plastic/pbt-wat.png');" },
      { "name": "PBT WBK", "style" : "background-image: url('/bg/plastic/pbt-wbk.png');" },
      { "name": "PBT WBR", "style" : "background-image: url('/bg/plastic/pbt-wbr.png');" },
      { "name": "PBT WCS", "style" : "background-image: url('/bg/plastic/pbt-wcs.png');" },
      { "name": "PBT WCV", "style" : "background-image: url('/bg/plastic/pbt-wcv.png');" },
      { "name": "PBT WCX", "style" : "background-image: url('/bg/plastic/pbt-wcx.png');" },
      { "name": "PBT WDG", "style" : "background-image: url('/bg/plastic/pbt-wdg.png');" },
      { "name": "PBT WFJ", "style" : "background-image: url('/bg/plastic/pbt-wfj.png');" },
      { "name": "PBT WFN", "style" : "background-image: url('/bg/plastic/pbt-wfn.png');" }
    ]
  },
  { 
    "category": "Wood", "style": "background-image: url('/bg/wood/wood-slice.jpg'); color: #000;",
    "content" : [
      { "name": "Bamboo", "style" : "background-image: url('/bg/wood/bamboo.jpg');" },
      { "name": "Bamboo dark", "style" : "background-image: url('/bg/wood/bamboo-dark.jpg');" },
      { "name": "Birch", "style" : "background-image: url('/bg/wood/birch.jpg');" },
      { "name": "Birch European white", "style" : "background-image: url('/bg/wood/birch-european-white.jpg');" },
      { "name": "Birch yellow", "style" : "background-image: url('/bg/wood/birch-yellow.jpg');" },
      { "name": "Cherry", "style" : "background-image: url('/bg/wood/cherry.jpg');" },
      { "name": "Chestnut American", "style" : "background-image: url('/bg/wood/chestnut-american.jpg');" },
      { "name": "Ebony Macassar", "style" : "background-image: url('/bg/wood/ebony-macassar.jpg');" },
      { "name": "Fir white", "style" : "background-image: url('/bg/wood/fir-white.jpg');" },
      { "name": "Maple orange", "style" : "background-image: url('/bg/wood/maple-orange.jpg');" },
      { "name": "Maple yellow", "style" : "background-image: url('/bg/wood/maple-yellow.jpg');" },
      { "name": "Mahogany African", "style" : "background-image: url('/bg/wood/mahogany-african.jpg');" },
      { "name": "Mahogany Red", "style" : "background-image: url('/bg/wood/Red_Mahogany_Wood.jpg');" },
      { "name": "Moringa", "style" : "background-image: url('/bg/wood/moringa.jpg');" },
      { "name": "Oak", "style" : "background-image: url('/bg/wood/oak.jpg');" },
      { "name": "Pine Oregon", "style" : "background-image: url('/bg/wood/pine-oregon.jpg');" },
      { "name": "Sandalwood African", "style" : "background-image: url('/bg/wood/sandalwood-african.jpg');" },
      { "name": "Teak African", "style" : "background-image: url('/bg/wood/teak-african.jpg');" },
      { "name": "Teak golden", "style" : "background-image: url('/bg/wood/teak-golden.jpg');" },
      { "name": "Walnut", "style" : "background-image: url('/bg/wood/walnut.jpg');" }
    ]
  }
]
# fmt: on

name_to_style = dict()
for category in backgrounds_json:
    for option in category["content"]:
        name_to_style[option["name"]] = option["style"]


class Background:
    """Class storing Metadata's Background."""

    def __init__(self, name: str = "", style: str = ""):
        self.__name = ""
        self.__style = ""
        self.name = name

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return autorepr(
            self,
            {
                "name": self.name,
                "style": self.style,
            },
        )

    @property
    def name(self) -> str:
        """Name of the background option.

        :getter: gets the name of the background option
        :setter: sets the name of the background option and the style
        :type: str
        """
        return self.__name

    @name.setter
    @typechecked
    def name(self, name: str) -> None:
        """Sets name.

        :param name: name
        :type name: str
        """
        expected(
            "name",
            name,
            "be a valid background option name",
            lambda name: name in name_to_style,
        )
        self.__name = name
        self.__style = name_to_style[name]

    @property
    def style(self) -> str:
        """CSS style declaration of background option.

        :getter: CSS style declaration of background option
        :type: str
        """
        return self.__style
