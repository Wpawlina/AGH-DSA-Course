#f(i,e)=min(f(i-k,e-k+A[i-k]))+1
#f(0,e)=0
def zaba(A):
    n=len(A)
    F=[[-1 for _ in range(n)] for _ in range(n)]
    for e in range(A[0]):
        F[0][e]=0
    for i in range(1,n):
        best=float('inf')
        for j in range(i):
            for e in range(n):
                if F[j][e]!=-1:
                    if i-j<=e:
                        F[i][min(e-(i-j)+A[i],n-1)]=F[j][e]+1
    return min(F[n-1])

        
