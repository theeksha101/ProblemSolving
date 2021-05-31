if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        name, *line = input().split()
        print(name)
        print(line)
        scores = list(map(float, line))
        print(scores)
