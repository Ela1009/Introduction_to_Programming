def kreiraj(lst, m, n):
    mat = []
    i = 0
    for r in range(m):
        redak = []
        for s in range(n):
            if i >= len(lst):
                redak.append(0)
            else:                
                redak.append(lst[i])
            i += 1
        mat.append(redak)
    return mat

print(kreiraj([ 1, 2, 3, 4, 5, 6 ], 3, 5))
