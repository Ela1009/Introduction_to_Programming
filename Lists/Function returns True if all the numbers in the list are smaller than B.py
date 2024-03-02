def manjiodB(rjecnik, B):
    for k in rjecnik:
        for v in rjecnik[k]:
            if v >= B:
                return False #cim nade jedan da je veci od B -> vraca False
    return True #inace True

B = ord('B') #vrijednost od B -> 66

rjecnik = {1: [1, 2, 3, 4, 5], 2: [10, 20, 30, 40, 50], 3: [44, 48, 52, 56, 60, 64]}
rjecnik1 = {1: [1, 2, 3, 4, 5], 2: [10, 20, 30, 40, 50, 100], 3: [44, 48, 52, 56, 60, 64]}

print(manjiodB(rjecnik, B))
print(manjiodB(rjecnik1, B))