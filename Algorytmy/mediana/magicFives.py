def partiton(T,L,P):
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
        i,j=partiton(T,L,P)
        quickSort(T,L,j)
        L=i

def megicFives(T):
    n=len(T)
    L=0
    P=4 if n>5 else n-1
    M=[]
    for i in range((n//5)):
        quickSort(T,L,P)
        k=(L+P)//2
        M.append(T[k])
        L=P+1
        P=P+5 if n>5 else n-1
    mn=len(M)
    quickSort(M,0,mn-1)
    return M[(mn-1)//2]


T=[24,-15,7,102,-56,33,0,91,-3,18,-77,42,5,-29,63,-8,11,-45,88,36,-12,72,-6,20,49,-91,2,13,-60,55]
print(megicFives(T))
