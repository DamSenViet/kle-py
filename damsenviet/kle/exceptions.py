from typing import (
    Union,
    List,
    Dict,
)

__all__ = ["DeserializeException"]


class DeserializeException(Exception):
    """An exception encountered during deserialization."""

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
        :param payload: the offending json payload, defaults to None
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
