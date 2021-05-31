import math

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        print(name)
        scores = list(map(float, line))
        print(scores)
        student_marks[name] = scores
        print(student_marks)
    query_name = input()
    print(query_name)

    for i in student_marks:
        if query_name == i:
            average = sum(student_marks[i]) / len(student_marks[i])
            print('%.2f' % average)
            break
