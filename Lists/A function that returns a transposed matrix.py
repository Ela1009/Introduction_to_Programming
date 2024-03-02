def transponirana(ma, mb):
    # provjera dimenzija
    if not (len(ma) == len(mb[0]) and len(ma[0]) == len(mb)):
        return False
    for i in range(len(ma)):
        for j in range(len(mb)):
            if ma[i][j] != mb[j][i]:
                return False
    return True

m1 = [ 
      [ 1, 2, 3, 50 ],
      [ 4, 5, 6, 60 ],
      [ 7, 8, 9, 70 ]      
      ]

m2 = [ 
      [ 1, 4, 7 ],
      [ 2, 5, 8 ],
      [ 3, 6, 9 ],
      [ 50, 60, 70 ]      
      ]

m3 = [ 
      [ 1, 4, 7 ],
      [ 6, 5, 8 ],
      [ 3, 6, 9 ],      
      [ 50, 60, 70 ]      
      ]

print(transponirana(m1, m2))
print(transponirana(m1, m3))

