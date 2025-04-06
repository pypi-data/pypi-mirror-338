from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from .qink_source import Message

T = TypeVar("T")  # Type variable for state


class ProcessFunction(ABC, Generic[T]):
    """
    Abstract base class for user-defined processing functions.

    Users should implement this class to define custom processing logic
    for messages. The class is generic over the state type T, which can
    be any serializable type.
    """

    def __init__(self):
        """Initialize the process function."""
        pass

    @abstractmethod
    async def process(
        self, message: Message, state: Optional[T] = None
    ) -> Optional[T]:
        """
        Process a message and update the state.

        Args:
            message: The message to process
            state: The current state for the message key, or
                None if no state exists

        Returns:
            The updated state, or None if no state should be stored
        """
        pass

    def get_module_path(self) -> str:
        """Return the module path for this class."""
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}"
