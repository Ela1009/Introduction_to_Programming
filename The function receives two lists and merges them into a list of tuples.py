def spoji(lista1,lista2):
    nova=[]
    for e in zip(lista1,lista2):
        nova.append(e)
    return nova

lista1=[1,2,3,4,5]
lista2=["a","b","c"]

print(spoji(lista1,lista2))