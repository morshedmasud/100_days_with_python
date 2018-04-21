# Go to the link to know about the problem
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations

n = int(input())
s = input().split()
k = int(input())

num = 0
den = 0
for i in combinations(s, k):
    den += 1
    num += 'a' in i

print(float(num/den))



from itertools import product
k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))
result = map(lambda x: sum(i**2 for i in x)%m, product(*n))
print(max(result))
