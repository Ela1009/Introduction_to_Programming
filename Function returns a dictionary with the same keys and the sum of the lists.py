def zbrojevi(rj):
    for k in rj:
        zbroj = 0
        for e in rj[k]:
            zbroj += e
        rj[k] = zbroj
    return rj

rj = {
      "a": [ 1, 2, 3 ],
      "b": [ 1, 2, 3, 4 ],
      "c": [ 10, 20, 30 ]
      }

print(zbrojevi(rj))
