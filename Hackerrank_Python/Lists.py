# FOR ACCURATE CODE PREFER ROUGH CODE (RoughCode_List)

if __name__ == '__main__':
    N = int(input())
    List = []
    list_commands = {}
    prints = []

    for i in range(N):
        key, *values = input().split()
        int_value = list(map(int, values))
        list_commands[key] = int_value
        print(list_commands)

        for command in list_commands:
            if command == 'insert':
                List.insert(list_commands[command][0], list_commands[command][1])
            elif command == 'print':
                prints.append(List)
                print(List)
                print(prints)
            elif command == 'remove':
                List.remove(list_commands[command][0])
            elif command == 'append':
                List.append(list_commands[command][0])
            elif command == 'sort':
                List.sort()
            elif command == 'pop':
                List.pop()
            elif command == 'reverse':
                List.reverse()
        list_commands.clear()
        print(prints)

    for Lst in prints:
        print(Lst)
