def zbroji(lst):
    zbrojevi=[]
    for podlista in lst:
        zbroj=0
        for e in podlista:
            zbroj+=e
        zbrojevi.append(zbroj)
    return zbrojevi

print(zbroji([[2,3], [4,5]]))