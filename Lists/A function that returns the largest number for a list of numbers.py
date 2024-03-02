def funkcija(lst):
    maks=lst[0]
    for e in lst:
        if e>maks:
            maks=e
    return maks

print(funkcija([1,2,3,4]))