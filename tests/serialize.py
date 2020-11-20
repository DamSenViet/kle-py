# checks deserialization
# python3 tests.py <path_to_input.json> <path_to_output.json>

import os
import sys
import json
from damsenviet.kle import Keyboard


def resolve(p):
    return os.path.join(os.getcwd(), os.path.expanduser(p))


if len(sys.argv) < 2 or len(sys.argv) > 3:
    exit(1)

input_path = resolve(sys.argv[1])
print(f"Examining KLE: {input_path}")

input_file = open(input_path)
keyboard = Keyboard.from_json(json.load(input_file))
input_file.close()

if (len(sys.argv) >= 3):
    output_path = resolve(sys.argv[2])
    output_file = open(f"{output_path}", "w")
    json.dump(
        keyboard.to_json(),
        output_file,
        sort_keys=False,
        indent=2,
        ensure_ascii=False
    )
    output_file.close()
else:
    kle_str = json.dumps(keyboard.to_json())
    print(kle_str)
