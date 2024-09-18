
from queue import Queue

def spojnosc(G):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    visted[0]=True
    Q.put(0)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v]:
                Q.put(v)
                visted[v]=True
    if False in visted:
        return False
    return True
G=[[1,2],[0],[0,3],[2]]
print(spojnosc(G))