def provjera(lista1,lista2):
    nova=[]
    for e1,e2 in zip(lista1,lista2):
        if e1>e2:
            nova.append(e1)
        else:
            nova.append(e2)
    return nova
    

print(provjera([2,1,4,6,3], [1,2,5,7,0]))