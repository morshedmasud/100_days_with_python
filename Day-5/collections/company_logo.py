# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter
s = input().strip()
temp = Counter(s)
for i in range(3):
  x= max(temp.values())
  maxs = [k for k, v in temp.items() if v == x]
  l = sorted(maxs)[0]
  print(l, x)
  del temp[l]