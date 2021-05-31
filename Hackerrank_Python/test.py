from collections import defaultdict

s = 'banana'

vowels = defaultdict(int)
consonants = defaultdict(int)
for k in range(len(s)):
    for i in range(1, len(s) + 1):
        t = "".join([s[j] for j in range(k, i)])
        if len(t) > 0:
            if t[0] in 'aeiou':
                vowels[t] += 1
            else:
                consonants[t] += 1
print(vowels)
print(consonants)
# print(sum(vowels.values()))
# print(sum(consonants.values()))

if len(consonants) > len(vowels):
    print('{} {}'.format('Stuart', sum(consonants.values())))
else:
    print('{} {}'.format('Kevin', sum(vowels.values())))
