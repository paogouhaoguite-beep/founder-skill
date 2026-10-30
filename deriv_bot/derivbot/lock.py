"""Single-instance lock: two bots on one journal would double-trade and split risk limits."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import IO


class AlreadyRunningError(RuntimeError):
    """Another bot process already holds the lock for this journal and mode."""


class InstanceLock:
    """OS-level exclusive lock on a file. Released automatically if the process dies,
    so a crash never leaves a stale lock behind. Works on Linux, macOS and Windows."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._fh: IO[str] | None = None

    def acquire(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fh = open(self.path, "a+", encoding="utf-8")  # noqa: SIM115 - held for process life
        try:
            if sys.platform == "win32":
                import msvcrt

                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl

                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            fh.close()
            raise AlreadyRunningError(
                f"another bot is already running on this journal ({self.path}). "
                "Stop it first; two bots would double-trade and bypass risk limits.") from exc
        fh.seek(0)
        fh.truncate()
        fh.write(str(os.getpid()))
        fh.flush()
        self._fh = fh

    def release(self) -> None:
        if self._fh is not None:
            self._fh.close()  # closing the handle releases the OS lock
            self._fh = None

    def __enter__(self) -> InstanceLock:
        self.acquire()
        return self

    def __exit__(self, *exc: object) -> None:
        self.release()
