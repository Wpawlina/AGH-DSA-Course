from zad2testy import runtests
from queue import PriorityQueue
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

def Dijkstra(G,L,W,S):
    m=len(W)
    n=len(G)
    distance=[[float('inf') for _ in range(m)] for _ in range(n)]
    Q=PriorityQueue()
    for s in S:
        distance[s][0]=0
        Q.put((distance[s][0],s,0))
    while not Q.empty():
        u=Q.get()
        for v in G[u[1]]:
            if u[2]+1 < m and L[v[0]]==W[u[2]+1]:
                if distance[v[0]][u[2]+1]> distance[u[1]][u[2]]+v[1]:
                    distance[v[0]][u[2]+1]=distance[u[1]][u[2]]+v[1]
                    Q.put((distance[v[0]][u[2]+1],v[0],u[2]+1))
    return distance
    





def letters( G, W ):
    L=G[0]
    G=EdgeListToNlistNDW(G[1])
    n=len(G)
    m=len(W)
    S=[]
    K=[]
    for i in range(n):
        if L[i]==W[0]:
            S.append(i)
        if L[i]==W[-1]:
            K.append(i)
    dist=Dijkstra(G,L,W,S)
    mind=float('inf')
    for k in K:
        if dist[k][m-1]<mind:
            mind=dist[k][m-1]
    if mind==float('inf'):
        return -1
    return mind









runtests( letters )
    
    
# L = ["k", "k", "o", "o", "t", "t"]
# E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
# G = (L, E)
# W = "kto"

# print( letters( (L, E), W) )