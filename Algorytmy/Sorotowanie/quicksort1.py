def quickSort(tab,L,P):
    pivot=tab[(L+P)//2]
    i=L
    j=P
    while i <= j:
        while tab[i]<pivot:
            i+=1
        while tab[j]>pivot:
            j-=1
        if i<=j:
            tab[i],tab[j]=tab[j],tab[i]
            i+=1
            j-=1
    if j>L:
        quickSort(tab,L,j)
    if i<P:
        quickSort(tab,i,P)


        
tab=[11,22,-33,22,1000,0,-100,80,1,9]
quickSort(tab,0,9)
print(tab)
