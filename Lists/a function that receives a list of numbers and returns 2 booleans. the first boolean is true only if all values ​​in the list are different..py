def funkcija(lista):
    svi_razliciti=True
    bar_dva=False
    brojacp=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]==lista[j]:
                svi_razliciti=False
                break
            if lista[i]>0:
                brojacp+=1
                if brojacp>=2:
                    bar_dva=True
                    break
    return svi_razliciti, bar_dva

print(funkcija([2,1,4,6,3,3]))