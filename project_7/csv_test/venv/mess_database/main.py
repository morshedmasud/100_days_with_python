import log
from datetime import datetime
import csv
import sys


class MessCost:
    # def __init__(self, option):
    #     self.option = option

    def add_cost(self):
        print("__________Added Options__________\n")
        date = datetime.today()
        date = date.date()
        name = input("Type your name: ")
        cost = input("Enter today cost: ")
        purpose = input("Type comments: ")
        if not name or not cost:
            print("You should fulfill both name and cost")
            log.error("You should fulfill name and cost field")

            sys.exit(0)
        data = [str(date), name, cost, purpose]
        try:
            with open("csv_file/data.csv", "a") as f:
                f = csv.writer(f)
                f.writerow(data)
            print("Added successfully.....\n")
        except Exception as e:
            print("something wrong!!\n")
            log.report(str(e))

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
    print("""
1: Add Cost.
2: Show Database.
3: Total Cost for Each Person.
4: Close Program.
""")

    # field_name = ['Date', 'Name', 'Cost', 'Purpose']
    # with open("csv_file/data.csv", "w") as f:
    #     csv_writer = csv.writer(f, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    #     csv_writer.writerow(field_name)
    option = int(input("Enter your option: "))
    cls = MessCost()
    cls.call_function(option)

    # option = int(input("Enter your option: "))
    # if option == 1:
    #     cls.add_cost()
    # elif option == 2:
    #     cls.show_database()
    # elif option == 3:
    #     cls.total_cost_for_each()
    # elif option == 4:
    #     cls.exit()
    # else:
    #     print("You choice wrong option!!!")
    #     print("try again....")
    #     option = int(input("Enter your option: "))







