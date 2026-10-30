"""A stand-in for Alpaca for --dry-run and the tests: no keys, no network, no
money. An entry fills at once at its plan price; the bracket legs wait (call
fill_leg to hit the stop or the target); a closing sell fills at once."""

import itertools


class SimBroker(object):
    def __init__(self, cash=100000.0, is_open=True, equity=None, last_equity=None, fill_price=None):
        self.cash = cash
        self.is_open = is_open
        self.equity = equity if equity is not None else cash
        self.last_equity = last_equity if last_equity is not None else cash
        self.fill_price = fill_price  # {symbol: price}; default: the stop/target midpoint
        self.orders = {}
        self.positions = {}
        self.placed = []
        self._ids = itertools.count(1)

    def _id(self):
        return "sim-%d" % next(self._ids)

    def account(self):
        return {"status": "ACTIVE", "trading_blocked": False, "cash": str(self.cash),
                "equity": str(self.equity), "last_equity": str(self.last_equity)}

    def clock(self):
        return {"is_open": self.is_open, "next_open": "the next session"}

    def place(self, tool_input, client_order_id=None):
        t = dict(tool_input)
        sym, qty = t["symbol"], t["qty"]
        price = (self.fill_price or {}).get(sym)
        if price is None:
            price = round((float(t["take_profit_limit_price"]) + float(t["stop_loss_stop_price"])) / 2, 2)
        oid = self._id()
        legs = [{"id": self._id(), "type": "limit", "side": "sell", "status": "held", "qty": qty,
                 "limit_price": t["take_profit_limit_price"]},
                {"id": self._id(), "type": "stop", "side": "sell", "status": "held", "qty": qty,
                 "stop_price": t["stop_loss_stop_price"]}]
        o = {"id": oid, "client_order_id": client_order_id, "symbol": sym, "side": t["side"], "qty": qty,
             "status": "filled", "filled_qty": qty, "filled_avg_price": str(price), "legs": legs}
        for leg in legs:
            leg["status"] = "new"
        self.orders[oid] = o
        self.positions[sym] = {"symbol": sym, "qty": qty}
        self.placed.append((t, client_order_id))
        return {"id": oid, "status": "accepted"}

    def order(self, order_id):
        for o in self.orders.values():
            if o["id"] == order_id:
                return o
        raise KeyError(order_id)

    def fill_leg(self, symbol, kind):
        """kind: 'limit' (the target) or 'stop'."""
        for o in self.orders.values():
            if o["symbol"] == symbol:
                for leg in o.get("legs") or []:
                    if leg["type"] == kind and leg["status"] == "new":
                        price = leg.get("limit_price") or leg.get("stop_price")
                        leg.update(status="filled", filled_qty=leg["qty"], filled_avg_price=price)
                        for other in o["legs"]:
                            if other is not leg:
                                other["status"] = "canceled"
                        self.positions.pop(symbol, None)
                        return leg

    def open_orders(self, symbol):
        return [leg for o in self.orders.values() if o["symbol"] == symbol
                for leg in o.get("legs") or [] if leg["status"] == "new"]

    def cancel(self, order_id):
        for o in self.orders.values():
            for leg in o.get("legs") or []:
                if leg["id"] == order_id:
                    leg["status"] = "canceled"

    def position(self, symbol):
        return self.positions.get(symbol)

    def close_position(self, symbol):
        pos = self.positions.pop(symbol)
        entry = next(o for o in self.orders.values() if o["symbol"] == symbol and o.get("legs"))
        oid = self._id()
        self.orders[oid] = {"id": oid, "symbol": symbol, "side": "sell", "qty": pos["qty"], "status": "filled",
                            "filled_qty": pos["qty"], "filled_avg_price": entry["filled_avg_price"]}
        return {"id": oid}
