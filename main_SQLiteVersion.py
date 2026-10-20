import argparse
import sqlite3


#a function that creates a connection to the DB
def connection_database():

    # make a connection to the DB
    connection = sqlite3.connect("expensesList.db")

    # create a bridge between the connection to send and receive sql commands
    cursor = connection.cursor()

    # creates the table if it doesnt exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            category TEXT,
            description TEXT,
            amount REAL
        )
    """)
    return connection, cursor


def main():
    connection, cursor = connection_database()

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

        cursor.execute(
            "INSERT INTO expenses (category, description, amount) VALUES (?, ?, ?)",
            (args.category, args.description, args.amount)
        )

        # saving the data
        connection.commit()

    # displays the list saved from the file
    elif args.command == "show":

        # a sql command to read data back from the DB
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

        for row in rows:
            print(f"{row[0]}: {row[1]} - {row[2]} = {row[3]}")


    # displays the total amount of the items
    elif args.command == "total":

        cursor.execute("SELECT SUM(amount) FROM expenses")
        result = cursor.fetchone()
        total = result[0] if result[0] is not None else 0
        print(f" your total is: £{total}")


    else:
        parser.print_help()

    # this will close the connection to the DB
    connection.close()
if __name__ == "__main__":
    main()




