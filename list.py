# Python Lists Example

if __name__ == '__main__':
    N = int(input())
    lst1 = list()
    for i in range(0,N):
        lst = list(input().split())
        if (lst[0] == 'insert'):
            lst1.insert(int(lst[1]), int(lst[2]))
        elif(lst[0] == 'remove'):
            lst1.remove(int(lst[1]))
        elif(lst[0] == 'append'):
            lst1.append(int(lst[1]))
        elif(lst[0] == 'sort'):
            lst1.sort()
        elif(lst[0] == 'pop'):
            lst1.pop()
        elif(lst[0] == 'reverse'):
            lst1.reverse()
        elif(lst[0] == 'print'):
            print(lst1)
