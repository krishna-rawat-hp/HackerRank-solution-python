# Nested List 

if __name__ == '__main__':
    lst = list()
    sc = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        sc.append(score)
    lst.sort()
    sc.sort()
    i=0
    sm = sc[0]
    if sc[0]<sc[1]:
        sm = sc[1]
    else:
        while i<len(sc):
            if(sc[i]<sc[i+1]):
                sm = sc[i+1]
                break
            i+=1
    for i in lst:
        if i[1] == sm:
            print(i[0])
    
