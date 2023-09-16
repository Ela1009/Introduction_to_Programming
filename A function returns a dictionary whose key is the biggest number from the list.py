def funkcija(lstlst):
    rjecnik={}
    for e in lstlst:
        najveci=e[0]   
        for b in e:
            if b>najveci:
                najveci=b  
        rjecnik[najveci]=e
    return rjecnik
        
                
print(funkcija([[ 6, 2],[7, 9 ]]))