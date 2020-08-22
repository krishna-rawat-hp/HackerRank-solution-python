# set.add() problem of hackerrank

val = int(input())
s = set()
for i in range(val):
    c = input()
    if c in s:
        continue
    else:
        s.add(c)
print(len(s))
