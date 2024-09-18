from egz3atesty import runtests
from queue import Queue

def MatrixToNListW(M):
    n=len(M)
    G=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j]!=-1:
                G[i].append([j,M[i][j]])
    return G

def bfs(G,s):
    n=len(G)
    dist=[[float('inf') for _ in range(17)] for _ in range(n)]
    Q=Queue()
    value=16
    dist[s][value]=0
    Q.put((s,value))
    while not Q.empty():
        u,value=Q.get()
        for v in G[u]:
            if v[1]<=value:
                if dist[v[0]][value-v[1]]>dist[u][value]+v[1]:
                    dist[v[0]][value-v[1]]=dist[u][value]+v[1]
                    Q.put((v[0],value-v[1]))
        prevValue=value
        value = 16
        for v in G[u]:
            if dist[v[0]][value-v[1]]>dist[u][prevValue]+v[1]+8:
                dist[v[0]][value-v[1]]=dist[u][prevValue]+v[1]+8
                Q.put((v[0],value-v[1]))
    return dist











def goodknight( G, s, t ):
    G=MatrixToNListW(G)
    dist=bfs(G,s)
    return min(dist[t])

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True)