def partition(T,L,P):
    pivot=T[P]
    i=L-1
    for j in range(L,P):
        if T[j]>=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[P]=T[P],T[i+1]
    return i+1

def quickSelect(T,L,P,k):
    if L==P:
        return T[P]
    pivotIndex=partition(T,L,P)
    if pivotIndex==k:
        return T[pivotIndex]
    elif pivotIndex<k:
        return quickSelect(T,pivotIndex+1,P,k)
    else:
        return quickSelect(T,L,pivotIndex-1,k)
    
def partition2(T,L,P):
    pivot=T[(L+P)//2]
    i=L
    j=P
    while i<=j:
        while T[i]>pivot:
            i+=1
        while T[j]<pivot:
            j-=1
        if i<=j:
            T[i],T[j]=T[j],T[i]
            i+=1
            j-=1
    return i,j
def quickSort(T,L,P):
    stos=[]
    stos.insert(0,(L,P))
    while len(stos)>0:
        L,P=stos.pop(0)
        if L<P:
            i,j=partition2(T,L,P)
            if j-L>P-i:
                stos.insert(0,(i,P))
                stos.insert(0,(L,j))  
            else:
                stos.insert(0,(L,j))
                stos.insert(0,(i,P))




def section(T,p,q):
    n=len(T)
    quickSelect(T,0,n-1,p)
    quickSelect(T,p,n-1,q)
    quickSort(T,p,q)
    print(T[p:q+1])
    

T = [10, 15, 34, 80, 97, 15, 24, 34, 11, 8, 2, 3]
section(T, 5, 8)

