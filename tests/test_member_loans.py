import pytest

from features.member_loans import member_loans


def fresh_data():
    return {
        "books": [
            {"id": "B001", "title": "Book One"},
            {"id": "B002", "title": "Book Two"},
        ],
        "members": [
            {"id": "M001", "name": "Ada"},
            {"id": "M002", "name": "Linus"},
        ],
        "loans": [
            {"book_id": "B001", "member_id": "M001", "due_date": "2026-06-10"},
        ],
    }


def test_lists_held_books():
    data = fresh_data()
    books = member_loans(data, "M001")
    assert books == [{"id": "B001", "title": "Book One"}]


def test_member_with_no_loans_returns_empty():
    data = fresh_data()
    assert member_loans(data, "M002") == []


def test_unknown_member_raises():
    data = fresh_data()
    with pytest.raises(ValueError):
        member_loans(data, "M999")
