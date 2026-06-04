from storage import load_data

ACTIONS = {}

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
