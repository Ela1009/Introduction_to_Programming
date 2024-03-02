def parni(r):
    p={}
    for k in r:
        if r[k]%2==0:
            p[k]=r[k]
    return p

rj={"a":12, "b":15, "c":16}

print(parni(rj))