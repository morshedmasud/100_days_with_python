# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

lst = deque()
for i in range(int(input())):
  command = input().split()
  cmd = command[0]
  arg = command[1:]
  cmd += "(" + str(*arg) + ")"
  eval('lst.' + cmd)

print(*lst)