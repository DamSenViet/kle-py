# kle-serial-python

This is a [MIT-licensed](LICENSE) javascript library for parsing the serialized format used on [keyboard-layout-editor.com](keyboard-layout-editor.com) (KLE) and converting it into something that is easier to undertsand and use in third-party applications.

Ported over from [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts); rotations fixed.

## Installation

Inside the directory, run the following commands:
```sh
pip3 install -r requirements.txt
pip3 setup -e .
```
It installs the package in editable mode so that changes are updated dynamically.

## Usage

```python
from kle import KLE

keyboard = KLE.parse()
for key in keyboard["keys"]:
  # do your thing here
  pass
```

Refer to [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts) for attribute access.