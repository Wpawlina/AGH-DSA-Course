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
    stos=[]
    stos.append((L,P))
    while len(stos)>0:
        L,P=stos.pop()
        if L<P:
            i,j=partition(T,L,P)
            if j-L>P-i:
                stos.append((i,P))
                stos.append((L,j))  
            else:
                stos.append((L,j))
                stos.append((i,P))

tab=[11,22,-33,22,1,0,-100,80,1,9]
quickSort(tab,0,9)
print(tab)

        