"""Tests for the overdue loan helper."""

from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from overdue import report_overdue


def test_report_overdue_returns_only_overdue_loans():
    """It returns only loans that are past the reference date."""
    loans = [
        {"name": "Ana", "object_loaned": "Libro A", "due_date": "2026-06-01"},
        {"name": "Luis", "object_loaned": "Libro B", "due_date": "2026-06-10"},
    ]

    overdue = report_overdue("2026-06-03", loans)

    assert len(overdue) == 1
    assert overdue[0]["name"] == "Ana"
    assert overdue[0]["object_loaned"] == "Libro A"
