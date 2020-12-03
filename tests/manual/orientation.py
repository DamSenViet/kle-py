# this file takes command line argument of a path (from anywhere)
# python3 tests.py <path_to.json>
import os
import sys
import math
import json
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import damsenviet.kle as kle

FORMATS = ["Middle Center", "Top Left", "Top Center"]


def rotate(x, y, origin_x, origin_y, degrees):
    rel_x = x - origin_x
    rel_y = y - origin_y
    new_x = (
        origin_x +
        (rel_x * math.cos(math.radians(angle))) -
        (rel_y * math.sin(math.radians(angle)))
    )
    new_y = (
        origin_y +
        (rel_y * math.cos(math.radians(angle))) +
        (rel_x * math.sin(math.radians(angle)))
    )
    return (new_x, new_y)


# check for command line arguments, print path argument
if len(sys.argv) != 2:
    exit(1)
json_path = os.path.join(os.getcwd(), os.path.expanduser(sys.argv[1]))
print(f"Examining KLE: {json_path}")

# select format
chosen_format = None
while(chosen_format not in range(len(FORMATS))):
    try:
        print(
            f"Valid Formats: [0] {FORMATS[0]}, [1] {FORMATS[1]}, [2] {FORMATS[2]}")
        chosen_format = input("Please select a format [0]: ")
        chosen_format = 0 if chosen_format == "" else int(chosen_format)
    except:
        print(f"Invalid Format: \"{chosen_format}.\"")
chosen_format = FORMATS[chosen_format]

# collect and calculate key positions
input_file = open(json_path, "r")
keyboard = kle.Keyboard.from_json(json.load(input_file))
input_file.close()
max_x = - math.inf
min_x = math.inf
max_y = - math.inf
min_y = math.inf
arrows = list()
origins = list()
is_labeled = {
    "rotated": False,
    "nonrotated": False,
    "origin": False
}
for key in keyboard.keys:
    x = float(key.get_x())
    y = float(key.get_y())
    width = float(key.get_width())
    height = float(key.get_height())
    angle = float(key.get_rotation_angle())
    origin_x = float(key.get_rotation_x())
    origin_y = float(key.get_rotation_y())

    adj_x = None  # adjustments
    adj_y = None
    chosen_format
    if chosen_format == "Top Left":
        adj_x = 0
        adj_y = 0
    elif chosen_format == "Top Center":
        adj_x = width/2
        adj_y = 0
    elif chosen_format == "Middle Center":
        adj_x = width/2.0
        adj_y = height/2.0

    if angle != 0:
        origins.append({
            "x": origin_x,
            "y": origin_y,
            "color": "g",
            "label": "origin points" if not is_labeled["origin"] else None,
        })
        is_labeled["origin"] = True

        new_x, new_y = rotate(x + adj_x, y + adj_y, origin_x, origin_y, angle)
        # 0.5 to get base coordinates for arrows
        low_x, low_y = rotate(x + adj_x, y + adj_y + 0.5,
                              origin_x, origin_y, angle)
        dir_x, dir_y = (low_x - new_x, low_y - new_y)  # vector normalized

        max_x = max(max_x, low_x, new_x)
        min_x = min(min_x, low_x, new_x)
        max_y = max(max_y, low_y, new_y)
        min_y = min(min_y, low_y, new_y)

        arrows.append({
            "low_x": low_x,
            "low_y": low_y,
            "vect_x": -dir_x,
            "vect_y": -dir_y,
            "color": "r",
            "label": "rotated" if not is_labeled["rotated"] else None
        })
        is_labeled["rotated"] = True
    else:
        max_x = max(max_x, x + width)
        min_x = min(min_x, x)
        max_y = max(max_y, y + height)
        min_y = min(min_y, y)

        # 0.5 to get base coordinates for arrows
        arrows.append({
            "low_x": x + adj_x,
            "low_y": y + adj_y + 0.5,
            "vect_x": 0,
            "vect_y": -0.5,
            "color": "b",
            "label": "non-rotated" if not is_labeled["nonrotated"] else None
        })
        is_labeled["nonrotated"] = True

# initiate figure to aspect ratio
aspect_ratio = (max_x - min_x)/(max_y - min_y)
figsize = ((max_y - min_y) * aspect_ratio/2, (max_y - min_y)/1)
plt.figure(figsize=figsize)

for origin in origins:
    plt.scatter(
        origin["x"],
        origin["y"],
        color=origin["color"],
        marker=".",
        label=origin["label"]
    )

for arrow in arrows:
    plt.arrow(
        arrow["low_x"],
        arrow["low_y"],
        arrow["vect_x"],
        arrow["vect_y"],
        color=arrow["color"],
        head_width=0.1,
        head_length=0.1,
        length_includes_head=True,
        label=arrow["label"]
    )

# make lines for legends
custom_lines = [
    lines.Line2D(
        [0],
        [0],
        color="w",
        marker="o",
        markerfacecolor="g",
        label="origin points"
    ),
    lines.Line2D([0], [0], color="b", lw=1, label="non-rotated"),
    lines.Line2D([0], [0], color="r", lw=1, label="rotated")
]
# label the lines for the legends
plt.legend(
    custom_lines,
    [
        "origin points",
        "non-rotated",
        "rotated",
    ],
    fontsize=9,
    loc="lower right"
)

# configure x and y axis for proper viewing
plt.xlim(min_x - 1, max_x + 1)
plt.ylim(max_y + 2, min_y - 1)  # turn y axis upside down
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.title(f"Keys (Aligned {chosen_format})", loc="center")
plt.show()

# verify manually that orientations are correct
