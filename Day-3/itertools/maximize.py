# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product
k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))
print(n)
