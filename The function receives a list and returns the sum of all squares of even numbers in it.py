def funkcija(lista):
    parni=[]
    kvadrati=[]
    zbroj=0
    for e in lista:
        if e%2==0:
            parni.append(e)
    for e in parni:
        kvadrati.append(e**2)
    for e in kvadrati:
        zbroj+=e
    return zbroj

print(funkcija([1,2,3,4]))
