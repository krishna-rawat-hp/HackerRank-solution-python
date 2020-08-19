# Find the Runner-Up Score

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    arr.sort()
    if(arr[l-2]<arr[l-1]):
        print(arr[l-2])
    else:
        while l>0:
            if(arr[l-2]<arr[l-1]):
                print(arr[l-2])
                break
            l-=1
    
    
 