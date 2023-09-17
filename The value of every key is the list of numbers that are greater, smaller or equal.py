def Test(lst,N):
    rj={}
    manji=[]
    veci=[]
    jednako=[]
    for broj in lst:
        if broj<N:
            manji.append(broj)
        if broj==N:
            jednako.append(broj)
        if broj>N:
            veci.append(broj)
    
    rj["manji"]=manji
    rj["jednako"]=jednako
    rj["veci"]=veci
    
    return rj

print(Test([1,3,5,9,6,12,9,11],9))