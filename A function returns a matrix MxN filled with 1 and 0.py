def kreiraj(n):
    mat = []
    for r in range(n):
        redak = []
        for s in range(n):
            if r <= s:
                redak.append(1)
            else:
                redak.append(0)
        mat.append(redak)
    return mat


mat = kreiraj(6)
for r in mat:
    print(r)
