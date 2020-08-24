from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
val = list(product(l1,l2))
for v in val:
    print(v,end=" ")