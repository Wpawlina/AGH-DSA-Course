from zad3testy import runtests
from queue import PriorityQueue 

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
    return distance

def paths(G,s,t):
    n=len(G)
    dist=Dijkstra(G,s)
    dist2=Dijkstra(G,t)
    d=dist[t]
    if d==float('inf'):
        return 0
    cnt=0
    for i in range(n):
        for [v,w] in G[i]:
            if i<v:
                ed=min(dist[i]+dist2[v]+w,dist[v]+dist2[i]+w)
                if ed == d:
                    cnt+=1
    return  cnt


    
   

    
    
        

   


    
runtests( paths )


