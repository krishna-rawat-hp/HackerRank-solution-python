# List Comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = list()
    for i1 in range(0,x+1):
        for i2 in range(0,y+1):
            for i3 in range(0,z+1):
                if i1+i2+i3 == n:
                    continue
                lst.append([i1,i2,i3])
print(lst)
