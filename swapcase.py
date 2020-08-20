# Swap the case of string 

def swap_case(s1):
    s = list(s1)
    l = len(s)
    for i in range(l):
        if s[i] >='a' and s[i]<='z':
            s[i] = chr(ord(s[i])-32)
        elif s[i] >='A' and s[i] <='Z':
            s[i] = chr(ord(s[i])+32)
        else:
            s[i] = s[i]
    
    str1 = ''.join(s)
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
