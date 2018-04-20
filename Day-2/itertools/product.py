# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product

a = map(int, input().split())
b = map(int, input().split())
for item in product(a, b):
    print(item, end=" ")