s="abc,123,456"

def bez_zareza(s):
    sn=""
    for z in s:
        if z!=",":
         sn+=z
    return sn
        
print(bez_zareza(s))