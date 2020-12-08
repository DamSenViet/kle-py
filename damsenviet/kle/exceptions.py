from typing import (
    Union,
    List,
    Dict,
)

from typeguard import typechecked


class DeserializeException(Exception):
    """Class for all exceptions encountered during deserialization."""

    @typechecked
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
        ] = None,
    ):
        """Construct a `DeserializeException`.

        :param message: A message indicating a processing error during
            deserialization of the KLE file.
        :type message: str
        :param payload: The offending payload during deserialization, defaults
            to `None`.
        :type payload: Union[dict, list, None], optional
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
