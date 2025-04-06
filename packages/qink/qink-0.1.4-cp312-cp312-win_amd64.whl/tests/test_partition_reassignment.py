import asyncio
import logging
import pytest
from datetime import timedelta
from typing import Dict, List, Optional

from qink.lib.models import PartitionState
from qink.lib.qink import Qink
from qink.lib.qink_source import Message, QinkSource
from qink.lib.qink_storage import QinkStorage
from qink.lib.qink_storage_provider import QinkStorageProvider

from tests.test_utils import wait_until_condition


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


@pytest.mark.asyncio
async def test_partition_reassignment(
    logger, storage_provider, controlled_source
):
    """Test that Qink handles partition reassignment correctly
    during active processing."""

    # Create a Qink instance with a short checkpoint interval
    qink = Qink(
        logger=logger,
        storage_provider=storage_provider,
        workers_per_partition=1,
        checkpoint_interval=timedelta(milliseconds=100),
    )
    qink.source(controlled_source)

    # Add test messages to partition 0
    messages_p0 = [
        Message(key=b"key1", value=b"value1", timestamp=1000, offset=0),
        Message(key=b"key2", value=b"value2", timestamp=1001, offset=1),
        Message(key=b"key1", value=b"value3", timestamp=1002, offset=2),
    ]
    controlled_source.add_messages(0, messages_p0)

    # Start with only partition 0
    controlled_source.assign_partitions([0])

    # Start Qink
    qink.start()

    # Wait for processing to start
    await wait_until_condition(lambda: len(qink._partition_consumers) > 0)
    await wait_until_condition(
        lambda: qink._partition_consumers[0]._state is not None
    )

    # Wait until partition 0 has processed all messages
    await wait_until_condition(
        lambda: (
            0 in qink._partition_consumers
            and qink._partition_consumers[0]._state.offset == 2
        )
    )

    # Wait for at least one checkpoint to happen
    await wait_until_condition(
        lambda: (
            0 in qink._partition_consumers
            and qink._partition_consumers[0]._checkpoint_count > 0
        )
    )

    # Prepare messages for partition 1
    messages_p1 = [
        Message(key=b"key3", value=b"value4", timestamp=1003, offset=0),
        Message(key=b"key4", value=b"value5", timestamp=1004, offset=1),
    ]
    controlled_source.add_messages(1, messages_p1)

    p0_checkpoint_count = qink._partition_consumers[0]._checkpoint_count

    await wait_until_condition(
        lambda: (
            1 in qink._partition_consumers
            and qink._partition_consumers[1]._checkpoint_count
            > p0_checkpoint_count
        )
    )

    # Reassign partitions: revoke 0, assign 1
    controlled_source.revoke_partitions([0])

    # Wait a bit for revocation to process
    await asyncio.sleep(0.2)

    # Verify partition 0 has been removed from consumers
    assert (
        0 not in qink._partition_consumers
    ), "Partition 0 was not removed from consumers"

    # Assign partition 1
    controlled_source.assign_partitions([1])

    # Wait for partition 1 to be assigned and process messages
    await wait_until_condition(lambda: 1 in qink._partition_consumers)
    await wait_until_condition(
        lambda: qink._partition_consumers[1]._state is not None
    )

    await wait_until_condition(
        lambda: (
            1 in qink._partition_consumers
            and qink._partition_consumers[1]._state.offset == 1
        )
    )

    p1_checkpoint_count = qink._partition_consumers[1]._checkpoint_count

    await wait_until_condition(
        lambda: (
            1 in qink._partition_consumers
            and qink._partition_consumers[1]._checkpoint_count
            > p1_checkpoint_count
        )
    )

    # Stop Qink
    await qink.stop()

    # Verify a checkpoint was created for partition 0
    storage = QinkStorage(storage_provider, logger)

    # Get the state for partition 0
    p0_state = await storage.get_partition_state(0)
    p1_state = await storage.get_partition_state(1)

    assert p0_state is not None, "State for partition 0 should exist"
    assert (
        p0_state.offset == 3
    ), "State for partition 0 should have correct offset"

    # Verify partition 1 was correctly processed
    p1_state = await storage.get_partition_state(1)
    assert p1_state is not None, "State for partition 1 should exist"
    assert (
        p1_state.offset == 2
    ), "State for partition 1 should have correct offset"
