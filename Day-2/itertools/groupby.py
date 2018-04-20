# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby
s = input()

for k, g in groupby(s):
    print("({}, {})".format(len(list(g)), k), end=" ")
