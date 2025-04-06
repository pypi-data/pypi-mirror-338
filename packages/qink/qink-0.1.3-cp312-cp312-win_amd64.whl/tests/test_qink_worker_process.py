import pytest
from multiprocessing import Process, connection

from qink.lib.qink_source import Message
from qink.lib.qink_worker_process import QinkWorkerProcess

from tests.test_utils import (
    CountItemsProcessFunction,
    ErrorProcessFunction,
)


@pytest.mark.asyncio
async def test_worker_process():
    """Test the QinkWorkerProcess using a connection Listener/Client pair."""
    # Create a listener for the worker to connect to
    listener = connection.Listener(address=("localhost", 0))
    address = listener.address

    # Create the test process function module
    process_function = CountItemsProcessFunction()
    process_function_path = process_function.get_module_path()

    # Start the worker process
    worker_process = Process(
        target=QinkWorkerProcess, args=(address, process_function_path)
    )
    worker_process.start()

    try:
        # Accept the connection from the worker
        conn = listener.accept()

        # Send initial empty state
        initial_states = {}
        conn.send(initial_states)

        # Send test messages with the same key
        messages = [
            Message(key=b"key1", value=b"apple", timestamp=1000, offset=0),
            Message(key=b"key1", value=b"banana", timestamp=1001, offset=1),
            Message(key=b"key1", value=b"apple", timestamp=1002, offset=2),
        ]
        conn.send(messages)

        # Wait for "drained" response
        response = conn.recv()
        assert response == b"drained", "Expected 'drained' response"

        # Request key states
        conn.send(b"collect_key_states")

        # Receive key states
        key_states = conn.recv()

        # Check the states
        assert "key1" in key_states, "Expected 'key1' in key states"
        assert key_states["key1"]["apple"] == 2, "Expected 2 apples"
        assert key_states["key1"]["banana"] == 1, "Expected 1 banana"

        # Send messages with a different key
        messages = [
            Message(key=b"key2", value=b"orange", timestamp=1003, offset=3),
            Message(key=b"key2", value=b"grape", timestamp=1004, offset=4),
            Message(key=b"key2", value=b"orange", timestamp=1005, offset=5),
        ]
        conn.send(messages)

        # Wait for "drained" response
        response = conn.recv()
        assert response == b"drained", "Expected 'drained' response"

        # Request key states again
        conn.send(b"collect_key_states")

        # Receive updated key states
        key_states = conn.recv()

        # Check both keys are in the state
        assert "key1" in key_states, "Expected 'key1' in key states"
        assert "key2" in key_states, "Expected 'key2' in key states"

        # Check key1 state is unchanged
        assert key_states["key1"]["apple"] == 2, "Expected 2 apples"
        assert key_states["key1"]["banana"] == 1, "Expected 1 banana"

        # Check key2 state
        assert key_states["key2"]["orange"] == 2, "Expected 2 oranges"
        assert key_states["key2"]["grape"] == 1, "Expected 1 grape"

    finally:
        # Clean up
        worker_process.terminate()
        worker_process.join(timeout=1.0)
        listener.close()


@pytest.mark.asyncio
async def test_worker_process_without_process_function():
    """Test the QinkWorkerProcess without a process function."""
    # Create a listener for the worker to connect to
    listener = connection.Listener(address=("localhost", 0))
    address = listener.address

    # Start the worker process without a process function
    worker_process = Process(target=QinkWorkerProcess, args=(address, None))
    worker_process.start()

    try:
        # Accept the connection from the worker
        conn = listener.accept()

        # Send initial empty state
        initial_states = {}
        conn.send(initial_states)

        # Send test messages
        messages = [
            Message(key=b"key1", value=b"apple", timestamp=1000, offset=0),
            Message(key=b"key1", value=b"banana", timestamp=1001, offset=1),
        ]
        conn.send(messages)

        # Wait for "drained" response
        # Worker should respond even without a process function
        response = conn.recv()
        assert response == b"drained", "Expected 'drained' response"

        # Request key states
        conn.send(b"collect_key_states")

        # Receive key states - should be empty since no process
        # function to update state
        key_states = conn.recv()
        assert len(key_states) == 0, "Expected empty key states"

    finally:
        # Clean up
        worker_process.terminate()
        worker_process.join(timeout=1.0)
        listener.close()


@pytest.mark.asyncio
async def test_worker_process_error_handling():
    """Test QinkWorkerProcess error handling."""

    # Create a listener for the worker to connect to
    listener = connection.Listener(address=("localhost", 0))
    address = listener.address

    # Get the module path of the error process function
    process_function_path = ErrorProcessFunction().get_module_path()

    # Start the worker process
    worker_process = Process(
        target=QinkWorkerProcess, args=(address, process_function_path)
    )
    worker_process.start()

    try:
        # Accept the connection from the worker
        conn = listener.accept()

        # Send initial empty state
        initial_states = {}
        conn.send(initial_states)

        # Send test messages
        messages = [
            Message(key=b"key1", value=b"apple", timestamp=1000, offset=0),
        ]
        conn.send(messages)

        # The worker should handle the error and still respond with "drained"
        response = conn.recv()
        assert response == b"drained", "Expected 'drained' response"

    finally:
        # Clean up
        worker_process.terminate()
        worker_process.join(timeout=1.0)
        listener.close()
