


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
G=[[1,5,4,3],[0,5,2,3],[1,3],[0,4,2,1],[0,3],[1,0]]

print(EulerCycle(G))

