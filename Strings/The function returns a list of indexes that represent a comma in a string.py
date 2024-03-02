def zarezi(string):
    lst=[]
    indeks=-1
    while True:
        indeks=string.find(",", indeks+1)
        if indeks<0:
            return lst
        lst.append(indeks)

print(zarezi("ab,cd,e,f"))