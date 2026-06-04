from datetime import date

from storage import find_by_id


def overdue_loans(data, today=None):
    """Return the loans whose due date is in the past.

    Args:
        data: the library state dict.
        today: a datetime.date used as "now". Defaults to the system date.

    Returns:
        A list of dicts, one per overdue loan, each with the book title and
        member name attached for display:
        {"book_id", "title", "member_id", "member_name", "due_date"}.
    """
    if today is None:
        today = date.today()

    overdue = []
    for loan in data["loans"]:
        due = date.fromisoformat(loan["due_date"])
        if due < today:
            book = find_by_id(data["books"], loan["book_id"])
            member = find_by_id(data["members"], loan["member_id"])
            overdue.append(
                {
                    "book_id": loan["book_id"],
                    "title": book["title"] if book else "(unknown)",
                    "member_id": loan["member_id"],
                    "member_name": member["name"] if member else "(unknown)",
                    "due_date": loan["due_date"],
                }
            )
    return overdue