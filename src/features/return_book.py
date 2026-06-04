def return_book(data, book_id):
    for loan in data["loans"]:
        if loan["book_id"] == book_id:
            data["loans"].remove(loan)
            return loan

    raise ValueError(f"Book '{book_id}' is not on loan.")
