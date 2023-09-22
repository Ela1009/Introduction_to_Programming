def funkcija(string):
    str1=[]
    str2=[]
    lista=string.split(",")
    for c in lista:
        if int(c)>0:
            str1.append(c)
        else:
            str2.append(c)
    return ",".join(str1), ",".join(str2)
    

print(funkcija("1,50,-7,40,-670"))