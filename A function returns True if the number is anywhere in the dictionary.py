def negdje(rj, br):
    for k in rj:
        if br in rj[k]: #ako se broj nalazi u nekoj od lista (koje su vrijednosti) salje True
            return True
    return False

rjecnik = {1: [2, 3, 4], 5: [6, 8], 10: [7, 9]}

print(negdje(rjecnik, 6))
print(negdje(rjecnik, 5))