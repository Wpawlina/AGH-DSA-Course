from egzP1btesty import runtests 
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

def Dijkstra(G,s,L):
    n=len(G)
    distance=[[float('inf') for _ in range(n) ] for _ in range(5)]
    Q=PriorityQueue()
    distance[0][s]=0

    Q.put((distance[0][s],s,0))
    while not Q.empty():
        u=Q.get()
        if u[2]==4:
            continue
        for v in G[u[1]]:
                    if distance[u[2]+1][v[0]]>=distance[u[2]][u[1]]+v[1]:
                        distance[u[2]+1][v[0]]=distance[u[2]][u[1]]+v[1]
                        Q.put((distance[u[2]+1][v[0]],v[0],u[2]+1))
                        
    return distance[4][L]


def turysta( G, D, L ):
    G=EdgeListToNlistNDW(G)
    return Dijkstra(G,D,L)
   
    
    


#end def 
#G=[(0,1,9),(0,2,1),(1,2,2),(1,3,8),(1,4,3),(2,4,7),(2,5,1),(3,4,7),(4,5,6),(3,6,8),(4,6,1),(5,6,1)]
#G=[(0,1,2),(1,2,1),(1,3,5),(1,4,10),(3,5,25),(4,5,21)]
#print(turysta(G,0,6))
runtests(turysta)