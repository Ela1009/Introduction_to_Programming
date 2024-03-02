def izracunaj(s):
    if "plus" in s:
        a, b = s.split("plus")
        return int(a) + int(b)
    else:
        a, b = s.split("minus")
        return int(a) - int(b)

print(izracunaj("23 plus 16"))
print(izracunaj("233 minus -2"))