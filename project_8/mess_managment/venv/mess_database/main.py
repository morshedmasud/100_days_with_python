import sqlite3
from datetime import datetime
import logging
import sys


class MessCost:

    def add_cost(self):
        print("__________Added Options__________\n")
        date = datetime.today()
        date = str(date.today().strftime("%m/%d/%Y %I:%M:%S %P"))
        name = input("Type your name: ").capitalize()
        cost = input("Enter today cost: ")
        purpose = input("Type comments: ").capitalize()
        if not name or not cost:
            print("\nYou should fulfill both name and cost field.")
            logging.warning("You should fulfill name and cost field")
            print("\ntry again...\n")
            self.call_function()

        try:
            data = "INSERT INTO CostSheet VALUES ('{0}', '{1}', {2}, '{3}')".format(str(date), name, cost, purpose)
            self.execute_query(data)
            logging.info(data)
            print("\nAdded successfully.....\n")
        except Exception as e:
            print("\nsomething wrong!!\n")
            logging.error(str(e))

        print("try again....any option")
        self.call_function()

    def show_database(self):
        print("___________Showing Database___________\n")
        data = "SELECT * FROM CostSheet"
        conn = sqlite3.connect("database/CostSheet.db")
        dbms = conn.cursor()
        result = dbms.execute(data)
        for i in result:
            print(*i, sep='   ')
        conn.commit()
        result.close()
        print("\ntry again....\n")
        self.call_function()

    def total_cost_for_each(self):
        print("___________Calculate Cost___________\n")
        total_cost = 0
        person = int(input("How many people living together: "))

        data = "SELECT Cost FROM CostSheet"
        conn = sqlite3.connect("database/CostSheet.db")
        dbms = conn.cursor()
        result = dbms.execute(data)
        for i in result:
            total_cost += int(i[0])
        conn.commit()
        result.close()
        print("Total cost: ", total_cost)
        print("Total cost for each person: %0.2f Taka.\n" % (total_cost/person))
        logging.info("Showing cost for each person.")
        print("\ntry again....\n")
        self.call_function()

    def exit(self):
        print("Thanks for using this application.")
        sys.exit(0)

    def execute_query(self, data):
        conn = sqlite3.connect("database/CostSheet.db")

        dbms = conn.cursor()
        dbms.execute(data)

        conn.commit()
        conn.close()

    def create_database(self):
        try:
            conn = sqlite3.connect("database/CostSheet.db")
            dbms = conn.cursor()
            dbms.execute('''CREATE TABLE CostSheet(Date text, Name text, Cost real, Purpose text)''')
            conn.commit()
            conn.close()
            print("Database created")
        except Exception as e:
            logging.exception(e)

    def call_function(self):
        print("........Welcome to Mess Management system..........")
        print("""
        1: Add Cost.
        2: Show Database.
        3: Total Cost for Each Person.
        4: Close Program.
        """)

        option = int(input("Enter your options: "))
        if option == 1:
            self.add_cost()
        elif option == 2:
            self.show_database()
        elif option == 3:
            self.total_cost_for_each()
        elif option == 4:
            self.exit()
        else:
            print("\nYou choice wrong option!!!\n")
            print("try again....")
            self.call_function()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %P', filename='log_info/error.log', level=logging.DEBUG)

    cls = MessCost()
    # cls.create_database()
    cls.call_function()






