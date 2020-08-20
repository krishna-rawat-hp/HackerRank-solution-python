# Designer Door Mat

x, y = input().split()
x = int(x)
y = int(y)

v1 = (x//2)+1
v2 = (y//2)-3
v3 = (y//2)-1
s1 = "-"
s2 = "WELCOME"
s3 = ".|."
i=1
for a in range(1, x+1):
    if(a == v1):
        print(s1*v2+s2+s1*v2)
    else:
        if(a < v1):
            print(s1*v3+s3*i+s1*v3)
            i+=2
            v3-=3
        elif(a > v1):
            i-=2
            v3+=3
            print(s1*v3+s3*i+s1*v3)
