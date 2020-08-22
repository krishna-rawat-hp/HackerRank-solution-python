# Merge the tool hackerrank problem

def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        s = list(string[i:i+k])
        l=list()
        for v in s: 
            if v not in l: 
                l.append(v)
        str1 = "".join(l)
        print(str1) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)