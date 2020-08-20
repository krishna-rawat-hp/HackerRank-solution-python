# String split and join

def split_and_join(line):
    a = line.split()
    str1 = "-".join(a)
    return str1
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)