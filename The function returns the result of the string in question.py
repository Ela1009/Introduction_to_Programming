def izracun(string):
    prvidio, n = string.split("**") #(A+B)  N
    aplusb = prvidio[1:4] #1+4
    a, b = aplusb.split("+") #1  4
    n = int(n)
    a = int(a)
    b = int(b)
    return (a + b) ** n
    
izraz = "(1+4)**2"
print(izracun(izraz))