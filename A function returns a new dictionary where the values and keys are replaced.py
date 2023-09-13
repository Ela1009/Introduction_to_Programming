def zamjenakv(rj):
    novi_rj = {}
    for k in rj:
            novi_rj[rj[k]] = k
    return novi_rj

rjecnik = {"ocjena1": "jedan", "ocjena2": "dva", "ocjena3": "tri", "ocjena4": "cetiri", "ocjena5": "pet"}
print(zamjenakv(rjecnik))