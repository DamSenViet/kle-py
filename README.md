# kle-cereal-python

This is a [MIT-licensed](LICENSE) third-party python library for parsing the
serialized format used on [keyboard-layout-editor.com](keyboard-layout-editor.com)
(KLE) and converting it into something that is easier to undertsand and use in
third-party applications. 'Cereal' is intentionally spelled incorrectly to
indicate that this repository is not developed or maintained by the same
maintainers of the [official keboard-layout-editor repository](https://github.com/ijprest/keyboard-layout-editor).

Ported over from [keyboard-layout-editor/serial.js](https://github.com/ijprest/keyboard-layout-editor/blob/master/serial.js)
with working rotations.

## Installation

Run the following commands to install the package or update it with pip3:
```sh
pip3 install -U git+https://github.com/DamSenViet/kle-cereal-python.git
```

## Uninstallation

Run the following commands to uninstall the package with pip3:
```sh
pip3 uninstall kle-cereal
```

## Example

```python
import kle.cereal as cereal

keyboard = cereal.load(open(file_path))
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
import decimal as dec
import kle.cereal as cereal

class CustomKey(cereal.Key):
  # your implementation here

# Don't need CustomKeyboard b/c kle.Keyboard is already generic

class CustomCereal(cereal.Cereal):
    key_class = CustomKey # set this to use your custom key

    @classmethod
    def deserialize_adjustment(
        cls, # class, like self but for @classmethod
        key: kle.Key,
        align: int,
        cluster_rotation: dec.Decimal,
        cluster_rotation_x: dec.Decimal,
        cluster_rotation_y: dec.Decimal,
        item: dict
    ) -> (
        kle.Key,
        int,
        dec.Decimal,
        dec.Decimal,
        dec.Decimal
    ):
        (
            key,
            align,
            cluster_rotation,
            cluster_rotation_x,
            cluster_rotation_y
        ) = super().deserialize_adjustment(
            cls,
            key,
            align,
            cluster_rotation,
            cluster_rotation_x,
            cluster_rotation_y,
            item
        )
        # your additional implementation or fields here
        # return critical arguments so they get updated in the parsing loop
        return (
            key,
            align,
            cluster_rotation,
            cluster_rotation_x,
            cluster_rotation_y
        )

CustomKle.load(open("file-path"))
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