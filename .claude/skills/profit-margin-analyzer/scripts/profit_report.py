#!/usr/bin/env python3
"""Calculate a transparent contribution waterfall from an explicit merchant CSV."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ("orders", "net_merchandise_revenue", "retained_shipping_revenue", "landed_cogs", "payment_platform_fees", "fulfillment_shipping", "attributable_return_costs", "ad_spend")

def report(path):
    rows = []
    with Path(path).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        required = {"sku", "currency", "period", *FIELDS}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Missing required columns: " + ", ".join(sorted(required - set(reader.fieldnames or []))))
        identities = set()
        for line, row in enumerate(reader, 2):
            if not all((row.get(k) or "").strip() for k in required):
                raise ValueError(f"Row {line}: missing values are unknown, not zero")
            identity = tuple(row[k] for k in ("sku", "currency", "period"))
            if identity in identities:
                raise ValueError(f"Row {line}: duplicate SKU/currency/period")
            identities.add(identity)
            try:
                values = {key: Decimal(row[key]) for key in FIELDS}
            except InvalidOperation as exc:
                raise ValueError(f"Row {line}: invalid numeric input") from exc
            if any(not v.is_finite() or v < 0 for v in values.values()):
                raise ValueError(f"Row {line}: use finite non-negative amounts; reconcile negative adjustments separately")
            orders = values["orders"]
            if orders <= 0 or orders != orders.to_integral_value():
                raise ValueError(f"Row {line}: orders must be a positive integer")
            revenue = values["net_merchandise_revenue"] + values["retained_shipping_revenue"]
            non_ad_costs = sum(values[k] for k in ("landed_cogs", "payment_platform_fees", "fulfillment_shipping", "attributable_return_costs"))
            pre_ad = revenue - non_ad_costs
            post_ad = pre_ad - values["ad_spend"]
            money = lambda value: str(value.quantize(Decimal("0.01")))
            rows.append({"sku": row["sku"], "currency": row["currency"], "period": row["period"], "orders": int(orders), "net_revenue_including_retained_shipping": money(revenue), "non_ad_variable_costs": money(non_ad_costs), "pre_ad_contribution": money(pre_ad), "post_ad_contribution": money(post_ad), "pre_ad_contribution_per_order": money(pre_ad / orders), "ad_spend_per_order": money(values["ad_spend"] / orders)})
    if not rows:
        raise ValueError("CSV has no data rows")
    return {"rows": rows, "interpretation": "Pre-ad contribution per order is a first-order break-even CPA ceiling only when the order population matches acquired orders. This is contribution, not net profit or observed lifetime value. Fixed overhead is excluded."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", nargs="?", help="Merchant CSV; omit when using --demo")
    parser.add_argument("--demo", action="store_true", help="Use the bundled synthetic sample")
    args = parser.parse_args()
    if args.demo == bool(args.csv_file):
        parser.error("Provide either a CSV path or --demo")
    source = Path(__file__).resolve().parents[1] / "assets" / "orders.csv" if args.demo else args.csv_file
    try:
        print(json.dumps(report(source), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Input error: {exc}\n")
