def funkcija(lst):
    novi=""
    for e in lst:
        brojac=0
        for c in e:
            if c.isdigit():
                brojac+=1
            if brojac==1:
                novi+=e + "," 
    return novi[:-1]
    
print(funkcija(["arc", "abc1", "efg44","3"]))
