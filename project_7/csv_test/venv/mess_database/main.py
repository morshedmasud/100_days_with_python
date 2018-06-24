from log import *
import csv
import sys


class MessCost:
    def __init__(self):
        pass

    def add_cost(self):
        pass

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

    option = int(input("Enter your option: "))
    
