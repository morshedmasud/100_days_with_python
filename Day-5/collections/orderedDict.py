# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
my_order = OrderedDict()
for i in range(int(input())):
    user_input = input().split()
    name  = " ".join(user_input[:-1])
    price = int(user_input[-1])
    if name not in my_order:
        my_order[name] = price
    else:
        my_order[name] += price

for item, net_price in my_order.items():
    print(item, net_price)