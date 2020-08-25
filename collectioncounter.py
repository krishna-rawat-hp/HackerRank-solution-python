# collection.Counter() 

from collections import Counter
v = int(input())
lst = list(map(int, input().split()))
dic = Counter(lst)

c = int(input())
tm = 0
for i in range(c):
    x,y = input().split()
    for j in dic:
        if j == int(x):
            if(dic[j]>=1):
                tm = tm+int(y)
                dic[j] -=1 
            else:
                continue
        else:
            continue
print(tm)