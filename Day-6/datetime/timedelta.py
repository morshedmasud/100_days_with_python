# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime

#  Day dd Mon yyyy hh:mm:ss +xxxx
fmt = "%a %d %b %Y %H:%M:%S %z"

for i in range(int(input()) ):
    t1 = datetime.datetime.strptime( input().strip(), fmt )
    print(t1)
    t2 = datetime.datetime.strptime( input().strip(), fmt )
    diff = datetime.timedelta.total_seconds(t1 - t2)
    print( abs( int(diff) ) )