def findBin(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s]==el:
            return s
        elif tab[s]>el:
            k=s-1
        else:
            p=s+1
    return -1

tab=[1,2,5,6,7,11,11,11,13,13,14,15,28,42]

print(findBin(tab,1000000))