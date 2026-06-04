from storage import find_by_id

MAX_BOOKS_PER_MEMBER = 3


def _is_on_loan(data, book_id):
    return any(loan["book_id"] == book_id for loan in data["loans"])


def _count_member_loans(data, member_id):
    return sum(1 for loan in data["loans"] if loan["member_id"] == member_id)


def loan_book(data, book_id, member_id, due_date):
    
    if find_by_id(data["books"], book_id) is None:
        raise ValueError(f"Book '{book_id}' does not exist.")
    if find_by_id(data["members"], member_id) is None:
        raise ValueError(f"Member '{member_id}' does not exist.")
    if _is_on_loan(data, book_id):
        raise ValueError(f"Book '{book_id}' is already on loan.")
    if _count_member_loans(data, member_id) >= MAX_BOOKS_PER_MEMBER:
        raise ValueError(
            f"Member '{member_id}' already holds {MAX_BOOKS_PER_MEMBER} books."
        )

    loan = {"book_id": book_id, "member_id": member_id, "due_date": due_date}
    data["loans"].append(loan)
    return loan