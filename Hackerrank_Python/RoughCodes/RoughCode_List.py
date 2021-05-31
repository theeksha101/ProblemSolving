N = int(input())
List = []
list_commands = []
for i in range(N):
    command = input().split()
    List.append(command)

for i in List:
    if i[0] == 'append':
        if i[1].isdigit():
            list_commands.append(int(i[1]))
        else:
            list_commands.append(i[1])
    elif i[0] == 'insert':
        if i[2].isdigit():
            list_commands.insert(int(i[1]), int(i[2]))
        else:
            list_commands.insert(int(i[1]), i[2])
    elif i[0] == 'print':
        print(list_commands)
    elif i[0] == 'remove':
        if i[1].isdigit():
            list_commands.remove(int(i[1]))
        else:
            list_commands.remove(i[1])
    elif i[0] == 'sort':
        list_commands.sort()
    elif i[0] == 'pop':
        list_commands.pop()
    elif i[0] == 'reverse':
        list_commands.reverse()


