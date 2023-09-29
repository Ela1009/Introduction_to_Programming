def funkcija(str1,str2,N):
    sam=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    brsam=0
    brsug=0
    for c in str1:
        if c in sam:
            brsam+=1
            
    for c in str2:
        if c.isalpha() and c not in sam:
            brsug+=1
    if brsam==N and brsug==N:
        return True
    return False
    
print(funkcija("uzeti","abcde",3))