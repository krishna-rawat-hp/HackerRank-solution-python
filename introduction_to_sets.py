# Hackerrank problem Introduction to sets

def average(array):
    st = set(array)
    s = sum(st)
    l = len(st)
    avg = s/l
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)