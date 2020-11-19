import json
from typing import (
    Union,
    List,
    Dict,
)


class DeserializeException(Exception):
    """Class for all exceptions encountered during deserialization."""

    def __init__(self, message: str = None,
                 payload: Union[Dict, List] = None):
        """Construct a `DeserializeException`.

        :param message: A message indicating a processing error during
            deserialization of the KLE file.
        :type message: str
        :param payload: The offending payload during deserialization, defaults
            to `None`.
        :type payload: Union[dict, list, None], optional
        """
        super().__init__(
            message + ("\n" + json.dumps(payload) if payload else "")
            if message else None
        )
