"""Notebooks are run in their own folder and saved with their outputs, so that GitHub shows them."""
from __future__ import annotations

import atexit
import subprocess
from pathlib import Path


def execute(notebook: Path, timeout: int = 900, metadata: dict | None = None) -> None:
    """Run `notebook` in its folder, each cell for `timeout` seconds at most, and save it with its
    outputs and `metadata`. The kernel is this interpreter's own, never one found by name on
    Jupyter's paths, and it is shut down once the notebook has run, however it ends. Its manager is
    asynchronous, so that the client's loop keeps running while a cell does: a cell past its
    timeout, a kernel that dies, and an interrupt during a cell or while the kernel gets ready raise
    instead of waiting for good (one that lands as the kernel is launched may be lost), and the
    handlers of interrupts are put back as they were. The kernel's own log is not shown: a cell
    that fails raises with its error, and the notebook is saved only once every cell has run."""
    import asyncio
    import signal
    import threading

    import nbformat
    from jupyter_client import AsyncKernelManager
    from jupyter_client.kernelspec import KernelSpecManager
    from jupyter_core.utils import run_sync
    from nbclient import NotebookClient
    book = nbformat.read(notebook, as_version=4)
    own = AsyncKernelManager(kernel_name="python3", kernel_spec_manager=KernelSpecManager(kernel_dirs=[]))
    client = NotebookClient(book, km=own, timeout=timeout, kernel_name="python3",
                            resources={"metadata": {"path": str(notebook.parent)}})
    main = threading.current_thread() is threading.main_thread()      # only its handlers can change
    kept = {number: signal.getsignal(number) for number in (signal.SIGINT, signal.SIGTERM)} if main else {}
    wakeup = signal.set_wakeup_fd(-1) if main else -1
    if main:
        signal.set_wakeup_fd(wakeup)
    try:
        client.execute(stderr=subprocess.DEVNULL)
    except asyncio.CancelledError as error:        # the client's own clean-up, as the kernel starts
        raise RuntimeError("the notebook was interrupted as its kernel started") from error
    finally:
        for number, handler in kept.items():        # the client leaves its own when the kernel does not start
            if handler is not None:
                signal.signal(number, handler)
        if main:
            signal.set_wakeup_fd(wakeup)
        atexit.unregister(client._cleanup_kernel)   # a kernel that never started leaves nothing to clean at exit
        if client.kc is not None:
            client.kc.stop_channels()
        if own.has_kernel:                          # the manager is the lab's: the client leaves its kernel running
            run_sync(own.shutdown_kernel)(now=True)
    book.metadata.update(metadata or {})
    nbformat.write(book, notebook)
