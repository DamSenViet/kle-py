import os
import glob
import json
import pytest
import damsenviet.kle as kle


inputs_dir = os.path.join(
    os.path.dirname(__file__),
    "..",
    "inputs"
)
outputs_dir = os.path.join(
    os.path.dirname(__file__),
    "..",
    "outputs"
)
os.makedirs(outputs_dir, exist_ok=True)
keyboard_jsons = list()
file_names = list()
for file_name in os.listdir(inputs_dir):
    if not file_name.endswith(".json"):
        continue
    file_names.append(file_name)


@pytest.mark.parametrize("file_name", file_names)
def test_inputs(file_name):
    # read input
    input_file_path = os.path.join(inputs_dir, file_name)
    input_file = open(input_file_path, "r")
    keyboard_json = json.load(input_file)
    keyboard = kle.Keyboard.from_json(keyboard_json)
    input_file.close()
    # write output
    output_file_path = os.path.join(outputs_dir, file_name)
    output_file = open(output_file_path, "w")
    json.dump(
        keyboard.to_json(),
        output_file,
        sort_keys=False,
        indent=2,
        ensure_ascii=False
    )
    output_file.close()
    assert json.dumps(
        keyboard_json, sort_keys=True, indent=2, ensure_ascii=True
    ) == json.dumps(
        keyboard.to_json(), sort_keys=True, indent=2, ensure_ascii=True
    )
