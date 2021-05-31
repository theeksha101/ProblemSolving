x1, v1, x2, v2 = 43, 5, 49, 3
X = [x1, v1]
Y = [x2, v2]
back = min(X, Y)
fwd = max(X, Y)
print(back, fwd)

dist = fwd[0] - back[0]

while back[0] < fwd[0]:
    back[0] += back[1]
    fwd[0] += fwd[1]
    if fwd[0] - back[0] >= dist:
        break

print(["NO", "YES"][back[0] == fwd[0]])
