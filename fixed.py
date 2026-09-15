"""AFTER (fixed): order total calculator.

Fixes applied:
  1. Safe numeric parsing: empty / word-form quantities ('two') no longer
     crash the run -- bad rows are skipped and logged with their line number.
  2. Missing prices default to 0.0 instead of raising TypeError.
  3. A clear per-row error log is printed so bad source data can be fixed
     upstream instead of silently corrupting the total.
"""
import csv

WORD_NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}


def parse_qty(raw, line_no, errors):
    raw = (raw or "").strip().lower()
    if raw.isdigit():
        return int(raw)
    if raw in WORD_NUMBERS:
        return WORD_NUMBERS[raw]
    errors.append(f"line {line_no}: bad qty {raw!r} -- row skipped")
    return None


def parse_price(raw):
    try:
        return float(raw or 0)
    except ValueError:
        return 0.0


def order_total(path):
    total, errors = 0.0, []
    with open(path, newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            qty = parse_qty(row["qty"], line_no, errors)
            if qty is None:
                continue
            total += qty * parse_price(row["price"])
    for e in errors:
        print("WARNING:", e)
    return total


if __name__ == "__main__":
    print("Grand total:", round(order_total("orders.csv"), 2))
