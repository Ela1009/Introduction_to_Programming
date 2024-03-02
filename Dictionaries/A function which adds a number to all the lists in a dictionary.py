def dodaj(r, b):
    for k in r:
        r[k].append(b)
    

rj = {
      "a": [ 1, 2, 3],
      "b": [ 2, 3],
      "c": [ 3 ],      
      }

dodaj(rj, 4)
print(rj)
