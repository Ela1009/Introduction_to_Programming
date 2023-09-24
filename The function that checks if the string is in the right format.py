def provjera(s):
    if len(s) !=8:
        return False
    if s[2]!=":" or s[5]!=":":
        return False
    if not s[:2].isdigit() or not s[3:5].isdigit() or not s[6:].isdigit():
        return False
    return True

print(provjera("22:33:15"))