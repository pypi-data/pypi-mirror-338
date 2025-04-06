import asyncio
import logging
import pytest
from typing import Dict, List, Optional

from qink.lib.models import PartitionState
from qink.lib.qink import Qink
from qink.lib.qink_source import Message, QinkSource
from qink.lib.qink_storage_provider import QinkStorageProvider
from qink.lib.process_function import ProcessFunction


class MockStorageProvider(QinkStorageProvider):
    """A mock storage provider that stores data in memory."""

    def __init__(self):
        super().__init__()
        self.storage: Dict[str, bytes] = {}
        self.set_calls = 0
        self.get_calls = 0

    async def get_file_contents_async(self, file_path: str) -> Optional[bytes]:
        self.get_calls += 1
        return self.storage.get(file_path)

    async def set_file_contents_async(self, file_path: str, content: bytes):
        self.set_calls += 1
        self.storage[file_path] = content


class MockSource(QinkSource):
    """A mock source that provides predefined messages."""

    def __init__(self, logger: logging.Logger):
        super().__init__(logger)
        self.messages: Dict[int, List[Message]] = {}
        self.partition_offsets: Dict[int, int] = {}
        self.seeks: List[PartitionState] = []
        self.partitions = [0]
        self.get_many_calls = 0

    async def stop(self):
        if self._listener:
            self._listener.on_partitions_revoked(self.partitions)

    async def seek(self, state: PartitionState):
        self.seeks.append(state)
        self.partition_offsets[state.partition] = state.offset

    async def start(self):
        if self._listener:
            self._listener.on_partitions_assigned(self.partitions)

    async def get_many(self, partition: int) -> List[Message]:
        self.get_many_calls += 1

        assert partition in self.partition_offsets

        await asyncio.sleep(0.01)

        offset = self.partition_offsets[partition]

        return self.messages[partition][offset:]

    def add_messages(self, partition: int, messages: List[Message]):
        if partition not in self.messages:
            self.messages[partition] = []

        for message in messages:
            self.messages[partition].append(message)


class ControlledMockSource(QinkSource):
    """A mock source that allows controlled partition assignment/revocation."""

    def __init__(self, logger: logging.Logger):
        super().__init__(logger)
        self.messages: Dict[int, List[Message]] = {}
        self.partition_offsets: Dict[int, int] = {}
        self.seeks: Dict[int, List[PartitionState]] = {}
        self.partitions = []
        self.get_many_calls = 0

    async def stop(self):
        if self._listener:
            self._listener.on_partitions_revoked(self.partitions)

    async def seek(self, state: PartitionState):
        if state.partition not in self.seeks:
            self.seeks[state.partition] = []

        self.seeks[state.partition].append(state)
        self.partition_offsets[state.partition] = state.offset

    async def start(self):
        if self._listener:
            self._listener.on_partitions_assigned(self.partitions)

    async def get_many(self, partition: int) -> List[Message]:
        self.get_many_calls += 1

        if partition not in self.partition_offsets:
            return []

        await asyncio.sleep(0.01)

        offset = self.partition_offsets[partition]

        if partition not in self.messages:
            return []

        return self.messages[partition][offset:]

    def add_messages(self, partition: int, messages: List[Message]):
        if partition not in self.messages:
            self.messages[partition] = []

        for message in messages:
            self.messages[partition].append(message)

    def assign_partitions(self, partitions: List[int]):
        """Manually assign partitions to this source."""
        self.partitions = partitions
        if self._listener:
            self._listener.on_partitions_assigned(partitions)

    def revoke_partitions(self, partitions: List[int]):
        """Manually revoke partitions from this source."""
        for partition in partitions:
            if partition in self.partitions:
                self.partitions.remove(partition)

        if self._listener:
            self._listener.on_partitions_revoked(partitions)


class CounterProcessFunction(ProcessFunction[Dict[str, int]]):
    """A simple process function that counts occurrences of values."""

    async def process(
        self, message: Message, state: Optional[Dict[str, int]] = None
    ) -> Optional[Dict[str, int]]:
        """Count occurrences of values in messages."""
        if state is None:
            state = {}

        value_str = message.value.decode("utf-8")

        print(
            f"[key: {message.key}] Processing message: {message.value} "
            f"with state: {state}"
        )

        if value_str in state:
            state[value_str] += 1
        else:
            state[value_str] = 1

        return state


class CountItemsProcessFunction(ProcessFunction[Dict[str, int]]):
    """A test process function that counts occurrences of values."""

    async def process(
        self, message: Message, state: Optional[Dict[str, int]] = None
    ) -> Optional[Dict[str, int]]:
        """Count occurrences of values in messages."""
        if state is None:
            state = {}

        value_str = message.value.decode("utf-8")
        if value_str in state:
            state[value_str] += 1
        else:
            state[value_str] = 1

        return state


class ErrorProcessFunction(ProcessFunction[Dict[str, int]]):
    """A process function that raises an exception."""

    async def process(
        self, message: Message, state: Optional[Dict[str, int]] = None
    ) -> Optional[Dict[str, int]]:
        """Raise an exception."""
        raise ValueError("Test error")


# Helper functions for testing
async def wait_until_offset_is(
    qink: Qink, offset: int, timeout_ms: int = 5000
):
    start_time = asyncio.get_event_loop().time() * 1000
    while True:
        await asyncio.sleep(0.1)
        if (
            (0 in qink._partition_consumers)
            and (qink._partition_consumers[0]._state is not None)
            and (qink._partition_consumers[0]._state.offset == offset)
        ):
            return

        if asyncio.get_event_loop().time() * 1000 - start_time > timeout_ms:
            raise Exception(f"Timeout waiting for offset to be {offset}")


async def wait_until_checkpoint_count_is(
    qink: Qink, count: int, timeout_ms: int = 5000
):
    start_time = asyncio.get_event_loop().time() * 1000
    while True:
        await asyncio.sleep(0.1)
        if qink._partition_consumers[0]._checkpoint_count == count:
            return

        if asyncio.get_event_loop().time() * 1000 - start_time > timeout_ms:
            raise Exception(
                f"Timeout waiting for checkpoint count to be {count}"
            )


async def wait_until_condition(condition_fn, timeout_ms=2000, interval_ms=100):
    start_time = asyncio.get_event_loop().time() * 1000
    while True:
        if condition_fn():
            return True

        if (asyncio.get_event_loop().time() * 1000 - start_time) > timeout_ms:
            return False

        await asyncio.sleep(interval_ms / 1000)


# Common fixtures - don't import these directly,
# they should be imported by pytest
@pytest.fixture
def logger():
    logger = logging.getLogger("test")
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture
def storage_provider():
    return MockStorageProvider()


@pytest.fixture
def source(logger):
    return MockSource(logger)


@pytest.fixture
def controlled_source(logger):
    return ControlledMockSource(logger)


@pytest.fixture
def process_function():
    return CounterProcessFunction()


@pytest.fixture
def count_items_process_function():
    return CountItemsProcessFunction()


@pytest.fixture
def error_process_function():
    return ErrorProcessFunction()
