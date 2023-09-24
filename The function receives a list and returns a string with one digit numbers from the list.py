def spoji(lst):
    string=""
    for e in lst:
        if e<10:
            string=string+str(e)+","
    return string[:-1]

lst=[1,15,4,32,12]

print(spoji(lst))
