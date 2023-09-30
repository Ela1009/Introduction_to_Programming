def prebroji(s):
    lst=s.split(" ")
    z=0
    for e in lst:
        z+=int(e)
    return z

print(prebroji("3 62 -12 8"))