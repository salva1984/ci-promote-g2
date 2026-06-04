import pytest

from features.return_book import return_book

def data_with_loan():
    return {
        "books": [{"id": "B001", "title": "Book One"}],
        "members": [{"id": "M001", "name": "Ada"}],
        "loans": [{"book_id": "B001", "member_id": "M001", "due_date": "2026-06-10"}],
    }

def test_return_removes_loan():
    data = data_with_loan()
    loan = return_book(data, "B001")
    assert loan["book_id"] == "B001"
    assert data["loans"] == []

def test_return_book_not_on_loan_raises():
    data = data_with_loan()
    with pytest.raises(ValueError):
        return_book(data, "B002")

def test_return_twice_raises():
    data = data_with_loan()
    return_book(data, "B001")
    with pytest.raises(ValueError):
        return_book(data, "B001")
