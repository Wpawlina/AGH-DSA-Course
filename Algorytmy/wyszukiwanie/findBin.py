def findBin(tab,el):
    p=0
    k=len(tab)
    while p<=k:
        s=(p+k)//2
        if tab[s]==el:
            return s
        elif tab[s]>el:
            k=s-1
        else:
            p=s+1
    return -1

tab=[2,3,5,7,11,11,11,12,13,13,17,19,24,25,31]
print(findBin(tab,11))


