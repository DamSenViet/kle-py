# checks deserialization
# python3 tests.py <path_to_input.json> <path_to_output.json>

import os
import sys
import kle.cereal as cereal

def resolve(p):
  return os.path.join(os.getcwd(), os.path.expanduser(p))

if len(sys.argv) < 2 or len(sys.argv) > 3: exit(1)

input_path = resolve(sys.argv[1])
print(f"Examining KLE: {input_path}")

input_file = open(input_path)
keyboard = cereal.load(input_file)
input_file.close()

if (len(sys.argv) >= 3):
  output_path = resolve(sys.argv[2])
  output_file = open(f"{output_path}", "w")
  cereal.dump(keyboard, output_file)
  output_file.close()
else:
  kle_str = cereal.dumps(keyboard)
  print(kle_str)