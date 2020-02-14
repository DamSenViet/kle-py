# kle-serial-python

This is a [MIT-licensed](LICENSE) javascript library for parsing the serialized
format used on [keyboard-layout-editor.com](keyboard-layout-editor.com) (KLE)
and converting it into something that is easier to undertsand and use in
third-party applications.

Ported over from [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts)
with working rotations.

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

## Example

```python
from kle import KLE

keyboard = KLE.load(open(file_path))
for key in keyboard.keys:
  # do your thing here
```

Refer to [kle-serial/index.ts](https://github.com/ijprest/kle-serial/blob/master/index.ts)
for attribute access. Note that variable and attribute names use python naming
conventions instead of javascript naming conventions. Docstrings are available
for all classes and methods in the module.

## Extending Classes

The classes have been designed such that anybody can customize the parsing of
the KLE file by simply extending the KLE and Key classes. Here's an example:

```python
from kle import Key, KLE

class CustomKey(Key):
  # your implementation here

class CustomKLE(KLE):
    key_class = CustomKey # set this to use your custom key

    @classmethod
    def deserialize_adjustment(
        cls, # class, like self but for @classmethod
        key: Key,
        align: int,
        current_rotation: float,
        current_rotation_x: float,
        current_rotation_y: float,
        item: dict
    ) -> (
        Key,
        int,
        float,
        float,
        float,
    ):
        (
            key,
            align,
            current_rotation,
            current_rotation_x,
            current_rotation_y
        ) = super().deserialize_adjustment(
            cls,
            key,
            align,
            current_rotation,
            current_rotation_x,
            current_rotation_y,
            item
        )
        # your additional implementation or fields here
        # return critical arguments so they get updated in the parsing loop
        return (
            key,
            align,
            current_rotation,
            current_rotation_x,
            current_rotation_y
        )
```

## Contributing and Testing

Inside the kle directory, run the following commands to prepare your
dependencies for testing:

```sh
pip3 install -r tests/requirements.txt
pip3 install -U -e . # update existing kle, install as editable module
```

To view and verify coordinates and orientation, run test.py with a file as an
argument:

```sh
python3 tests/orientation.py <path_to.json>
```