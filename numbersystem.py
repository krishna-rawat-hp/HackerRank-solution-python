# String Formatting 

def print_formatted(x):
    bl = len(str(bin(x)))-2
    for i in range(1, x+1):
        d = str(i)
        oc = str(oct(i))
        o = oc[2:]
        he = str(hex(i)).upper()
        h = he[2:]
        bi = str(bin(i))
        b = bi[2:] 
        print(d.rjust(bl), o.rjust(bl), h.rjust(bl), b.rjust(bl))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)