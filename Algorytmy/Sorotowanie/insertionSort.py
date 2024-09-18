def insertionSort(T):
    n=len(T)
    for i in range(1,n):
        k=i-1
        pom=T[i]
        while k>=0 and T[k]>pom:
            T[k+1]=T[k]
            k-=1
        T[k+1]=pom

tab=[11,22,-33,22,1,0,-100,80,1,9]
insertionSort(tab)
print(tab)
