# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

k, m = map(int, input().split())
n = []
for _ in range(k):
    n.append(list(map(int, input().split()))[1:])
temp = []

def test(arr):
    total = 0
    for i in arr:
        total += i*i
    return total%m

for j in product(*n):
    temp.append(test(j))

print(max(temp))