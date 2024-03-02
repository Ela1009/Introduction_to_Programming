while True:
    string=input("Unesite 3 broja: ")
    a,b,c=string.split(" ")
    if a.isdigit() and b.isdigit() and c.isdigit():
        print (int(a)+int(b)+int(c))
    else:
        print("Greška")