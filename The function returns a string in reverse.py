def okreni(string):
    r=""
    for c in string:
        r=c+r
    return r 

print(okreni("abc def"))