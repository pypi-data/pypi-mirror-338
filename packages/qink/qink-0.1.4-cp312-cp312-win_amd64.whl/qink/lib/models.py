from dataclasses import dataclass
from typing import Any


@dataclass
class KeyState(dict[str, Any]):
    """State for a specific key."""


@dataclass
class PartitionState:
    partition: int
    offset: int
    """offset - 1 is the last successfully processed offset."""
    state: dict[str, KeyState]
