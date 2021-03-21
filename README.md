# kle-py

A Python library for interacting with KLE data structures and KLE JSON files.

Originally ported from [keyboard-layout-editor](https://github.com/ijprest/keyboard-layout-editor/)
with improvements to make the source code increasingly portable across
different language platforms.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Contributing](#contributing)

## Documentation

To view documentation, examples, visit the [documentation site](https://damsenviet.github.io/kle-py/).

## Installation

To install and use the library, use the installation method listed below.

```sh
pip3 install damsenviet.kle
```

## Quick Start

This quick start demo demonstrates parsing a KLE JSON file.

```python
import os
import json
from damsenviet.kle import Keyboard

# relative to this file
json_relative_file_path = "./keyboard.json"
json_absolute_file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        json_relative_file_path,
    )
)

keyboard = Keyboard.from_json(
    json.load(json_absolute_file_path)
)

for key in keyboard.keys:
    for label in key.labels:
        pass
```

## Contributing

There are many ways to contribute to this project.

- [Creating Issues](./CONTRIBUTING.md#creating-issues)
- [Contributing Code](./CONTRIBUTING.md#contributing-code)
- [Sponsoring Developers](./CONTRIBUTING.md#sponsoring-developers)

For more information please see the [contributing guidelines](./CONTRIBUTING.md).
