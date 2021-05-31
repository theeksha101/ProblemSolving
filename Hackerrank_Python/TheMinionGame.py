def minion_game(string):
    # your code goes here
    list_consonants = []
    list_vowels = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string:
        if i in vowels:
            temp = ''
            j = string.index(i)
            if i in list_vowels:
                j = string.index(i, string.index(i) + 1)
                for k in range(j, len(string)):
                    list_vowels.append(temp + string[j])
                    temp = list_vowels[len(list_vowels) - 1]
                    j += 1
                continue
            for k in range(j, len(string)):
                list_consonants.append(temp + string[j])
                temp = list_consonants[len(list_consonants) - 1]
                j += 1
        else:
            temp = ''
            j = string.index(i)
            if i in list_consonants:
                j = string.index(i, string.index(i) + 1)
                for k in range(j, len(string)):
                    list_consonants.append(temp + string[j])
                    temp = list_consonants[len(list_consonants) - 1]
                    j += 1
                continue
            for k in range(j, len(string)):
                list_consonants.append(temp + string[j])
                temp = list_consonants[len(list_consonants) - 1]
                j += 1

    print(list_vowels)
    print(list_consonants)


if __name__ == '__main__':
    s = 'banana'
    minion_game(s)

