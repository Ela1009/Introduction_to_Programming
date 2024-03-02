def isprepleti(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        #clan prve pa clan druge dodajemo u novu listu, za svaki indeks
        lst.append(lst1[i])
        lst.append(lst2[i])
    return lst

lsta = [1, 3, 5]
lstb = [2, 4, 6]

print(isprepleti(lsta, lstb))
