from log import *
from datetime import datetime
import csv
import sys


class MessCost:
    # def __init__(self):
    #     pass

    def add_cost(self):
        date = datetime.today()
        date = date.date()
        name = input("Type your name: ")
        cost = input("Enter today cost: ")
        data = [str(date), name, cost]

        with open("csv_file/data.csv", "a") as f:
            f = csv.writer(f)
            f.writerow(data)

    def show_running_activities(self):
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
2: Show Running activities.
3: Total Cost.
4: Total Cost for Each Person.
5: Close Program.
""")

    # option = int(input("Enter your option: "))
    # set_custom_log_info()
    # field_name = ['Date', 'Name', 'Cost']
    # with open("csv_file/data.csv", "w") as f:
    #     csv_writer = csv.writer(f, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    #     csv_writer.writerow(field_name)

    cls = MessCost()
    cls.show_running_activities()






