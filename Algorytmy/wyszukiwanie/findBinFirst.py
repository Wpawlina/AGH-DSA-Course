def findBinFirst(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s]<el:
            p=s+1
        else:
            k=s-1
    if p<len(tab) and el==tab[p]:
        return p
    return -1



tab=[2,3,5,7,11,11,11,12,13,13,17,19,24,25,31]
print(findBinFirst(tab,31))
