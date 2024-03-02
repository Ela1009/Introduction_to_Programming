def rastavi(string):
    niz = []
    poc = 0
    cilj = 0
    for i in range(len(string)):
        if string[i] == "(":
            poc = i+1
        elif string[i] == ")":
            cilj = i-1
            niz.append(string[poc:cilj+1])
    return niz

print(rastavi("ab(cd)ef(g)"))