def najveciulst(rj):   
    for k in rj: 
        najv = rj[k][0] 
        for e in rj[k]:
            if e > najv: 
                najv = e
        rj[k] = najv 
    return rj 

rjecnik = {"haha": [10, 30, 0, 40], "hehe": [1, 4, 8, 7], "hihi": [10, 60, 40, 90, 50]}

print(najveciulst(rjecnik))