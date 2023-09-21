def provjera(string):
    novi=""
    for c in string:
        if c=="O":
            novi+="0"
        if c=="I":
            novi+="1"
        if c=="E":
            novi+="3"
        elif c!="O" and c!="I" and c!="E":
            novi+=c
    return novi
    
print(provjera("PREVELIKO"))