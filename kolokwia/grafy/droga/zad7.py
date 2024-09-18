from zad7testy import runtests
from queue import Queue




    


def droga( G ):
    n = len(G)
    Q=Queue()
    visted=[False for _ in range(n)]
    visted[0]=True
    route=[0]
    Q.put((0,0,visted,route))
    while not Q.empty():
        u,gate,vist,route=Q.get()
        for v in G[u][(gate+1)%2]:
            if v==0 and False not in vist:
                return route2
            if not vist[v]:
                vist2=vist.copy()
                vist2[v]=True
                route2=route.copy()
                route2.append(v)
                if u in G[v][0]:
                    Q.put((v,0,vist2,route2))
                else:
                    Q.put((v,1,vist2,route2))
            
    return None



def EulerCycle(G):
    def DFSvisit(G,u):
        nonlocal edges,cycle
        for v in G[u]:
                if edges[u][v]==0 and edges[v][u]==0:
                    edges[u][v]=1
                    edges[v][u]=1 
                    DFSvisit(G,v)
        cycle.append(u)
    n=len(G)
    edges=[[0 for _ in range(n)] for _ in range(n)]
    cycle=[]
    DFSvisit(G,0)
    cycle.reverse()                                              
    return cycle

def droga2( G ):
    n=len(G)
    G2=[[] for _ in range(2*n)]
    for i in range(n):
        for v in G[i][0]:
            if i in G[v][0]:
                G2[2*i].append(2*v)
               
            else:
                G2[2*i].append(2*v+1)
              
        for v in G[i][1]:
            if i in G[v][0]:
                G2[2*i+1].append(2*v)
              
            else:
               
                G2[2*i+1].append(2*v+1)
       
        G2[2*i].append(2*i+1)
        G2[2*i+1].append(2*i)
    cycle=EulerCycle(G2)
    for i in range(len(cycle)):
        cycle[i]//=2
    i=1
    while i < len(cycle):
        if cycle[i-1]==cycle[i]:
            del cycle[i-1]
        else:
            i+=1


            
    return cycle



        



G = [
    ([1], [2, 3, 4]),
    ([0],[2,5,6]),
    ([1, 5, 6], [0, 3, 4]),
    ([0, 2, 4], [5, 7, 8]),
    ([0, 2, 3], [6, 7, 9]),
    ([1, 2, 6], [3, 7, 8]),
    ([1, 2, 5], [4, 7, 9]),
    ([4, 6, 9], [3, 5, 8]),
    ([3, 5, 7], [9]),
    ([4, 6, 7], [8])
]
#print(droga(G))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True)