from storage import find_by_id


def member_loans(data, member_id):
    
    if find_by_id(data["members"], member_id) is None:
        raise ValueError(f"Member '{member_id}' does not exist.")

    held = []
    for loan in data["loans"]:
        if loan["member_id"] == member_id:
            book = find_by_id(data["books"], loan["book_id"])
            if book is not None:
                held.append(book)
    return held
