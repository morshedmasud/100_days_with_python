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
        with open("csv_file/date.csv", "a") as csvf:
            csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(data)

    def show_running_cost(self):
        pass

    def total_cost_for_each(self):
        pass

    def exit(self):
        pass


if __name__ == "__main__":
    print("""
1: Add Cost.
2: Show Running Cost.
3: Total Cost.
4: Total Cost for Each Person.
5: Close Program.
""")

    # option = int(input("Enter your option: "))
    set_custom_log_info()
    field_name = ['Date', 'Name', 'Cost']
    with open("csv_file/date.csv", "w") as csvf:
        csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(field_name)
    cls = MessCost()
    cls.add_cost()




