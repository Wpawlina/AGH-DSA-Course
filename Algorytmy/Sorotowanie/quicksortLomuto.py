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
    while L<P:
        pivotIndex=partition(T,L,P)
        quickSort(T,L,pivotIndex-1)
        L=pivotIndex+1

tab=[11,22,-33,22,1,0,-100,80,1,9]
quickSort(tab,0,9)

#-33 22 11 22 1 0 -100 80 1 9
#-33 1 11 22 22 0 -100 80 1 9
# -33 1 0 22 22 11 -100 80 1 9
#-33 1 0 -100 1 11 22 80 22 9