# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement
s, k = input().split()
for i in combinations_with_replacement(sorted(s), int(k)):
    print("".join(i))