rj={"Ivan":50, "Tina":50, "Jure":20}

def Test(rj):
    suma=0
    novi={}
    for k in rj:
        suma+=rj[k]
    for k in rj:
        novi[k]=rj[k]/suma*100
    return novi

print(Test(rj))