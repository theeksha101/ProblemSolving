def split_and_join(line):
    list_string = line.split()
    joint = '-'.join(list_string)
    return joint


# write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
