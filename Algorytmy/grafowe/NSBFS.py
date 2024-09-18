
from queue import Queue


def BFS(G,s):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    dist=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    dist[s]=0
    Q.put([s,dist[s],0,0])
    while not Q.empty():
        u=Q.get()
        if u[1]==0:
            if not visted[u[0]]:
                visted[u[0]]=True
                parent[u[0]]=u[2]
                dist[u[0]]=dist[u[2]]+u[3]
                for v in G[u[0]]:
                    if not visted[v[0]]:
                        Q.put([v[0],v[1]-1,u[0],v[1]])
                    
        else:
            Q.put([u[0],u[1]-1,u[2],u[3]])
    return visted,dist,parent

G=[[[1,3],[2,1]],[[0,3],[2,5]],[[0,1],[1,5]]]
print(BFS(G,0))

