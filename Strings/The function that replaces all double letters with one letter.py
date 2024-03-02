def funkcija(s):
    r=" "
    for i in range (len(s)):
        if s[i]!=s[i-1]:
            r+=s[i]
    return r

s="llllllllook aat thiss"
print(funkcija(s))