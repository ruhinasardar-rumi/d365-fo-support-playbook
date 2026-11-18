"""Summarise a support ticket log: volume, resolution time, and recurring root causes.
Usage: python ticket_analysis.py data/sample_tickets.csv
"""
import csv
import sys
from collections import Counter
from datetime import date


def days_open(row):
    opened = date.fromisoformat(row["opened"])
    closed = date.fromisoformat(row["closed"])
    return (closed - opened).days


def main(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Total tickets: {len(rows)}")
    avg = sum(days_open(r) for r in rows) / len(rows)
    print(f"Average days to resolve: {avg:.1f}\n")

    print("Tickets by module:")
    for module, n in Counter(r["module"] for r in rows).most_common():
        print(f"  {module}: {n}")

    print("\nRecurring root causes (2+ tickets):")
    causes = Counter(r["root_cause"] for r in rows)
    for cause, n in causes.most_common():
        if n >= 2:
            print(f"  {cause}: {n}  -> candidate for a runbook, validation or user tip")

    print("\nAverage days to resolve by category:")
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(days_open(r))
    for cat, vals in sorted(by_cat.items()):
        print(f"  {cat}: {sum(vals) / len(vals):.1f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python ticket_analysis.py <tickets.csv>")
    main(sys.argv[1])
