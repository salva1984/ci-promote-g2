from features.loan_book import loan_book
from features.member_loans import member_loans
from features.overdue import overdue_loans
from features.register_member import register_member
from features.return_book import return_book
from storage import load_data, save_data

def show_catalogue(data):
    on_loan = {loan["book_id"] for loan in data["loans"]}
    print("\nCatalogue:")
    for book in data["books"]:
        state = "on loan" if book["id"] in on_loan else "available"
        print(f"  {book['id']}  {book['title']}  [{state}]")


def do_register(data):
    member_id = input("New member id: ")
    name = input("Member name: ")
    member = register_member(data, member_id, name)
    save_data(data)
    print(f"Registered {member['name']} ({member['id']}).")


def do_loan(data):
    show_catalogue(data)
    book_id = input("Book id to loan: ")
    member_id = input("Member id: ")
    due_date = input("Due date (yyyy-mm-dd): ")
    loan_book(data, book_id, member_id, due_date)
    save_data(data)
    print(f"Loaned {book_id} to {member_id}, due {due_date}.")


def do_return(data):
    book_id = input("Book id to return: ")
    return_book(data, book_id)
    save_data(data)
    print(f"Returned {book_id}.")


def do_member_loans(data):
    member_id = input("Member id: ")
    books = member_loans(data, member_id)
    if not books:
        print("This member holds no books.")
    else:
        print(f"Books held by {member_id}:")
        for book in books:
            print(f"  {book['id']}  {book['title']}")


def do_overdue(data):
    overdue = overdue_loans(data)
    if not overdue:
        print("No overdue loans.")
    else:
        print("Overdue loans:")
        for loan in overdue:
            print(
                f"  {loan['book_id']} '{loan['title']}' — "
                f"{loan['member_name']} ({loan['member_id']}), "
                f"due {loan['due_date']}"
            )

ACTIONS = {
    "1": ("Register a member", do_register),
    "2": ("Loan a book", do_loan),
    "3": ("Return a book", do_return),
    "4": ("List a member's loans", do_member_loans),
    "5": ("Report overdue loans", do_overdue),
}
def main():
    while True:
        print("\n=== CaféLibro — Library Loan Manager ===")
        for key, (label, _) in ACTIONS.items():
            print(f"  {key}. {label}")
        print("  0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye.")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Unknown option.")
            continue

        data = load_data()
        try:
            action[1](data)
        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
