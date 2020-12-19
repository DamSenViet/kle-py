import os
import json
import pytest
from damsenviet.kle import Keyboard


inputs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "inputs"))
outputs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs"))
os.makedirs(outputs_dir, exist_ok=True)
keyboard_jsons = list()
file_names = list()
for file_name in os.listdir(inputs_dir):
    if not file_name.endswith(".json"):
        continue
    file_names.append(file_name)


@pytest.mark.parametrize("file_name", file_names)
def test_inputs(file_name: str):
    # read input
    input_file_path = os.path.join(inputs_dir, file_name)
    input_file = open(input_file_path, "r")
    keyboard_json = json.load(input_file)
    keyboard = Keyboard.from_json(keyboard_json)
    input_file.close()
    # write output and formatted input file for debugging
    output_file_path = os.path.join(outputs_dir, file_name)
    tokens = file_name.split(".")
    formatted_input_path = os.path.join(
        outputs_dir,
        tokens[0] + "-formatted." + ".".join(tokens[1:]),
    )
    formatted_input_file = open(formatted_input_path, "w")
    output_file = open(output_file_path, "w")
    json.dump(
        keyboard.to_json(),
        output_file,
        sort_keys=False,
        indent=2,
        ensure_ascii=False,
    )
    json.dump(
        keyboard_json,
        formatted_input_file,
        sort_keys=False,
        indent=2,
        ensure_ascii=False,
    )
    formatted_input_file.close()
    output_file.close()
    # compare text versions
    assert json.dumps(
        keyboard_json,
        sort_keys=True,
        indent=2,
        ensure_ascii=True,
    ) == json.dumps(
        keyboard.to_json(),
        sort_keys=True,
        indent=2,
        ensure_ascii=True,
    )
