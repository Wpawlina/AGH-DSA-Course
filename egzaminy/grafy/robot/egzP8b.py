from egzP8btesty import runtests

def FW(G):
    n=len(G)
    S=[[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            S[i][j]=G[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][k]+S[k][j]<S[i][j]:
                    S[i][j]=S[i][k]+S[k][j]
    return S


def NListToMatrixW(G):
    n=len(G)
    M=[[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        M[i][i]=0
    for i in range(n):
        for v in G[i]:
            M[i][v[0]]=v[1]
    return M


def robot( G, P ):
    M=NListToMatrixW(G)
    m=len(P)
    S=FW(M)
  
    dist=0
    for i in range(1,m):
        dist+=S[P[i-1]][P[i]]
    return dist


runtests(robot, all_tests = True)
