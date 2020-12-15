from typing import (
    Any,
    Union,
    List,
    Dict,
)

__all__ = [
    "IllegalValueException",
    "DeserializeException",
]


class IllegalValueException(Exception):
    """Exceptions for encountering illegal values."""

    def __init__(
        self,
        message: str,
        value: Any,
    ):
        """Initializes an IllegalArgumentException.

        :param message: A message indicating an illegal argument.
        :type message: str
        """
        super().__init__(message)
        self.value = value


class DeserializeException(Exception):
    """Exceptions encountered during deserialization."""

    def __init__(
        self,
        message: str,
        payload: Union[
            int,
            float,
            str,
            None,
            Dict,
            List,
        ],
    ):
        """Initializes a DeserializeException.

        :param message: the error message
        :type message: str
        :param payload: the offending json payload, defaults to None
        :type payload: Union[ int, float, str, None, Dict, List, ], optional
        """
        super().__init__(message)
        self.payload: Union[
            int,
            float,
            str,
            None,
            Dict,
            List,
        ] = payload
