# kle-py

A Python library for interacting with KLE data structures and files.

Originally ported from [keyboard-layout-editor/serial.js](https://github.com/ijprest/keyboard-layout-editor/)
with improvements to make the source code increasingly portable across
different language platforms.

## Table of Contents

* [Documentation](#documentation)
* [Installation](#installation)
* [Quick Start](#quick-start)

## Documentation

To view documentation, examples, visit the [documentation site](https://damsenviet.github.io/kle-py/).

## Installation

To install and use the library, use the installation method listed below.

``` bash
pip3 install damsenviet.kle
```

## Quick Start

This quick start demo demonstrates parsing a KLE formatted json file.

``` py
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
