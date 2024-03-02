def razvrstaj(lst):
    prva = []
    druga = []
    for e1,e2 in lst:
        prva.append(e1)
        druga.append(e2)
    return prva,druga

lp = [ (1, -1), (3, -2), (16, -5), (3, 2) ]
print(razvrstaj(lp))
