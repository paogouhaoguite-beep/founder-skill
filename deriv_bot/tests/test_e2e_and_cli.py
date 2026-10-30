import dataclasses
import json
import socket
from pathlib import Path

from derivbot.__main__ import main, parse_args
from derivbot.api import DerivClient
from derivbot.config import StrategyConfig
from derivbot.e2e import pick_signal, run_e2e
from derivbot.mock_server import DEMO_TOKEN, MockDerivServer
from derivbot.strategy import Candle, EmaCrossoverStrategy

ROOT = Path(__file__).resolve().parents[1]


async def test_e2e_succeeds_against_simulator(cfg, db):
    async with MockDerivServer() as srv:
        run_cfg = dataclasses.replace(cfg, api=srv.api_config(cfg.api))
        res = await run_e2e(run_cfg, DerivClient(run_cfg.api, DEMO_TOKEN), db,
                            duration=2, duration_unit="t", poll=0.5)
    assert res.success, res.traceback
    assert [s.name for s in res.steps] == ["connect", "market_data", "signal", "risk",
                                          "proposal", "settlement", "verify"]
    assert res.trade["status"] in ("won", "lost")
    assert not any("buy" in r for r in srv.requests)
    json.loads(res.to_json())


async def test_e2e_reports_failure_with_hint(cfg, db):
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    api = dataclasses.replace(cfg.api, endpoint=f"ws://127.0.0.1:{port}", max_retries=0)
    run_cfg = dataclasses.replace(cfg, api=api)
    res = await run_e2e(run_cfg, DerivClient(api), db, duration=1, duration_unit="t")
    assert not res.success
    assert res.failed_step == "connect" and "ConnectionLostError" in res.error
    assert "WebSocket" in res.hint and res.traceback


def test_pick_signal_falls_back_when_no_fresh_cross():
    st = EmaCrossoverStrategy(StrategyConfig(fast_period=3, slow_period=5, candle_count=20))
    closes = [10.0] * 8 + [9.0, 8.5, 8.0, 8.0, 12.0, 13.0, 14.0]
    candles = [Candle(i * 60, c, c, c, c) for i, c in enumerate(closes)]
    sig, source = pick_signal(st, candles)
    assert sig.direction.value == "CALL" and "2 candles ago" in source
    rising = [Candle(i * 60, float(i), i, i, float(i)) for i in range(1, 30)]
    sig, source = pick_signal(st, rising)
    assert sig.direction.value == "CALL" and "alignment" in source


def test_cli_parses_flags():
    a = parse_args(["--paper", "--no-dashboard", "--config", "x.yaml"])
    assert a.paper and a.no_dashboard and a.config == "x.yaml" and not a.e2e_test


def test_cli_bad_config_exit_code(tmp_path):
    bad = tmp_path / "c.yaml"
    bad.write_text("risk:\n  risk_per_trade_pct: 50\n")
    assert main(["--config", str(bad)]) == 2


def test_cli_e2e_with_mock_server_and_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    cfg_text = (ROOT / "config.yaml").read_text().replace('file: "logs/bot.log"', 'file: ""')
    (tmp_path / "config.yaml").write_text(cfg_text)
    assert main(["--e2e-test", "--mock-server", "--e2e-duration", "2",
                 "--e2e-db", "data/trades.db"]) == 0
    result = json.loads((tmp_path / "data" / "e2e_result.json").read_text())
    assert result["success"] is True
    assert main(["--report"]) == 0


def test_cli_live_without_token_refuses(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("DERIV_API_TOKEN", raising=False)
    (tmp_path / "config.yaml").write_text((ROOT / "config.yaml").read_text())
    assert main(["--no-dashboard"]) == 2


def test_cli_paper_run_with_mock_server(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "config.yaml").write_text((ROOT / "config.yaml").read_text()
                                          .replace("poll_interval: 5.0", "poll_interval: 0.01"))
    assert main(["--paper", "--mock-server", "--max-iterations", "2"]) == 0
    assert (tmp_path / "logs" / "bot.log").exists()
    assert (tmp_path / "data" / "trades.db").exists()
