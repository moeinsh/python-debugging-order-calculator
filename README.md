# Debugging: Order Total Calculator (Python) — sample project

Diagnosed and fixed a script (`broken.py`) that crashed with
`ValueError: invalid literal for int()` on real-world dirty CSV data.

## The fix (`fixed.py`)

- **Safe numeric parsing** — bad rows are skipped AND logged with line numbers
- Word-form quantities ("two") and missing prices handled gracefully
- Clear warning log so bad source data can be fixed upstream

## Result

The exact input file that crashed (`orders.csv`) now produces the correct
total (**43.98**) with zero data loss — and every skipped row is reported.

```bash
python fixed.py
```

This is a demonstration sample showing my debugging approach.
No client, no fake data.
