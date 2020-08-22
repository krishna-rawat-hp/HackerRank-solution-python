x, y = input().split()
lst = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
c = 0
s = set()
for i in lst:
    s.add(i)
    if(s.intersection(s1)):
        c+=1
    if(s.intersection(s2)):
        c-=1
    s.remove(i)
print(c)
