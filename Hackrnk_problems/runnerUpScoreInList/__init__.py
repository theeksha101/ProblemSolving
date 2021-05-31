lst = []
for _ in range(int(input("enter no. of students"))):
    name = input("enter name: ")
    score = float(input("enter score:"))
    lst.append([name, score])
print(lst)
for i in lst:
    print(i)
