def zamijeni(s):
    r=""
    for c in s:
        if c.isupper():
            r+="$"
        elif c.islower():
            r+=c.upper()
        else:
            r+=c
    return r

print(zamijeni("aB cd EF"))
