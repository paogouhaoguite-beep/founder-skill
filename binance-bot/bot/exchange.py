"""Pieces shared by every exchange connection."""

from decimal import ROUND_DOWN, Decimal

# 4xx answers that mean "try again later", not "this order was refused / does not exist"
RETRY_LATER = {408, 418, 429}


class ExchangeError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status


def refused(e):
    """True only when the exchange definitely refused the request (a 4xx that is
    not a rate limit). Outages, rate limits and unknown failures return False."""
    return (isinstance(e, ExchangeError) and e.status is not None
            and 400 <= e.status < 500 and e.status not in RETRY_LATER)


def floor_to_step(value, step):
    step_d = Decimal(str(step))
    if step_d <= 0:
        return Decimal(str(value))
    return (Decimal(str(value)) / step_d).to_integral_value(rounding=ROUND_DOWN) * step_d


def fmt(d):
    s = format(Decimal(d).normalize(), "f")
    return s if s not in ("-0", "") else "0"
