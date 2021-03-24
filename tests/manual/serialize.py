# utility script to manually check for deserialization results
# python3 serialize.py <path_to_input.json> <path_to_output.json>

import os
import sys
import json
import damsenviet.kle as kle


def resolve(p):
    return os.path.join(os.getcwd(), os.path.expanduser(p))


if len(sys.argv) < 2 or len(sys.argv) > 3:
    exit(1)

input_path = resolve(sys.argv[1])
print(f"Reading KLE JSON: {input_path}")

input_file = open(input_path)
keyboard = kle.Keyboard.from_json(json.load(input_file))
input_file.close()

output = None
if len(sys.argv) >= 3:
    output_path = resolve(sys.argv[2])
    output_file = open(f"{output_path}", "w")
    print(f"Writing KLE JSON: {output_path}")
    json.dump(
        keyboard.to_json(),
        output_file,
        sort_keys=False,
        indent=2,
        ensure_ascii=False,
    )
    output_file.close()
else:
    output = json.dumps(
        keyboard.to_json(),
        sort_keys=False,
        indent=2,
        ensure_ascii=False,
    )
    print(output)
