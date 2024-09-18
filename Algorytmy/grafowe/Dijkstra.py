from queue import PriorityQueue

def Dijkstra(G,s):
    n=len(G)
    distance=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    visted=[False for _ in range(n)]
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        if not visted[u[1]]:
            visted[u[1]]=True
            for v in G[u[1]]:
                if distance[v[0]]> distance[u[1]]+v[1]:
                    distance[v[0]]=distance[u[1]]+v[1]
                    parent[v[0]]=u[1]
                    Q.put((distance[v[0]],v[0]))
    return parent,distance

G=[[[1,2],[2,4]],[[0,2],[2,1],[3,4]],[[0,4],[1,1],[3,2],[4,1]],[[1,4],[2,2],[5,1]],[[2,1],[5,3]],[[3,1],[4,3]]]
print(Dijkstra(G,0))
    



