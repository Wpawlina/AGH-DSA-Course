def MatrixToNList(M):
    n=len(M)
    G=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                G[i].append(j)
    return G

def MatrixToNListW(M):
    n=len(M)
    G=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] not in (float('inf'),0):
                G[i].append([j,M[i][j]])
    return G

def NListToMatrix(G):
    n=len(G)
    M=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            M[i][v]=1
    return M

def NListToMatrixW(G):
    n=len(G)
    M=[[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        M[i][i]=0
    for i in range(n):
        for v in G[i]:
            M[i][v[0]]=v[1]
    return M

def NListToEdgeListND(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v:
                E.append([i,v])
    return E

def NListToEdgeListNDW(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v[0]:
                E.append([i,v[0],v[1]])
    return E

def NListToEdgeListD(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
                E.append([i,v])
    return E

def NListToEdgeListDW(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v[0]:
                E.append([i,v[0],v[1]])
    return E

def EdgeListToNlistND(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    return G

def EdgeListToNlistNDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append([e[1],e[2]])
        G[e[1]].append([e[0],e[2]])
    return G

def EdgeListToNlistD(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append(e[1])
    return G

def EdgeListToNlistDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append([e[1],e[2]])
    return G

def MatrixToEdgeListND(M):
    n=len(M)
    E=[]
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                if i<j:
                    E.append([i,j])
    return E


def MatrixToEdgeListNDW(M):
    n=len(M)
    E=[]
    for i in range(n):
        for j in range(n):
            if M[i][j] not in (float('inf'),0):
                if i<j:
                    E.append([i,j,M[i][j]])
    return E

def MatrixToEdgeListD(M):
    n=len(M)
    E=[]
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                    E.append([i,j])
    return E                   

def MatrixToEdgeListDW(M):
    n=len(M)
    E=[]
    for i in range(n):
        for j in range(n):
            if M[i][j] not in (float('inf'),0):
                    E.append([i,j,M[i][j]])
    return E

def EdgeListToMatrixND(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    M=[[0 for _ in range(m)] for _ in range(m)]
    for e in E:
        M[e[0]][e[1]]=1
        M[e[1]][e[0]]=1
    return M

def EdgeListToMatrixNDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    M=[[0 for _ in range(m)] for _ in range(m)]
    for e in E:
        M[e[0]][e[1]]=e[2]
        M[e[1]][e[0]]=e[2]
    return M

def EdgeListToMatrixD(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    M=[[0 for _ in range(m)] for _ in range(m)]
    for e in E:
        M[e[0]][e[1]]=1
    return M

def EdgeListToMatrixDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    M=[[0 for _ in range(m)] for _ in range(m)]
    for e in E:
        M[e[0]][e[1]]=e[2]
    return M













