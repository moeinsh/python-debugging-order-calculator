"""BEFORE (buggy): order total calculator.

Bug: crashes with ValueError on rows where quantity is empty or
written as words ('two'), and with TypeError when price is missing.
"""
import csv

def order_total(path):
    total = 0.0
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            qty = int(row["qty"])            # crashes on '' / 'two'
            price = float(row["price"])      # crashes on ''
            total += qty * price
    return total

if __name__ == "__main__":
    print("Grand total:", order_total("orders.csv"))
