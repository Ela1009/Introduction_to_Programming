def jednom(string,broj):
    lst=string.split(" ")
    br=0
    for e in lst:
        if str(broj)==e:
            br+=1
    if br==1:
        return True
    else:
        return False


print(jednom("parni broj 42", 42))
print(jednom("10 plus 10", 10))