#A expense Tracker CLI 

this is a command line tool for tracking personal expenses built in python.
you can add expenses in an organise section that includes, categories, amount, description and the total spent.
this data is saved in a local file so the data stays persistant between runs.

## Features
- add an expense with a category, a description and an amount
- view all the expenses
- view all the total spent
- data is saved locally in a JSON file

## Tech stack used
- python 3
- argparse to use the command line
- JSON - for storing the data

## Installation

- you can use the git clone https://github.com/Entrepesh95/trackerExpenserCLI.git
- cd into the folder /trackerExpenserCLI
- then open it with your current IDE (pycharm, VSCode, Eclipse, etc)
- no external dependencies were used in this project

## Usage

1. open the terminal
2. to add items into the list you must enter the file name and then the command: python main.py show  
3. to add an item write: python main.py add --amount 12.50 --category food --description “lunch
4. to show the items write: python main.py show 
4. to display the total write: python main.py total


# V2 Expense tracker CLI with SQLite

another version of the expense tracker was added, in a separate file using SQLite instead of JSON

the main reason for changing from JSON to SQLite if because, if the data grows over more than 50 to 100 lines,
then more python code needs to be written in order to obtain a result, a sum, requires filtering, but with SQL it
can be done with one single query.

## New Features
- data is now saved in a sqlite file.

## New tech replaced
- JSON was removed and SQLite was introduced.


      

