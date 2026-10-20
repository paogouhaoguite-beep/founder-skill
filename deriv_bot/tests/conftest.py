import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from derivbot.config import Config, config_from_dict  # noqa: E402
from derivbot.database import TradeDatabase  # noqa: E402


class FakeClock:
    """Controllable wall clock shared by the mock server, executors and the bot."""

    def __init__(self, t: float | None = None) -> None:
        # Start at real "now" so DB timestamps (wall clock) and bot dates agree.
        self.t = float(int(time.time())) if t is None else t

    def __call__(self) -> float:
        return self.t

    def advance(self, seconds: float) -> None:
        self.t += seconds


@pytest.fixture
def cfg() -> Config:
    return config_from_dict({
        "api": {"max_retries": 2, "reconnect_base_delay": 0.01, "reconnect_max_delay": 0.02,
                "rate_limit_backoff": 0.01, "request_timeout": 3.0},
        "trading": {"poll_interval": 0.01},
        "logging": {"file": ""},
    })


@pytest.fixture
def db():
    d = TradeDatabase(":memory:")
    yield d
    d.close()


@pytest.fixture
def clock() -> FakeClock:
    return FakeClock()
