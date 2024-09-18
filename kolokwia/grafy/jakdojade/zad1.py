
from zad1testy import runtests
from queue import PriorityQueue


def MatrixToNListW(M):
    n=len(M)
    G=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] >0:
                G[i].append([j,M[i][j]])
    return G

def createGasList(G,P):
    n=len(G)
    Gas=[False for _ in range(n)]
    for i in range(n):
        if i in P:
            Gas[i]=True
    return Gas
def Dijkstra(G,s,d,Gas):
    n=len(G)
    distance=[[float('inf') for _ in range(d+1)]  for _ in range(n)]
    parent=[[None for _ in range(d+1) ] for _ in range(n)]
    
    Q=PriorityQueue()
    distance[s][d]=0
    Q.put((distance[s][d],s,d))
    while not Q.empty():
        u=Q.get()
        full=u[2]
        u=u[1]
        prevf=full
        if Gas[u]:
            full=d
        for v in G[u]:
            if full-v[1]>=0:
                if distance[v[0]][full-v[1]]> distance[u][prevf]+v[1]:
                    distance[v[0]][full-v[1]]= distance[u][prevf]+v[1]
                    parent[v[0]][full-v[1]]=(u,prevf)
                    Q.put((distance[v[0]][full-v[1]],v[0],full-v[1]))
    return distance,parent

def findPath(parent,a,b,index):
    path=[]
    path.append(b)
    u=parent[b][index][0]
    index=parent[b][index][1]
    print(u,index,parent[u][index])
    while u!=a:
        path.append(u)
        u,index=parent[u][index][0],  parent[u][index][1]
      
       
       
    path.append(a)
    path.reverse()
    return path





def jak_dojade(G, P, d, a, b):
    G=MatrixToNListW(G)
    Gas=createGasList(G,P)
    mind=float('inf')
    mini=-1
    dist,parent=Dijkstra(G,a,d,Gas)
    for i in range(d+1):
        if dist[b][i]<mind:
            mind= dist[b][i]
            mini=i
    if mind==float('inf'):
        return None
    print(dist)
    print(parent)
    return findPath(parent,a,b,mini)
    


    


runtests( jak_dojade ) 

