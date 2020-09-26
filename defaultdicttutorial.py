# Hackerrank DefaultDict Tutorial problem solution

from collections import defaultdict
x,y = map(int, input().split())
lst1 = []
d = defaultdict(list)
for i in range(0,x):
    d[input()].append(i+1)
for i in range(0,y):
    lst1.append(input())
for i in lst1:
    if i in d:
        print(' '.join(map(str,d[i])))
    else:
        print('-1')