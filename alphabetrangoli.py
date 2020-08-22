# Alphabet Rangoli Hacker rank solution

def print_rangoli(size):
    p = 97+size-1
    k = (2*size)-2
    for i in range(0,size):
        for j in range(0,k):
            print(end="-")
        for l in range(0,2*i+1):
            print(chr(p), end="")
            if(l!=2*i):
                print(end="-")
            if(l >= i):
                p+=1
            else:
                p-=1
        for j in range(0,k):
            print(end="-")
        print("")
        k=k-2
        p = 97+size-1
    k=2
    for i in range(size-1, 0, -1):
        for j in range(k, 0, -1):
            print(end="-")
        for j in range(2*i-1, 0, -1):
            print(chr(p), end="")
            if(j!=1):
                print(end="-")
            if(j <= i):
                p+=1
            else:
                p-=1
        for j in range(k, 0, -1):
            print(end="-")
        print("")
        k+=2
        p=97+size-1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)