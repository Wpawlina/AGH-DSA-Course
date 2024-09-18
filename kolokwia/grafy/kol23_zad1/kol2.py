from kol2testy import runtests
from queue import Queue

def spojnosc(E,m):
    Q=Queue()
    n=len(E)
    visted=[False for _ in range(m)]
    visted[0]=True
    Q.put(0)
    while not Q.empty():
        u=Q.get()
        for i in range(n):
            if E[i][0]==u and not visted[E[i][1]]:
                Q.put(E[i][1])
                visted[E[i][1]]=True
            if E[i][1]==u and not visted[E[i][0]]:
                Q.put(E[i][0])
                visted[E[i][0]]=True

    if False in visted:
        return False
    return True


def NListToEdgeListNDW(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v[0]:
                E.append([i,v[0],v[1]])
    return E

def sumOfWeights(T):
    res=0
    for e in T:
        res+=e[2]
    return res






def beautree(G):
    E=NListToEdgeListNDW(G)
    n=len(G)
    m=len(E)
    E.sort(key=lambda x: x[2])
    for i in range(m-(n-1)):
        T=E[i:i+n-1]
        if spojnosc(T,n):
            return sumOfWeights(T)
    return None
            

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)
