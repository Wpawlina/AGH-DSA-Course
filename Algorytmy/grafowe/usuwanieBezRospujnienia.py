from queue import Queue

def deleteOrder(G):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    delete=[[i,-1] for i in range(n)]
    delete[0][1]=0
    visted[0]=True
    Q.put(0)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v]:
                Q.put(v)
                visted[v]=True
                delete[v][1]=delete[u][1]+1
    delete.sort(reverse=True,key=lambda x:x[1])
    for i in range(n):
        delete[i]=delete[i][0]
    return delete


G=[[2,4],[2,3],[0,1],[1],[0]]
print(deleteOrder(G))