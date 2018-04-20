# Go to the README file to know about the problem
from itertools import product

a = map(int, input().split())
b = map(int, input().split())
for item in product(a, b):
    print(item, end=" ")