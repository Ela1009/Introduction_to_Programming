def ukloni(s):
    lst=s.split(" ")
    lst2=[]
    for e in lst:
        if e!="":
            lst2.append(e)
    return " ".join(lst2)

print(ukloni("   ab    cde    fhg   "))
