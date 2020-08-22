# Symmetric Difference problem hackerrank

n = int(input())
s1 = set(map(int, input().split()))
m = int(input())
s2 = set(map(int, input().split()))
s3 = set()
v1 = s1.difference(s2)
v2 = s2.difference(s1)
s3.update(v1)
s3.update(v2)
l = list(s3)
l.sort()
for i in l:
    print(i)
