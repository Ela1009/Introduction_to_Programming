def funkcija(m1,m2):
    if not (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        return False
    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i][j] != m2[i][j]:
                return False
    return True


m1=[[1,2],[3,4]]
m2=[[1,2],[3,4]]

print(funkcija(m1,m2))
