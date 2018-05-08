# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())
total = 0
student = namedtuple('student', input())
for i in range(n):
   s = student(*input().split())
   total += int(s.MARKS)

print("%.2f" % (total/n))