def funkcija(lst,A,B):
     nova=[]
     for e in lst:
         if e > A and e < B:
             nova.append(e)
     return nova
 
print(funkcija([1,2,3,4,5,6,7],3,6))