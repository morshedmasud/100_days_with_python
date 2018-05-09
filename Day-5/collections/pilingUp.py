# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/piling-up/problem

for _ in range(int(input())):
  n = int(input())
  q = list(map(int, input().split()))

  for j in range(n-1):
    if q[0] >= q[-1]:
      q.pop(0)
    elif q[-1] >= q[-2]:
      q.pop()
    else:
      break

  print("Yes" if len(q) == 1 else "No")