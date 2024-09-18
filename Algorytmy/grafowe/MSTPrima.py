from queue import PriorityQueue

def Prim(G,s):
    n=len(G)
    Q=PriorityQueue()
    dist=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    visted=[False for _ in range(n)]
    dist[s]=0
    parent[s]=s
    Q.put((dist[s],s))
    while not Q.empty():
        u=Q.get()[1]
        if not visted[u]:
            visted[u]=True
            for v in G[u]:
                if dist[v[0]] > v[1] and v[0]!=parent[u]:
                    dist[v[0]]=v[1]
                    parent[v[0]]=u
                    Q.put((dist[v[0]],v[0]))
    return dist,parent
G=[[[1,1],[5,3]],[[0,1],[2,2],[4,4]],[[1,2],[3,1],[5,1]],[[2,1],[4,3]],[[1,4],[3,3],[5,2]],[[0,3],[2,1],[4,2]]]
print(Prim(G,4))
    

        
            
        

    