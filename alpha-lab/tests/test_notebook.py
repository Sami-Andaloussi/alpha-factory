"""The notebooks' runner: this interpreter's kernel, shut down however the notebook ends; a kernel
that cannot start, or an interrupt as it gets ready, leaves one line and the handlers as they were."""
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import nbformat
import pytest

LAB = Path(__file__).resolve().parent.parent

TELL = """import socket
before = [signal.getsignal(signal.SIGINT), signal.getsignal(signal.SIGTERM)]   # ignored in a shell's background
wake, _ = socket.socketpair()
wake.setblocking(False)
signal.set_wakeup_fd(wake.fileno())                                           # the caller's, as a loop sets it
try:
    notebook.execute(Path(sys.argv[1]), timeout=60)
except Exception as error:
    print("the notebook failed:", type(error).__name__, file=sys.stderr)
kept = [signal.getsignal(signal.SIGINT), signal.getsignal(signal.SIGTERM)] == before
print("handlers as they were" if kept and signal.set_wakeup_fd(-1) == wake.fileno() else "handlers changed")
"""

RUN = """import signal
import sys
from pathlib import Path
from lab import notebook
""" + TELL

READY = """import asyncio
import os
import signal
import sys
from pathlib import Path
from jupyter_client.asynchronous.client import AsyncKernelClient
from lab import notebook
ready = AsyncKernelClient.wait_for_ready


async def interrupted(self, *args, **options):     # Ctrl-C while the kernel gets ready
    os.kill(os.getpid(), getattr(signal, sys.argv[2]))
    await asyncio.sleep(0.05)
    return await ready(self, *args, **options)
AsyncKernelClient.wait_for_ready = interrupted
""" + TELL

MANY = """import os
import sys
import threading
from pathlib import Path
from lab import notebook
counts = []
for k in range(6):
    try:
        notebook.execute(Path(sys.argv[1 + k % 2]), timeout=60)
    except Exception:
        pass
    counts.append((len(os.listdir("/dev/fd")), threading.active_count()))
print(counts[1] == counts[-1], counts)
"""


def book(path, source):
    nbformat.write(nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(source)]), path)
    return path


def test_the_kernel_is_this_interpreter_s_own(tmp_path):
    spec = tmp_path / "spec" / "kernels" / "python3"
    spec.mkdir(parents=True)
    (spec / "kernel.json").write_text('{"argv": ["/nonexistent/python", "-f", "{connection_file}"], '
                                      '"display_name": "elsewhere", "language": "python"}')
    path = book(tmp_path / "n.ipynb", "import sys\nprint(sys.executable)")
    done = subprocess.run([sys.executable, "-c", RUN, str(path)], cwd=LAB, capture_output=True, text=True, timeout=300,
                          env={**os.environ, "JUPYTER_PATH": str(tmp_path / "spec")})   # found first by name
    assert done.stderr == ""
    shown = nbformat.read(path, as_version=4).cells[0].outputs[0]["text"].strip()
    assert Path(shown).resolve() == Path(sys.executable).resolve()


def test_a_kernel_that_cannot_start_leaves_one_line_and_nothing_at_exit(tmp_path):
    fake = tmp_path / "fake"
    fake.mkdir()
    (fake / "ipykernel_launcher.py").write_text("import sys\nprint('the kernel s own log', file=sys.stderr)\n"
                                                "sys.exit(1)\n")
    path = book(tmp_path / "n.ipynb", "1")
    done = subprocess.run([sys.executable, "-c", RUN, str(path)], cwd=LAB, capture_output=True, text=True, timeout=300,
                          env={**os.environ, "PYTHONPATH": os.pathsep.join([str(fake), str(LAB)])})
    assert done.stderr.strip() == "the notebook failed: RuntimeError"  # no kernel log, no warning at exit
    assert done.stdout.strip() == "handlers as they were"


@pytest.mark.parametrize("interrupt", ["SIGINT", "SIGTERM"])
def test_an_interrupt_while_the_kernel_gets_ready_raises_and_leaves_the_handlers_as_they_were(tmp_path, interrupt):
    path = book(tmp_path / "n.ipynb", "1")
    done = subprocess.run([sys.executable, "-c", READY, str(path), interrupt], cwd=LAB, capture_output=True, text=True,
                          timeout=300)
    assert done.stderr.strip() == "the notebook failed: RuntimeError"  # an error the report tells, not a traceback
    assert done.stdout.strip() == "handlers as they were"


def test_notebooks_run_one_after_another_leave_no_connection_or_thread_behind(tmp_path):
    runs, fails = book(tmp_path / "runs.ipynb", "1"), book(tmp_path / "fails.ipynb", "raise ValueError('no')")
    done = subprocess.run([sys.executable, "-c", MANY, str(runs), str(fails)], cwd=LAB, capture_output=True, text=True,
                          timeout=300)
    assert done.stdout.startswith("True"), done.stdout                  # open files and threads, as after the second


def gone(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return True
    return False


@pytest.mark.parametrize("cell", ["pass", "raise ValueError('a cell that fails')"])
def test_the_kernel_is_shut_down_once_the_notebook_has_run(tmp_path, cell):
    from lab import notebook
    path = book(tmp_path / "n.ipynb", "import os\nopen('pid', 'w').write(str(os.getpid()))\n" + cell)
    if cell.startswith("raise"):
        with pytest.raises(Exception, match="a cell that fails"):      # a cell that fails stops the notebook
            notebook.execute(path, timeout=60)
    else:
        notebook.execute(path, timeout=60)
    assert gone(int((tmp_path / "pid").read_text()))


@pytest.mark.parametrize("cell, timeout", [("import time\ntime.sleep(60)", 2),
                                           ("import signal\nos.kill(os.getpid(), signal.SIGKILL)", 60)])
def test_a_cell_past_its_timeout_or_a_kernel_that_dies_raises_at_once(tmp_path, cell, timeout):
    from lab import notebook
    path = book(tmp_path / "n.ipynb", "import os\nopen('pid', 'w').write(str(os.getpid()))\n" + cell)
    began = time.time()
    with pytest.raises(Exception):
        notebook.execute(path, timeout=timeout)
    assert time.time() - began < 30 and gone(int((tmp_path / "pid").read_text()))


def test_the_runner_runs_from_a_thread_other_than_the_main_one(tmp_path):
    from lab import notebook
    path, failed = book(tmp_path / "n.ipynb", "1 + 1"), []

    def work():
        try:
            notebook.execute(path, timeout=60)
        except Exception as error:
            failed.append(error)
    worker = threading.Thread(target=work)
    worker.start()
    worker.join(120)
    assert not failed and nbformat.read(path, as_version=4).cells[0].outputs[0]["data"]["text/plain"] == "2"
