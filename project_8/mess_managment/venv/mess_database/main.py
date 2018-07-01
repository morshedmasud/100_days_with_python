from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from datetime import datetime
import logging
import sys

# Global Variable
SQLITE = 'sqlite'

# Table names
COST = "cost_list"



class MessCost:

    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    db_engine = None

    def __init__(self, dbtype, date='', cost='', comment=''):

    def add_cost(self):
        print("__________Added Options__________\n")
        date = datetime.today()
        date = date.date()
        name = input("Type your name: ")
        cost = input("Enter today cost: ")
        purpose = input("Type comments: ")
        if not name or not cost:
            print("You should fulfill both name and cost")
            logging.WARNING("You should fulfill name and cost field")

            sys.exit(0)
        data = [str(date), name, cost, purpose]
        try:
            with open("csv_file/data.csv", "a") as f:
                f = csv.writer(f)
                f.writerow(data)
            print("Added successfully.....\n")
        except Exception as e:
            print("something wrong!!\n")
            logging.ERROR(e)

        print("try again....any option")
        option = int(input("Enter your option: "))
        cls.call_function(option)

    def show_database(self):
        print("___________Showing Database___________\n")
        with open("csv_file/data.csv", 'r') as f:
            r = csv.reader(f)
            for i, row in enumerate(r):
                print(row)
            print()
            print("try again....any option")
            option = int(input("Enter your option: "))
            cls.call_function(option)

    def total_cost_for_each(self):
        print("___________Calculate Cost___________\n")
        total_cost = 0
        person = int(input("How many people living together: "))
        with open("csv_file/data.csv", 'r') as f:
            csv_reader = csv.reader(f)
            for i, row in enumerate(csv_reader):
                if i > 0:
                    total_cost += int(row[2])
        print("Total cost: ", total_cost)
        print("Total cost for each person: %d Taka\n" % (total_cost/person))
        print("try again....any option")
        option = int(input("Enter your option: "))
        cls.call_function(option)

    def exit(self):
        print("Thanks for using this application.")
        sys.exit(0)

    def call_function(self, option):
        print("""
        1: Add Cost.
        2: Show Database.
        3: Total Cost for Each Person.
        4: Close Program.
        """)

        if option == 1:
            cls.add_cost()
        elif option == 2:
            cls.show_database()
        elif option == 3:
            cls.total_cost_for_each()
        elif option == 4:
            cls.exit()
        else:
            print("You choice wrong option!!!\n")
            print("try again....")
            option = int(input("Enter your option: "))
            cls.call_function(option)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename='log_info/error.log', level=logging.DEBUG)

    dbms = MessCost()

    option = int(input("Enter your option: "))
    cls = MessCost()
    cls.call_function(option)






