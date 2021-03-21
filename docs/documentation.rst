Documentation
=============

This library provides comprehensive apis to serialize/deserialize and access
KLE data. While being a port of KLE's official code, it provides improvements
to prevent needing to evaluate redirected values. With this library, no
re-evaluation on redirected values need to be performed, as the redirected values
have been unpacked into the data structures.

Precision
---------

This library attempts to replicate the calculation precision in the existing
KLE JavaScript library, choosing to be no more and no less precise. Because KLE
doesn't use arbitrary precision and uses JavaScript's floating point numbers,
we chose to match the IEEE-754 standard for floating-point arithmetic.This was
necessary to maintain identical import/export results with KLE's web application.

Deterministic
-------------

The primary property this library maintains is that any KLE JSON serialized and
deserialized by this library can be serialized back into an equivalent json.

.. code-block:: python
    
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
    
    keyboard_json = json.load(json_absolute_file_path)
    keyboard = Keyboard.from_json(keyboard_json)
    assert(keyboard_json == keyboard.to_json()) # true


The KLE Format
--------------

KLE's JSON format was designed to help minimize it's file size. The JSON
mainly records the running changes as opposed to individual key property
objects. This also means that precision errors and invalid/missing values can
invalidate every subsequent key stored.

The format is composed as a JSON array with an optional metadata JSON object as
the first item. Every item after the first metadata object in the JSON must
be an array. These arrays contain objects that record key property changes
or strings that represent labels. Some of these key properties changes and labels
have been reordered to minimize file size and therefore need to be unaligned
before being put into data structures and re-aligned when exporting.

Not all objects in the arrays represent key property changes however, some are
boolean properties that only apply to the following key after it (e.g. 'd'
property for decal keys is an example of this).

An example of the KLE JSON format:

.. code-block:: json
    
    [
      {
        "backcolor": "#ac6363",
        "name": "Numpad",
        "author": "Example",
        "background": {
          "name": "Carbon fibre 2",
          "style": "background-image: url('/bg/carbonfibre/carbon_texture1874.png');"
        },
        "radii": "6px 6px 6px 6px / 6px 6px 6px 6px",
        "switchMount": "cherry",
        "switchBrand": "cherry",
        "switchType": "MX1A-11Nx",
        "pcb": true,
        "plate": false
      },
      [
        "Num Lock",
        "/",
        "*",
        "-"
      ],
      [
        "7\nHome",
        {
          "g": true
        },
        "8\n↑",
        {
          "g": false
        },
        "9\nPgUp",
        {
          "h": 2
        },
        "+"
      ],
      [
        "4\n←",
        {
          "d": true
        },
        "5",
        "6\n→"
      ],
      [
        "1\nEnd",
        "2\n↓",
        "3\nPgDn",
        {
          "sm": "wow",
          "sb": "oops",
          "st": "PG155B01",
          "h": 2
        },
        "Enter"
      ],
      [
        {
          "w": 2
        },
        "0\nIns",
        ".\nDel"
      ]
    ]