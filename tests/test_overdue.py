from datetime import date
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from features.overdue_loans import overdue_loans


def fresh_data():
    return {
        "books": [
            {"id": "B001", "title": "Book One"},
            {"id": "B002", "title": "Book Two"},
        ],
        "members": [
            {"id": "M001", "name": "Ada"},
            {"id": "M002", "name": "Grace"},
        ],
        "loans": [
            {"book_id": "B001", "member_id": "M001", "due_date": "2026-06-01"},
            {"book_id": "B002", "member_id": "M002", "due_date": "2026-06-03"},
            {"book_id": "B002", "member_id": "M001", "due_date": "2026-06-10"},
        ],
    }


def test_overdue_loans_returns_only_past_due_items():
    data = fresh_data()

    result = overdue_loans(data, today=date(2026, 6, 3))

    assert result == [
        {
            "book_id": "B001",
            "title": "Book One",
            "member_id": "M001",
            "member_name": "Ada",
            "due_date": "2026-06-01",
        }
    ]


def test_overdue_loans_returns_empty_when_nothing_is_overdue():
    data = fresh_data()

    result = overdue_loans(data, today=date(2026, 6, 1))

    assert result == []