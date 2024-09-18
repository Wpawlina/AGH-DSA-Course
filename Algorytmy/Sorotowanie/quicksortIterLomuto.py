def partition(T,L,P):
    pivot=T[P]
    i=L-1
    for j in range(L,P):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[P]=T[P],T[i+1]
    return i+1


def quickSort(T,L,P):
    stos=[]
    stos.insert(0,(L,P))
    while len(stos)>0:
        L,P=stos.pop(0)
        if L<P:
            q=partition(T,L,P)
            if q-L>P-q:
                stos.insert(0,(L,q-1))  
                stos.insert(0,(q+1,P))
            else:
                stos.insert(0,(q+1,P))
                stos.insert(0,(L,q-1))



tab=[11,22,-33,22,1,0,-100,80,1,9]
quickSort(tab,0,9)
print(tab)