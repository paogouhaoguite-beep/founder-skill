"""Configuration loading and validation (config.yaml -> typed dataclasses)."""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TypeVar, get_type_hints

import yaml


class ConfigError(ValueError):
    """Raised when config.yaml is missing, malformed or contains invalid values."""


@dataclass(frozen=True)
class ApiConfig:
    # "new": Deriv's current Options API (api.derivws.com). Login = REST one-time password.
    # "legacy": the old ws.binaryws.com / ws.derivws.com v3 API with the `authorize` call,
    # which Deriv is retiring as accounts migrate to the new platform.
    protocol: str = "new"
    endpoint: str = "wss://api.derivws.com/trading/v1/options/ws/public"
    rest_base: str = "https://api.derivws.com"
    app_id: str = ""  # new: Deriv-App-ID (required with a personal access token)
    account_type: str = "demo"  # new: which account the token's OTP is issued for
    account_id: str = ""  # new: pick a specific account (optional)
    token_env: str = "DERIV_API_TOKEN"
    request_timeout: float = 15.0
    max_retries: int = 5
    reconnect_base_delay: float = 1.0
    reconnect_max_delay: float = 30.0
    rate_limit_backoff: float = 5.0

    @property
    def url(self) -> str:
        if self.protocol == "new":
            return self.endpoint
        sep = "&" if "?" in self.endpoint else "?"
        return f"{self.endpoint}{sep}app_id={self.app_id or LEGACY_PUBLIC_APP_ID}"


@dataclass(frozen=True)
class TradingConfig:
    symbol: str = "R_100"
    currency: str = "USD"
    contract_duration: int = 5
    duration_unit: str = "m"
    poll_interval: float = 5.0
    min_payout_ratio: float = 0.75


@dataclass(frozen=True)
class StrategyConfig:
    name: str = "ema_crossover"
    fast_period: int = 9
    slow_period: int = 21
    granularity: int = 60
    candle_count: int = 100
    min_ema_gap_pct: float = 0.0


@dataclass(frozen=True)
class RiskConfig:
    risk_per_trade_pct: float = 1.0
    daily_loss_limit_pct: float = 5.0
    max_consecutive_losses: int = 3
    cooldown_minutes: float = 60.0
    min_stake: float = 0.35
    max_stake: float = 50.0
    max_trades_per_day: int = 20
    max_open_positions: int = 1
    max_critical_errors: int = 5


@dataclass(frozen=True)
class PaperConfig:
    starting_balance: float = 100.0


@dataclass(frozen=True)
class DatabaseConfig:
    path: str = "data/trades.db"


@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    file: str = "logs/bot.log"


@dataclass(frozen=True)
class SafetyConfig:
    allow_real_account: bool = False
    kill_switch_file: str = "KILL_SWITCH"
    close_positions_on_kill: bool = False


@dataclass(frozen=True)
class Config:
    api: ApiConfig = field(default_factory=ApiConfig)
    trading: TradingConfig = field(default_factory=TradingConfig)
    strategy: StrategyConfig = field(default_factory=StrategyConfig)
    risk: RiskConfig = field(default_factory=RiskConfig)
    paper: PaperConfig = field(default_factory=PaperConfig)
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    safety: SafetyConfig = field(default_factory=SafetyConfig)


LEGACY_PUBLIC_APP_ID = "1089"
MAX_RISK_PER_TRADE_PCT = 2.0
VALID_DURATION_UNITS = {"t", "s", "m", "h"}
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
SUPPORTED_STRATEGIES = {"ema_crossover"}

T = TypeVar("T")


def _coerce(section: str, key: str, value: Any, expected: Any) -> Any:
    # bool is a subclass of int, so it must be rejected explicitly for numeric fields.
    is_bool = isinstance(value, bool)
    if expected is bool and is_bool:
        return value
    if expected is int and isinstance(value, int) and not is_bool:
        return value
    if expected is float and isinstance(value, (int, float)) and not is_bool:
        return float(value)
    if expected is str and isinstance(value, str):
        return value
    if expected is str and isinstance(value, int) and not is_bool:
        return str(value)  # e.g. `app_id: 1089` written without quotes
    raise ConfigError(
        f"{section}.{key}: expected {expected.__name__}, got {type(value).__name__} ({value!r})"
    )


def _build_section(cls: type[T], section: str, raw: Any) -> T:
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise ConfigError(f"section '{section}' must be a mapping")
    hints = get_type_hints(cls)
    known = {f.name for f in dataclasses.fields(cls)}  # type: ignore[arg-type]
    unknown = set(raw) - known
    if unknown:
        raise ConfigError(f"{section}: unknown key(s) {sorted(unknown)}")
    kwargs = {k: _coerce(section, k, v, hints[k]) for k, v in raw.items()}
    return cls(**kwargs)


