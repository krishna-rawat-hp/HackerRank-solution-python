# string Validation

if __name__ == '__main__':
    s = input()
    alphaval = False
    alnumval = False
    digitval = False
    lowerval = False
    upperval = False 
    for i in s:
        if(i.isalnum()):
            alnumval = True
        if(i.isalpha()):
            alphaval = True
        if(i.isdigit()):
            digitval = True
        if(i.islower()):
            lowerval = True
        if(i.isupper()):
            upperval = True
    print(alnumval)
    print(alphaval)
    print(digitval)
    print(lowerval)
    print(upperval)
