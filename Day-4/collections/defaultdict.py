# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

m, n = map(int, input().split())
d = defaultdict(list)
lis = []
for i in range(1, m+1):
    d[input()].append(i)

for i in range(n):
    lis.append(input())

for x in lis:
    if x in d:
        print(" ".join(map(str, d[x])))
    else:
        print(-1)