from queue import Queue


def BFSMatrix(G,s):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    dist=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    visted[s]=True
    dist[s]=0
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in range(n):
                if G[u][v]==1 and  not visted[v]:
                    Q.put(v)
                    visted[v]=True
                    parent[v]=u
                    dist[v]=dist[u]+1
    return visted,dist,parent

G=[[0,0,1,0,1],[0,0,1,1,0],[1,1,0,0,0],[0,1,0,0,1],[1,0,0,1,0]]
print(BFSMatrix(G,0))
