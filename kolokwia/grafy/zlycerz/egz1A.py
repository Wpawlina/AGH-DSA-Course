from egz1Atesty import runtests
from queue import PriorityQueue



def Dijkstra(G,s):
    n=len(G)
    distance=[float('inf') for _ in range(n)]
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
                    
                    Q.put((distance[v[0]],v[0]))
    return distance



def DijkstraPo(G,s,r):
    n=len(G)
    distance=[float('inf') for _ in range(n)]
    visted=[False for _ in range(n)]
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        if not visted[u[1]]:
            visted[u[1]]=True
            for v in G[u[1]]:
                if distance[v[0]]> distance[u[1]]+2*v[1]+r:
                    distance[v[0]]=distance[u[1]]+2*v[1]+r
                    Q.put((distance[v[0]],v[0]))
    return distance

def gold(G,V,s,t,r):
  dist1=Dijkstra(G,s)
  dist2=DijkstraPo(G,t,r)
  minCost=dist1[t]
  n=len(V)
  for i in range(n):
      cost=dist1[i]+dist2[i]-V[i]
      minCost=min(cost,minCost)
  return minCost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
