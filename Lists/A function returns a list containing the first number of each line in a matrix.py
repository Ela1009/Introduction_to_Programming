def prviuretku(mat):
    lst = []
    for r in mat:
        lst.append(r[0]) #za svaki redak dodaje prvi broj (indeksa 0) u listu
    return lst

print(prviuretku([[8, 7, 4, 5], [2, 3, 0, 6], [9, 0, 1, 1]]))
