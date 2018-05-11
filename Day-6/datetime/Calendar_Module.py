# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
# input from user for month, day, year
m, d, y = map(int, input().split())
# first we find out the weekday and then we make the real name for day using calendar.day_name()
print(calendar.day_name[calendar.weekday(y, m, d)].upper())