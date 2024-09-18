def ferry(C,L):
    n=len(C)
    res=0
    F=[[[-1]*(L+1)]*(L+1) for _ in range(n)]
    def f(w,i,L,R):
        nonlocal res
        if F[i][L][R]!=-1:
            return F[i][L][R]
        if i==n:
            res=max(res,w)
            return
        if C[i]>L and C[i]>R:
            res=max(res,w)
            return
        best=0
        if C[i]<=L:
            best=f(w+1,i+1,L-C[i],R)
        if C[i]<=R:
            best=max(best,f(w+1,i+1,L,R-C[i]))
        F[i][L][R]=best
        return F[i][L][R]
    f(0,0,L,L)
    return res

