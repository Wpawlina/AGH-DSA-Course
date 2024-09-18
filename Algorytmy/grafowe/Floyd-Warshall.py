def FW(G):
    n=len(G)
    S=[[float('inf') for _ in range(n)] for _ in range(n)]
    P=[[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            S[i][j]=G[i][j]
            if G[i][j]!=float('inf'):
                P[i][j]=i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][k]+S[k][j]<S[i][j]:
                    S[i][j]=S[i][k]+S[k][j]
                    P[i][j]=P[k][j]
    
    return S,P

G=[
   [0,9,4,3,float('inf'),2,6,float('inf')],
   [9,0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],
   [4,float('inf'),0,float('inf'),5,float('inf'),float('inf'),float('inf')],
   [3,float('inf'),float('inf'),0,1,float('inf'),float('inf'),float('inf')],
   [float('inf'),float('inf'),5,1,0,float('inf'),float('inf'),float('inf')],
   [2,float('inf'),float('inf'),float('inf'),float('inf'),0,7,3],
   [6,float('inf'),float('inf'),float('inf'),float('inf'),7,0,float('inf')],
   [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),3,float('inf'),0]
   ]
S,P=FW(G)
print(S),
print("=====")
print(P)
