def jednakprosjeku(rj):
    for k in rj:
        zbr = 0
        for e in rj[k]: #value je lista pa secemo ovako po elementima
            zbr += e
        if k != zbr / len(rj[k]):
            return False
    return True
    
           

rjecnik = {20: [10, 30, 0, 40], 5: [1, 4, 8, 7], 50: [10, 60, 40, 90, 50]}
rjecnik2 = {8: [55, 4], 16: [7, 64, 1,]}

print(jednakprosjeku(rjecnik))
print(jednakprosjeku(rjecnik2))