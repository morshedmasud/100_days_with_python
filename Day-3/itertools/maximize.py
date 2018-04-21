# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product

k, m = map(int, input().split())
lis = []
for _ in range(int(k)):
    lis.append(list(map(int, input().split()))[1:])

result = sum(map(lambda x: x**2, lis)) % m
print(result)

print(lis)

print(list(product(*lis)))