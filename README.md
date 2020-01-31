# kle-serial-python

This is a [MIT-licensed](LICENSE) javascript library for parsing the serialized format used on [keyboard-layout-editor.com](keyboard-layout-editor.com) (KLE) and converting it into something that is easier to undertsand and use in third-party applications.

Ported over from [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts) with working rotations.

## Installation

Run the following commands to install the package or update it with pip3:
```sh
pip3 install -U git+https://github.com/DamSenViet/kle-serial-python.git
```

## Uninstallation

Run the following commands to uninstall the package with pip3:
```sh
pip3 uninstall kle
```

## Usage

```python
from kle import KLE

keyboard = KLE.parse(open(file_path))
for key in keyboard.keys:
  # do your thing here
  pass
```

Refer to [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts) for attribute access.

## Contributing and Testing

Inside the kle directory, run the following commands:
```sh
pip3 install -r tests/requirements.txt
pip3 install -U -e .
```

To verify coordinates and orientation, run test.py with a file as an argument:
```sh
python3 tests/test.py <path_to.json>
```