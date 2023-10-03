def zbroji(string1, string2):
    lst1 = string1.split(",")
    lst2 = string2.split(",")
    rez = []
    for e1, e2 in zip(lst1, lst2):
        zbr = int(e1) + int(e2)
        rez.append(str(zbr))
    return ",".join(rez)
    
print(zbroji("3,14,2,10", "6,11,5,5"))