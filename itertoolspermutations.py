from itertools import permutations
x, y = input().split()
lst = list(permutations(x,int(y)))
lst.sort()
for i in lst:
    str = ''.join(i)
    print(str)