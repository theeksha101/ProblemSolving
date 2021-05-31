from __future__ import print_function

score_list = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        print(score)
        score_list[score].append(name)
        print(score_list)
    else:
        score_list[score] = [name]
        print(score_list)
new_list = []
for i in score_list:
    print(i)
    new_list.append([i, score_list[i]])
    print(new_list)
new_list.sort()
result = new_list[1][1]
result.sort()
print(*result, sep="\n")
