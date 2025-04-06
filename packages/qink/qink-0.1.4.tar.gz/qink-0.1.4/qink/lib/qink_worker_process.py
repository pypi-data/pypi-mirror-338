import asyncio
import importlib
from multiprocessing import connection
from typing import Optional, Union

from .qink_source import Message
from .models import KeyState


class QinkWorkerProcess:
    """
    Worker process for multiprocessing.Process targets.
    Handles messages, processing, and state maintenance.
    """

    def __init__(
        self,
        address: tuple[str, int],
        process_function_path: Optional[str] = None,
    ):
        """
        Initialize the worker process.

        Args:
            address: The address to connect to the main process
            process_function_path: Process function module path
        """
        self._client = connection.Client(address)
        self._process_func = self._create_process_func(process_function_path)

        asyncio.run(self._run())

    @staticmethod
    def _create_process_func(process_function_path: Optional[str]):
        if process_function_path:
            module_path, class_name = process_function_path.rsplit(".", 1)
            module = importlib.import_module(module_path)
            process_class = getattr(module, class_name)
            return process_class()
        return None

    async def _receive(self):
        return await asyncio.get_running_loop().run_in_executor(
            None, self._client.recv
        )

    async def _run(self):
        states: dict[str, KeyState] = await self._receive()

        while True:
            try:
                data: Union[list[Message], bytes, str] = await self._receive()

                if data == b"collect_key_states":
                    self._client.send(states)
                else:
                    # Process messages if we have any
                    if len(data) > 0 and self._process_func:
                        for message in data:
                            # Get the message key as string
                            key = message.key.decode("utf-8")
                            current_state = states.get(key)

                            try:
                                # Process the message
                                new_state = await self._process_func.process(
                                    message, current_state
                                )
                            except Exception:
                                new_state = current_state

                            # Update state if needed
                            if new_state is not None:
                                states[key] = new_state
                            elif key in states and new_state is None:
                                # Remove the state if None is returned
                                del states[key]

                    self._client.send(b"drained")
            except Exception as e:
                print(f"Worker process error: {e}")
                await asyncio.sleep(1)