def _validate(cfg: Config) -> None:
    errors: list[str] = []
    a, t, s, r = cfg.api, cfg.trading, cfg.strategy, cfg.risk

    if a.protocol not in ("new", "legacy"):
        errors.append("api.protocol must be 'new' or 'legacy'")
    if not a.endpoint.startswith(("wss://", "ws://")):
        errors.append("api.endpoint must be a ws:// or wss:// URL")
    if not a.rest_base.startswith(("https://", "http://")):
        errors.append("api.rest_base must be an http(s):// URL")
    if a.account_type not in ("demo", "real"):
        errors.append("api.account_type must be 'demo' or 'real'")
    if a.request_timeout <= 0:
        errors.append("api.request_timeout must be > 0")
    if a.max_retries < 0:
        errors.append("api.max_retries must be >= 0")

    if not t.symbol:
        errors.append("trading.symbol must not be empty")
    if t.duration_unit not in VALID_DURATION_UNITS:
        errors.append(f"trading.duration_unit must be one of {sorted(VALID_DURATION_UNITS)}")
    if t.contract_duration <= 0:
        errors.append("trading.contract_duration must be > 0")
    if t.poll_interval <= 0:
        errors.append("trading.poll_interval must be > 0")
    if t.min_payout_ratio < 0:
        errors.append("trading.min_payout_ratio must be >= 0")

    if s.name not in SUPPORTED_STRATEGIES:
        errors.append(f"strategy.name must be one of {sorted(SUPPORTED_STRATEGIES)}")
    if s.fast_period < 1 or s.slow_period < 2:
        errors.append("strategy periods must be positive")
    if s.fast_period >= s.slow_period:
        errors.append("strategy.fast_period must be smaller than strategy.slow_period")
    if s.granularity <= 0:
        errors.append("strategy.granularity must be > 0")
    if s.candle_count < s.slow_period + 2:
        errors.append("strategy.candle_count must be at least slow_period + 2")
    if s.min_ema_gap_pct < 0:
        errors.append("strategy.min_ema_gap_pct must be >= 0")

    if not 0 < r.risk_per_trade_pct <= MAX_RISK_PER_TRADE_PCT:
        errors.append(f"risk.risk_per_trade_pct must be in (0, {MAX_RISK_PER_TRADE_PCT}]")
    if not 0 < r.daily_loss_limit_pct <= 100:
        errors.append("risk.daily_loss_limit_pct must be in (0, 100]")
    if r.max_consecutive_losses < 1:
        errors.append("risk.max_consecutive_losses must be >= 1")
    if r.cooldown_minutes < 0:
        errors.append("risk.cooldown_minutes must be >= 0")
    if r.min_stake <= 0 or r.max_stake < r.min_stake:
        errors.append("risk: require 0 < min_stake <= max_stake")
    if r.max_trades_per_day < 1 or r.max_open_positions < 1 or r.max_critical_errors < 1:
        errors.append("risk: max_trades_per_day, max_open_positions, max_critical_errors >= 1")

    if cfg.paper.starting_balance <= 0:
        errors.append("paper.starting_balance must be > 0")
    if cfg.logging.level.upper() not in VALID_LOG_LEVELS:
        errors.append(f"logging.level must be one of {sorted(VALID_LOG_LEVELS)}")

    if errors:
        raise ConfigError("invalid configuration:\n  - " + "\n  - ".join(errors))


SECTIONS: dict[str, type[Any]] = {
    "api": ApiConfig,
    "trading": TradingConfig,
    "strategy": StrategyConfig,
    "risk": RiskConfig,
    "paper": PaperConfig,
    "database": DatabaseConfig,
    "logging": LoggingConfig,
    "safety": SafetyConfig,
}


def config_from_dict(raw: Any) -> Config:
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise ConfigError("top level of config must be a mapping")
    unknown = set(raw) - set(SECTIONS)
    if unknown:
        raise ConfigError(f"unknown section(s) {sorted(unknown)}")
    built = {name: _build_section(cls, name, raw.get(name)) for name, cls in SECTIONS.items()}
    cfg = Config(**built)
    _validate(cfg)
    return cfg


def load_config(path: str | Path) -> Config:
    p = Path(path)
    if not p.is_file():
        raise ConfigError(f"config file not found: {p}")
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"could not parse {p}: {exc}") from exc
    return resolve_paths(config_from_dict(raw), p.resolve().parent)


def resolve_paths(cfg: Config, base: Path) -> Config:
    """Make relative file paths relative to the config file's folder, not the current
    directory, so the bot behaves the same when started from cron, a service or
    another folder (otherwise it would silently use a fresh, empty journal)."""

    def fix(path: str) -> str:
        return str(base / path) if path and not Path(path).is_absolute() else path

    return dataclasses.replace(
        cfg,
        database=dataclasses.replace(cfg.database, path=fix(cfg.database.path)),
        logging=dataclasses.replace(cfg.logging, file=fix(cfg.logging.file)),
        safety=dataclasses.replace(cfg.safety,
                                   kill_switch_file=fix(cfg.safety.kill_switch_file)),
    )
