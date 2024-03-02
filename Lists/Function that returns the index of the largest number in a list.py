def funkcija(lista):
    nova=[]
    for i in range (len(lista)):
        for j in range(i):
            if lista[i]%lista[j]!=0:
                break
        nova.append(lista[i])
             
    return nova

print(funkcija([2,3,6,12,15]))