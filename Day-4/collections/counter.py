# Go to the link to know about problem
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
shoes = int(input())
size = Counter(map(int, input().split()))

total_amount = 0
for i in range(int(input())):
  s, m = map(int, input().split())
  if s in size and size[s] > 0:
    size[s] -= 1
    total_amount += m

print(total_amount)