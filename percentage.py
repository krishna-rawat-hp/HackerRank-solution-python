# Find The Percentage 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lst = list()
    for i in student_marks:
        if i == query_name:
            lst = student_marks[i]
    sum = 0
    for j in lst:
        sum = sum+j
    val = sum/len(lst)
    print("%.2f"%round(val,2))
