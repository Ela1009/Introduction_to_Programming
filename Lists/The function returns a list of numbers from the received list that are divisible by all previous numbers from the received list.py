def funkcija(lista):
    nova=[]
    for i in range(len(lista)):
        brojac=0
        for j in range(i):
            if lista[i]%lista[j]!=0:
                brojac+=1
                
        if brojac==0:
            nova.append(lista[i])      
    return nova[1:]

print(funkcija([2,3,6,12,15]))
