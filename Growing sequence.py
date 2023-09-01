lista=[1,2,3,4,5]
def Test(lista):
    prva=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<prva:
            return False
        prva=lista[i]
    return True
print(Test(lista))