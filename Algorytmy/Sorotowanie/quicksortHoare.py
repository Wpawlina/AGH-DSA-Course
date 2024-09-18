def partition(T,L,P):
    pivot=T[(L+P)//2]
    i=L
    j=P
    while i<=j:
        while T[i]<pivot:
            i+=1
        while T[j]>pivot:
            j-=1
        if i<=j:
            T[i],T[j]=T[j],T[i]
            i+=1
            j-=1
    return i,j
def quickSort(T,L,P):
    while L<P:
        i,j=partition(T,L,P)
        quickSort(T,L,j)
        L=i
#tab=[11,22,-33,22,1,0,-100,80,1,9]
tab=[0,1,22,33,55,11,9,8,17,23,22,1,0,0,5,6,18]
quickSort(tab,0,16)
print(tab)

        