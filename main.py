import argparse
import json
import os

LIST_FILE = "expenseList.json"


# a function to load data
def load_data():
    # If the file doesn't exist yet (very first run), start empty
    if not os.path.exists(LIST_FILE):
        return []
    try:
        with open(LIST_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error while reading file")
        return []

# a function to save data
def save_data(expense_data):
    with open(LIST_FILE, "w") as f:
        json.dump(expense_data, f, indent=2)



def main():
    expense_data = load_data()
    parser = argparse.ArgumentParser(description="A CLI - command line interface expense tracker tool")

    # subcommands used to call out the command operations
    subparsers = parser.add_subparsers(dest="command")

    # operations that calls out the command add to add items into the expense list
    add_parser = subparsers.add_parser("add", help="add items to the list")
    add_parser.add_argument('-a', '--amount', type=float, required=True, help="amount of the item")
    add_parser.add_argument('-c', '--category', type=str, required=True, help="type of the item")
    add_parser.add_argument('-d', '--description', type=str, required=True, help="description of the item")


    #operations that calls out the command show the list
    show_parser = subparsers.add_parser("show", help="show items to the list")

    #operation to call the total in command
    total_parser = subparsers.add_parser("total", help="show the total amount of the items")


    args = parser.parse_args()

    # add items into the file and saves it as a dictionary
    if args.command == "add":

        expenseDict = {
            "category": args.category,
            "description": args.description,
            "amount": args.amount,
        }
        expense_data.append(expenseDict)
        save_data(expense_data)
        print(f"You added: {expenseDict['category']} - {expenseDict['description']} - {expenseDict['amount']}")

    # displays the list saved from the file
    elif args.command == "show":
        for expenseItem in expense_data:

            print(f"{expenseItem['category']}: {expenseItem['description']} = £{expenseItem['amount']}")

    # displays the total amount of the items
    elif args.command == "total":
        total = 0
        for amountItem in expense_data:
            total += float(amountItem["amount"])
        print(f"You total: £{total}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

