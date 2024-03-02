def konstruiraj(lst):
    rj = {}
    for i in lst:
        zbr = 0
        for e in i:
            zbr += e
        rj[zbr] = i #vrijednost
    return rj
    
print(konstruiraj([[5, 8, 10, 25, 2], [80, 90, 40, 3], [77, 11, 42]]))