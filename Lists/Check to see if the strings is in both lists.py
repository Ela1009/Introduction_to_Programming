l1=["Split", "Solin", "Zadar","Sinj"]
l2=["Solin", "Sinj", "Omis"]

def Test(l1,l2):
    rj={}
    for k in l1:
        if k in l2:
            rj[k]=True
        else:
            rj[k]=False
    return rj

print(Test(l1,l2))
