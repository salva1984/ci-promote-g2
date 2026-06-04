from datetime import date
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from features.overdue import overdue_loans


def fresh_data():
    return {
        "books": [
            {"id": "B001", "title": "Book One"},
            {"id": "B002", "title": "Book Two"},
        ],
        "members": [{"id": "M001", "name": "Ada"}],
        "loans": [
            {"book_id": "B001", "member_id": "M001", "due_date": "2026-06-01"},
            {"book_id": "B002", "member_id": "M001", "due_date": "2026-06-20"},
        ],
    }


def test_returns_only_past_due_loans():
    data = fresh_data()
    overdue = overdue_loans(data, today=date(2026, 6, 10))
    assert len(overdue) == 1
    assert overdue[0]["book_id"] == "B001"
    assert overdue[0]["title"] == "Book One"
    assert overdue[0]["member_name"] == "Ada"


def test_due_today_is_not_overdue():
    data = fresh_data()
    overdue = overdue_loans(data, today=date(2026, 6, 1))
    assert overdue == []


def test_nothing_overdue_returns_empty():
    data = fresh_data()
    overdue = overdue_loans(data, today=date(2026, 5, 1))
    assert overdue == []