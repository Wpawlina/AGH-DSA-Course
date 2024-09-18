def lis(T):
    n=len(T)
    F=[1]*n
    P=[-1]*n
    for k in range(1,n):
        for t in range(k):
            if T[t]<T[k] and F[k]<F[t]+1:
                F[k]=F[t]+1
                P[k]=t
    maxl=-1
    maxk=-1
    for i in range(n):
        if F[i]>maxl:
            maxl=F[i]
            maxk=i
    return maxk,F,P

def print_sol(T,P,k):
    if P[k]!=-1:
        print_sol(T,P,P[k])
    print(T[k])

T=[2,1,4,3,4,8,5,7]
k,F,P=lis(T)
print_sol(T,P,k)

        