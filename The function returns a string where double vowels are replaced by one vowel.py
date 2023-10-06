def dvostruki_sugl(string):
    samoglasnici = ['a', 'e', 'i', 'o', 'u']
    novi_string = string[0]
    for c in string[1:]: 
        if c != novi_string[-1] or c in samoglasnici:
            novi_string += c
    return novi_string

print(dvostruki_sugl("lookk"))