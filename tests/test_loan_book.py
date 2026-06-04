import pytest

from features.loan_book import loan_book


def fresh_data():
    return {
        "books": [
            {"id": "B001", "title": "Book One"},
            {"id": "B002", "title": "Book Two"},
            {"id": "B003", "title": "Book Three"},
            {"id": "B004", "title": "Book Four"},
        ],
        "members": [
            {"id": "M001", "name": "Ada"},
            {"id": "M002", "name": "Linus"},
        ],
        "loans": [],
    }


def test_loan_adds_loan():
    data = fresh_data()
    loan = loan_book(data, "B001", "M001", "2026-06-10")
    assert loan == {"book_id": "B001", "member_id": "M001", "due_date": "2026-06-10"}
    assert data["loans"] == [loan]


def test_unknown_book_raises():
    data = fresh_data()
    with pytest.raises(ValueError):
        loan_book(data, "B999", "M001", "2026-06-10")


def test_unknown_member_raises():
    data = fresh_data()
    with pytest.raises(ValueError):
        loan_book(data, "B001", "M999", "2026-06-10")


def test_already_on_loan_raises():
    data = fresh_data()
    loan_book(data, "B001", "M001", "2026-06-10")
    with pytest.raises(ValueError):
        loan_book(data, "B001", "M002", "2026-06-10")


def test_fourth_loan_for_member_raises():
    data = fresh_data()
    loan_book(data, "B001", "M001", "2026-06-10")
    loan_book(data, "B002", "M001", "2026-06-10")
    loan_book(data, "B003", "M001", "2026-06-10")
    with pytest.raises(ValueError):
        loan_book(data, "B004", "M001", "2026-06-10")