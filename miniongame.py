def minion_game(string):
    k=0
    s=0
    res = 'AEIOU'
    l=len(string)    
    for i in range(l): 
        if string[i] in res:
            k+=l-i
        else:
            s+=l-i


    
    if k>s:
        print("Kevin", k)
    elif s>k:
        print("Stuart", s)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)