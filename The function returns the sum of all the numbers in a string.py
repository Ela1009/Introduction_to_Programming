def provjera(string):
    lst=string.split(" ")
    zbroj=0
    for c in lst:
        zbroj+=int(c)
    return zbroj
        

print(provjera("3 6 12 8"))