from pathlib import Path

import pytest

from derivbot.config import ConfigError, config_from_dict, load_config

ROOT = Path(__file__).resolve().parents[1]


def test_shipped_config_yaml_is_valid():
    cfg = load_config(ROOT / "config.yaml")
    assert cfg.trading.symbol == "R_100"
    assert cfg.strategy.fast_period == 9 and cfg.strategy.slow_period == 21
    assert 1.0 <= cfg.risk.risk_per_trade_pct <= 2.0
    assert cfg.safety.allow_real_account is False
    assert cfg.api.url.endswith("?app_id=1089")


def test_defaults_when_empty():
    cfg = config_from_dict({})
    assert cfg.risk.daily_loss_limit_pct == 5.0
    assert cfg.paper.starting_balance == 100.0


def test_int_is_accepted_for_float_fields():
    cfg = config_from_dict({"risk": {"risk_per_trade_pct": 2}})
    assert cfg.risk.risk_per_trade_pct == 2.0
    assert isinstance(cfg.risk.risk_per_trade_pct, float)


@pytest.mark.parametrize("raw, message", [
    ({"risk": {"risk_per_trade_pct": 5}}, "risk_per_trade_pct"),
    ({"risk": {"risk_per_trade_pct": 0}}, "risk_per_trade_pct"),
    ({"strategy": {"fast_period": 21, "slow_period": 9}}, "fast_period"),
    ({"trading": {"duration_unit": "d"}}, "duration_unit"),
    ({"risk": {"min_stake": 10, "max_stake": 5}}, "min_stake"),
    ({"api": {"endpoint": "http://example.com"}}, "endpoint"),
    ({"strategy": {"candle_count": 10}}, "candle_count"),
    ({"logging": {"level": "LOUD"}}, "logging.level"),
    ({"paper": {"starting_balance": -1}}, "starting_balance"),
])
def test_invalid_values_rejected(raw, message):
    with pytest.raises(ConfigError, match=message):
        config_from_dict(raw)


@pytest.mark.parametrize("raw, message", [
    ({"risk": {"max_consecutive_losses": "three"}}, "expected int"),
    ({"risk": {"max_consecutive_losses": True}}, "expected int"),
    ({"safety": {"allow_real_account": "yes"}}, "expected bool"),
    ({"risk": {"bogus": 1}}, "unknown key"),
    ({"bogus_section": {}}, "unknown section"),
    ({"risk": [1, 2]}, "must be a mapping"),
    ([1, 2], "top level"),
])
def test_type_and_structure_errors(raw, message):
    with pytest.raises(ConfigError, match=message):
        config_from_dict(raw)


def test_load_missing_file(tmp_path):
    with pytest.raises(ConfigError, match="not found"):
        load_config(tmp_path / "nope.yaml")


def test_load_malformed_yaml(tmp_path):
    p = tmp_path / "bad.yaml"
    p.write_text("risk: [unclosed\n")
    with pytest.raises(ConfigError, match="could not parse"):
        load_config(p)


def test_token_never_in_config():
    text = (ROOT / "config.yaml").read_text()
    assert "token_env" in text
    assert "a1-" not in text  # Deriv tokens look like a1-xxxx; none must be committed
