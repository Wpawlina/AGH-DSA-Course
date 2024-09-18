def predicate(L,i,j):
    a,b=L[i]
    c,d=L[j]
    if a<=c and b>=d:
        return True
    return False

def tower(L):
    n=len(L)
    F=[1 for _ in range(n)]
    for i in range(1,n):
        best=1
        for j in range(i):
            if predicate(L,j,i):
                best=max(best,F[j]+1)
        F[i]=best
    max_height=max(F)
    return n-max_height

