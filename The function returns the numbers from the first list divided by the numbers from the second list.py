def funkcija(lst1,lst2):
    nova=[]
    for e1, e2 in zip(lst1,lst2):
        if e2==0:
            nova.append(0)
        else:
            nova.append(e1//e2)
    return nova
        

print(funkcija([2,4,4,6], [1,2,0,3]))