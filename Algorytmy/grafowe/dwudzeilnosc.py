from queue import Queue

def dwudzielnosc(G):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    colors=[-1 for _ in range(n)]
    visted[0]=True
    Q.put(0)
    colors[0]=0
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v]:
                Q.put(v)
                visted[v]=True
                colors[v]=(colors[u]+1)%2
            elif colors[u]==colors[v]:
                return False
    return True

G=[[2,4],[2,3],[0,1],[1],[0]]
print(dwudzielnosc(G))

