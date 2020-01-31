# file takes command line argument of a path
# python3 tests.py <path_to.json>

import matplotlib.pyplot as plt
from sys import argv
from os import path, getcwd
from kle import KLE
from math import radians, sin, cos, inf

if len(argv) != 2: exit(1)
json_path = path.join(getcwd(), path.expanduser(argv[1]))

FORMATS = ["Middle Center", "Top Left", "Top Center"]

def rotate(x, y, origin_x, origin_y, degrees):
  rel_x = x - origin_x
  rel_y = y - origin_y
  new_x = origin_x + (rel_x * cos(radians(angle))) - (rel_y * sin(radians(angle)))
  new_y = origin_y + (rel_y * cos(radians(angle))) + (rel_x * sin(radians(angle)))
  return (new_x, new_y)

# select format
chosen_format = None
while(chosen_format not in range(len(FORMATS))):
  try:
    print(f"Valid Formats: [0] {FORMATS[0]}, [1] {FORMATS[1]}, [2] {FORMATS[2]}")
    chosen_format = input("Please select a format [0]: ")
    chosen_format = 0 if chosen_format == "" else int(chosen_format)
  except:
    print(f"Invalid Format: \"{chosen_format}.\"")
chosen_format = FORMATS[chosen_format]

# print test
fig = plt.figure()
ax = plt.gca()
keyboard = KLE.parse(open(json_path))
max_x = 0.0
min_x = inf
max_y = 0.0
min_y = inf
is_labeled = {
  "rotated": False,
  "nonrotated": False,
  "origin": False
}
for key in keyboard.keys:
  x = key.x
  y = key.y
  width = key.width
  height = key.height
  angle = key.rotation_angle
  origin_x = key.rotation_x
  origin_y = key.rotation_y

  adj_x = None # adjustments
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
    plt.scatter(
      origin_x,
      origin_y,
      color = "g",
      marker = ".",
      label = "origin points" if not is_labeled["origin"] else None
    )
    is_labeled["origin"] = True

    new_x, new_y = rotate(x + adj_x, y + adj_y, origin_x, origin_y, angle)
    # 0.5 to get base coordinates for arrows
    low_x, low_y = rotate(x + adj_x, y + adj_y + 0.5, origin_x, origin_y, angle)
    dir_x, dir_y = (low_x - new_x, low_y - new_y)

    max_x = max(max_x, new_x)
    min_x = min(min_x, new_x)
    max_y = max(max_y, new_y)
    min_y = min(min_y, new_y)

    plt.arrow(
      low_x,
      low_y,
      -dir_x,
      -dir_y,
      color='r',
      head_width = 0.1,
      head_length = 0.1,
      length_includes_head = True,
      label = "rotated" if not is_labeled["rotated"] else None
    )
    is_labeled["rotated"] = True
  else:
    max_x = max(max_x, x)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    min_y = min(min_y, y)

    # 0.5 to get base coordinates for arrows
    plt.arrow(
      x + adj_x,
      y + adj_y + 0.5,
      0,
      -0.5,
      color = 'b',
      head_width = 0.1,
      head_length = 0.1,
      length_includes_head = True,
      label = "non-rotated" if not is_labeled["nonrotated"] else None
    )
    is_labeled["nonrotated"] = True

plt.xlim(min_x - 1, max_x + 2)
plt.ylim(max_y + 3, min_y - 1)
plt.legend(fontsize = 12, loc = "lower right")
plt.title(f"Keys (aligned {chosen_format})", loc = "center")
plt.show()