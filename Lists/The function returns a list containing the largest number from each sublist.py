def funkcija(lista):
    nova=[]
    for i in lista:
        maks=i[0]
        for e in i:
            if e>maks:
                maks=e
        nova.append(maks)
    return nova

print(funkcija([[1,2,3],[4,5,6]]))