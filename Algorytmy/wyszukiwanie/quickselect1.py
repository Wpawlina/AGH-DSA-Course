def partition(T,L,P):
    pivot=T[P]
    i=L-1
    for j in range(L,P):
        if T[j]<=pivot:
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

    
tab=[11,22,-33,22,1,0,-100,80,1,9]
print(quickSelect(tab,0,9,4))

