# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
s, k = input().split()
for i in sorted(list(permutations(s, int(k)))):
    print("".join(i))