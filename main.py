r = int(input())
c = int(input())
A = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    A.append(row)
def diagonal(A):
    res = []
    for i in range(2 * len(A) - 1):
        if i < len(A):
            z = 0
        else:
            z = i - len(A) + 1
        temp = []
        for j in range(z, i - z + 1):
            temp.append(A[j][i - j])
        res.append(temp)
    return res
anti_diagonals = diagonal(A)
for anti_diagonal in anti_diagonals:-
    print(' '.join(map(str, anti_diagonal)))
