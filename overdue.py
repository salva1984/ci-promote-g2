"""Minimal overdue loan helper."""

from datetime import datetime


def report_overdue(reference_date, loans=None):
    """Print and return loans whose due date is before the reference date."""
    if loans is None:
        loans = []

    if isinstance(reference_date, str):
        reference_date = datetime.strptime(reference_date, "%Y-%m-%d").date()

    overdue = []

    for loan in loans:
        due_date = loan.get("due_date")
        if not due_date:
            continue

        if isinstance(due_date, str):
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

        if due_date < reference_date:
            overdue.append(loan)

    for loan in overdue:
        print(
            f"name={loan.get('name')} object={loan.get('object_loaned')} "
            f"due_date={loan.get('due_date')}"
        )

    return overdue
