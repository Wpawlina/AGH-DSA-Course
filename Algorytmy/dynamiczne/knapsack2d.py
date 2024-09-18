def knapsack2d(P,W,H,B,V):
    n=len(P)
    F=[[[0]*(B+1)]*(V+1) for _ in range(n)]
    for w in range(W[0],B+1):
        for h in range(H[0],V+1):
            F[0][h][w]=P[0]
    for i in range(1,n):
        for w in range(B+1):
            for h in range(V+1):
                best=F[i-1][h][w]
                if W[i]<=w and H[i]<=h:
                    best=max(best,F[i-1][h-H[i]][w-W[i]])
                F[i][h][w]=best
    return F[n-1][V][B]
