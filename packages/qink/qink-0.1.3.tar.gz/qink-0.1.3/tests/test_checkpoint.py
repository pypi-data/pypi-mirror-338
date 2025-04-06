import asyncio
import pytest
from datetime import timedelta

from qink.lib.models import PartitionState
from qink.lib.qink import Qink
from qink.lib.qink_source import Message
from qink.lib.qink_storage import QinkStorage

from tests.test_utils import (
    wait_until_offset_is,
    wait_until_checkpoint_count_is,
)


@pytest.mark.asyncio
async def test_checkpoint_saves_state(logger, storage_provider, source):
    """Test that Qink creates checkpoints at the specified interval."""

    # Create a Qink instance with a short checkpoint interval
    qink = Qink(
        logger=logger,
        storage_provider=storage_provider,
        workers_per_partition=1,
        checkpoint_interval=timedelta(milliseconds=100),
    )
    qink.source(source)

    # Add test messages
    test_messages = [
        Message(key=b"key1", value=b"value1", timestamp=1000, offset=0),
        Message(key=b"key2", value=b"value2", timestamp=1001, offset=1),
        Message(key=b"key1", value=b"value3", timestamp=1002, offset=2),
    ]
    source.add_messages(0, test_messages)

    # Start Qink
    qink.start()

    # Wait for checkpoint to happen (longer than checkpoint_interval)
    while True:
        await asyncio.sleep(0.1)

        if qink._partition_consumers[0]._checkpoint_count > 2:
            break

    await wait_until_offset_is(qink, 3, timeout_ms=4_000)
    partition_consumer = qink._partition_consumers[0]

    checkpoint_count = partition_consumer._checkpoint_count
    await wait_until_checkpoint_count_is(
        qink, checkpoint_count + 1, timeout_ms=4_000
    )

    # Stop Qink
    await qink.stop()

    # Check if a checkpoint was created
    assert storage_provider.set_calls > 0, "No checkpoint was created"

    # Get the checkpoint state
    state_file = "p-0.state.pkl"
    assert state_file in storage_provider.storage, "Checkpoint file not found"

    # Load state from storage to verify
    storage = QinkStorage(storage_provider, logger)
    state = await storage.get_partition_state(0)

    # Verify the checkpoint contains the correct offset
    assert state is not None, "State should not be None"
    assert state.offset == 3, "Checkpoint has wrong offset"


@pytest.mark.asyncio
async def test_resume_from_checkpoint(logger, storage_provider, source):
    """Test that Qink resumes from the saved checkpoint."""
    # First, create an initial state and save it
    initial_state = PartitionState(
        partition=0,
        offset=5,
        state={"key1": {"processed": True}},
    )
    storage = QinkStorage(storage_provider, logger)
    await storage.set_partition_state(0, initial_state)

    # Create a Qink instance
    qink = Qink(
        logger=logger,
        storage_provider=storage_provider,
        workers_per_partition=1,
        checkpoint_interval=timedelta(seconds=10),
    )
    qink.source(source)

    # Start Qink
    qink.start()

    # Wait for startup
    async def wait_until_seek_count_gt(count: int, timeout_ms: int = 1000):
        start_time_ms = asyncio.get_event_loop().time() * 1000
        while True:
            await asyncio.sleep(0.1)
            if len(source.seeks) > count:
                return

            current_time_ms = asyncio.get_event_loop().time() * 1000

            if current_time_ms - start_time_ms > timeout_ms:
                raise Exception(
                    f"Timeout waiting for seek count to be > {count}"
                )

    await wait_until_seek_count_gt(0, timeout_ms=2_000)

    # Check if the source received a seek call with the correct state
    seek_state = source.seeks[0]
    assert seek_state.offset == 5, "Did not seek to the correct offset"
    assert (
        seek_state.state["key1"]["processed"] is True
    ), "Did not process key1"

    # Stop Qink
    await qink.stop()
