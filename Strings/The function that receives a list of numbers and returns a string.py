def spoji(lst):
    s=""
    for e in lst:
        s+=str(e)+";"
    return s[:-1]

lst=[2,4,5,6]
print(spoji(lst))