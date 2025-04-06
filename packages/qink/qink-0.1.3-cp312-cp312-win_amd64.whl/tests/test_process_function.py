import pytest
from datetime import timedelta

from qink.lib.qink import Qink
from qink.lib.qink_source import Message
from qink.lib.qink_storage import QinkStorage

from tests.test_utils import (
    wait_until_offset_is,
    wait_until_checkpoint_count_is,
)


@pytest.mark.asyncio
async def test_process_function(
    logger, storage_provider, source, process_function
):
    """Test that the process function correctly processes messages."""

    # Create a Qink instance with a short checkpoint interval
    qink = Qink(
        logger=logger,
        storage_provider=storage_provider,
        workers_per_partition=1,
        checkpoint_interval=timedelta(milliseconds=100),
    )
    qink.source(source).process(process_function)

    # Add test messages with the same key but different values
    test_messages = [
        Message(key=b"key1", value=b"apple", timestamp=1000, offset=0),
        Message(key=b"key1", value=b"banana", timestamp=1001, offset=1),
        Message(key=b"key1", value=b"apple", timestamp=1002, offset=2),
        Message(key=b"key1", value=b"orange", timestamp=1003, offset=3),
        Message(key=b"key1", value=b"apple", timestamp=1004, offset=4),
    ]
    source.add_messages(0, test_messages)

    # Start Qink
    qink.start()

    # Wait for processing to complete and checkpoint to happen
    await wait_until_offset_is(qink, 5, timeout_ms=10000)

    # Get the current checkpoint count
    checkpoint_count = qink._partition_consumers[0]._checkpoint_count

    # Wait for an additional checkpoint to occur
    await wait_until_checkpoint_count_is(
        qink, checkpoint_count + 1, timeout_ms=10000
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

    # Verify the state contains the correct counts
    assert state is not None, "State should not be None"
    assert "key1" in state.state, "Key1 should be in state"

    key1_state = state.state["key1"]
    assert key1_state["apple"] == 3, "Should count 3 apples"
    assert key1_state["banana"] == 1, "Should count 1 banana"
    assert key1_state["orange"] == 1, "Should count 1 orange"


@pytest.mark.asyncio
async def test_process_function_with_multiple_keys(
    logger, storage_provider, source, process_function
):
    """Test that the process function correctly handles multiple keys."""

    # Create a Qink instance
    qink = Qink(
        logger=logger,
        storage_provider=storage_provider,
        workers_per_partition=1,
        checkpoint_interval=timedelta(milliseconds=100),
    )
    qink.source(source).process(process_function)

    # Add test messages with different keys
    test_messages = [
        Message(key=b"key1", value=b"apple", timestamp=1000, offset=0),
        Message(key=b"key2", value=b"banana", timestamp=1001, offset=1),
        Message(key=b"key1", value=b"apple", timestamp=1002, offset=2),
        Message(key=b"key2", value=b"orange", timestamp=1003, offset=3),
        Message(key=b"key3", value=b"apple", timestamp=1004, offset=4),
    ]
    source.add_messages(0, test_messages)

    # Start Qink
    qink.start()

    # Wait for processing to complete and checkpoint to happen
    await wait_until_offset_is(qink, 5, timeout_ms=10000)

    # Get the current checkpoint count
    checkpoint_count = qink._partition_consumers[0]._checkpoint_count

    # Wait for an additional checkpoint to occur
    await wait_until_checkpoint_count_is(
        qink, checkpoint_count + 1, timeout_ms=10000
    )

    # Stop Qink
    await qink.stop()

    # Load state from storage to verify
    storage = QinkStorage(storage_provider, logger)
    state = await storage.get_partition_state(0)

    # Verify the state contains the correct counts for each key
    assert state is not None, "State should not be None"
    assert "key1" in state.state, "key1 should be in state"
    assert "key2" in state.state, "key2 should be in state"
    assert "key3" in state.state, "key3 should be in state"

    key1_state = state.state["key1"]
    assert key1_state["apple"] == 2, "key1 should count 2 apples"

    key2_state = state.state["key2"]
    assert key2_state["banana"] == 1, "key2 should count 1 banana"
    assert key2_state["orange"] == 1, "key2 should count 1 orange"

    key3_state = state.state["key3"]
    assert key3_state["apple"] == 1, "key3 should count 1 apple"
