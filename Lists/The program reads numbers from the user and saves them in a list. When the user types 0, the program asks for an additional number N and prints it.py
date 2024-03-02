lst = []
zbroj = 0

while True:
    br = int(input("Unesite broj koji zelite unijeti u listu: "))
    lst.append(br)
    if br == 0:
        N = int(input("Upisite dodatni broj N: "))
        if N > len(lst):
            print("Greska! Nema dovoljno brojeva u listi.")
        else:
            for i in range(len(lst) - N, len(lst)):
                zbroj += lst[i]
            print("Zbroj zadnjih", N, "upisanih brojeva: ", zbroj)
        break