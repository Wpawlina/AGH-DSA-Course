def countingSort(T,k):
    n=len(T)
    C=[0]*k
    B=[None]*n
    for element in T:
        C[element]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[T[i]]-1]=T[i]
        C[T[i]]-=1
    for i in range(n):
        T[i]=B[i]
tab=[0,1,22,33,55,11,9,8,17,23,22,1,0,0,5,6,18]
countingSort(tab,56)
print(tab)
