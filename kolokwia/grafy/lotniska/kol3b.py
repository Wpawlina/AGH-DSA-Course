#from kol3btesty import runtests
from queue import PriorityQueue

def Dijkstra(G,s,A):
    n=len(G)
    distance=[float('inf')for _ in range(n)]
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        for v in G[u[1]]:
            if distance[v[0]]> distance[u[1]]+v[1]:
                distance[v[0]]=distance[u[1]]+v[1]
                Q.put((distance[v[0]],v[0]))
        for v in range(n):
            if v!=u[1]:
                if distance[v]> distance[u[1]]+A[u[1]]+A[v]:
                    distance[v]=distance[u[1]]+A[u[1]]+A[v]
                    Q.put((distance[v],v))
    return distance

def airports( G, A, s, t ):
    dist=Dijkstra(G,s,A)
    return dist[t]

   
#end procedure airports()
G = [
    [(1, 3), (3, 2)],
    [(0, 3), (2, 20)],
    [(1, 20), (5, 1), (3, 6)],
    [(0, 2), (2, 6), (4, 1)],
    [(3, 1), (5, 7)],
    [(4, 7), (2, 1)]
]

A=[50,100,1,20,2,70]
print(airports(G,A,0,5))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( airports, all_tests = True )