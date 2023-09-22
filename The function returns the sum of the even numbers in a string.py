def funkcija(string):
    lst=string.split("+")
    zbroj=0
    for e in lst:
        if int(e)%2==0:
            zbroj+=int(e)
    return zbroj

print(funkcija("1+2+3+4"))