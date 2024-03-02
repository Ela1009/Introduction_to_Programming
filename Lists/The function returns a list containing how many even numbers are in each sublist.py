def funkcija(lista):
    nova=[]
    for e in lista:
        brojac=0
        for i in e:
            if i%2==0:
                brojac+=1
        nova.append(brojac)
    return nova

print(funkcija([[1,2,3,4],[3,4,5,6,8]]))   