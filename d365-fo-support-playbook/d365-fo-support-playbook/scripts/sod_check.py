"""Flag users who hold conflicting roles (segregation of duties).
Usage: python sod_check.py data/sample_role_assignments.csv data/sod_rules.csv
"""
import csv
import sys
from collections import defaultdict


def main(assignments_path, rules_path):
    roles = defaultdict(set)
    with open(assignments_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            roles[row["user"]].add(row["role"])

    with open(rules_path, newline="", encoding="utf-8") as f:
        rules = list(csv.DictReader(f))

    found = 0
    for user, user_roles in sorted(roles.items()):
        for rule in rules:
            if rule["role_a"] in user_roles and rule["role_b"] in user_roles:
                found += 1
                print(f"CONFLICT: {user} holds '{rule['role_a']}' and '{rule['role_b']}' - {rule['reason']}")
    if not found:
        print("No conflicts found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python sod_check.py <assignments.csv> <rules.csv>")
    main(sys.argv[1], sys.argv[2])
