def findBinLast(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s]>el:
            k=s-1
        else:
            p=s+1
    if k>=0 and tab[k]==el:
        return k
    return -1

tab=[2,3,5,7,11,11,11,11,13,13,17,19,24,25,31]
print(findBinLast(tab,31))
