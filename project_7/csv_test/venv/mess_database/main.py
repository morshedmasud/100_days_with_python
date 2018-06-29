import log
from datetime import datetime
import csv
import sys


class MessCost:

    def add_cost(self):
        print("          Added Options         ")
        date = datetime.today()
        date = date.date()
        name = input("Type your name: ")
        cost = input("Enter today cost: ")
        if not name or not cost:
            print("You should fulfill both name and cost")
            log.error("You should fulfill name and cost field")
            sys.exit(0)
        data = [str(date), name, cost]
        try:
            with open("csv_file/data.csv", "a") as f:
                f = csv.writer(f)
                f.writerow(data)
            print("Added successfully.....")
        except Exception as e:
            print("something wrong!!")
            log.report(str(e))

    def show_database(self):
        print("         Showing Database          ")
        with open("csv_file/data.csv", 'r') as f:
            r = csv.reader(f)
            for i, row in enumerate(r):
                print(row)

    def total_cost_for_each(self):
        pass

    def exit(self):
        pass


if __name__ == "__main__":
    print("""
1: Add Cost.
2: Show Database.
3: Total Cost for Each Person.
5: Close Program.
""")

    # option = int(input("Enter your option: "))
    # set_custom_log_info()
    # field_name = ['Date', 'Name', 'Cost']
    # with open("csv_file/data.csv", "w") as f:
    #     csv_writer = csv.writer(f, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    #     csv_writer.writerow(field_name)

    log.set_custom_log_info()

    cls = MessCost()
    # cls.add_cost()
    cls.show_running_activities()






