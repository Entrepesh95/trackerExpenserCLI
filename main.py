import argparse
import json
import os

LIST_FILE = "expenseList.json"



def load_data():
    # If the file doesn't exist yet (very first run), start empty
    if not os.path.exists(LIST_FILE):
        return []
    with open(LIST_FILE, "r") as f:
        return json.load(f)

def save_data(expense_data):
    with open(LIST_FILE, "w") as f:
        json.dump(expense_data, f, indent=2)


items = dict(category="category", description="description", amount="amount")

def main():
    expense_data = load_data()
    parser = argparse.ArgumentParser(description="A CLI - command line interface expense tracker tool")

    # subcommands used to call out the command operations
    subparsers = parser.add_subparsers(dest="command")

    # operations that calls out the command add to add items into the expense list
    add_parser = subparsers.add_parser("add", help="add items to the list")
    add_parser.add_argument('--a', '--amount', type=str, required=True, help="amount of the item")
    add_parser.add_argument('--c', '--category', type=str, required=True, help="type of the item")
    add_parser.add_argument('--d', '--description', type=str, required=True, help="description of the item")

    ## to be continue
    #operations that calls out the command show the list
    show_parser = subparsers.add_parser("show", help="show items to the list")
    show_parser.add_argument('--s', '--show', help="display the items")

    args = parser.parse_args()

    if args.command == "add":

        print(args.c + " " + args.d + " " + args.a)
        items["category"] = args.c
        items["description"] = args.d
        items["amount"] = args.a

        expense_data.append(items)
        save_data(expense_data)

        print(items)

    ## we need to be able to store the data into the dict
    elif args.command == "show":
        for item in expense_data:

            print(item)

    else:
        parser.print_help()

if __name__ == "__main__":
        main()

