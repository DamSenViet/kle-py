Documentation
=============

This library provides comprehensive apis to serialize/deserialize and access
KLE data. While being a port of KLE's official code, it provides improvements
to prevent needing to evaluate redirected values. With this library, no
evaluation on redirected values needs to be performed, as the redirected values
have been unpacked into the data structures.

Precision
---------

This library uses arbitrary math precision libraries, but uses specific
precision when serializing and deserializing. To maintain precision on
mathematical operations, utilize the decimal's Decimal constructor with
strings.

.. code-block:: python

    from decimal import Decimal
    from damsenviet.kle import Key
    
    # str native float values to prevent inprecision from affecting Decimal
    key = Key()
    key.x += Decimal(str(1.2))


Invariants
----------

Any invariants that cannot be maintained by KLE will not be enforced in this
library for the sake of consistency (e.g. colors can be invalid string
representations). Generic types however are enforced on the properties.

.. code-block:: python

    from decimal import Decimal
    from damsenviet import Key
    
    key = Key()
    
    # throws error
    key.x = "wow"
    key.width = "oops"
    # perfectly fine
    key.x = Decimal(str(1))
    key.width = -Decimal(str(2)) # kle doesn't correct negative numbers
    
    # throws error, only takes numbers
    key.color = 0
    # success
    key.color = "#000000"
    key.color = "asdjfljasdlfjl;aksdjflk"


Deterministic
-------------

The primary property this library maintains is that any KLE file deserialized
in this library can be serialized back into an equivalent json.

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
    assert(kle_json == keyboard.to_json()) # true


The KLE Format
--------------

KLE's JSON serial format was designed to help minimize it's file size and not
ease of use. The JSON serial records the running changes as opposed to
individual key dictionaries.

Specific values like empty strings or 0's are flags to developers to check the
default value which is used to help optimize the final changes, but put
an additional burden on developers who try to access the data.

The format is composed of a optional metadata JSON object as a first item.
Every item after the first metadata object in the JSON must be an array.These
arrays can contain objects that record key property changes or strings that
represent labels. Some of these key properties changes and labels have been
reordered to minimize file size and therefore need to be unaligned before
being put into data structures.

Not all objects in the arrays represent key property changes however, some are
boolean properties that only apply to the following key after it (e.g. 'g'
property for ghosted keys is an example of this).


.. code-block:: python

    import os
    import json

    # relative to this file
    json_relative_file_path = "./keyboard.json"
    json_absolute_file_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            json_relative_file_path,
        )
    )
