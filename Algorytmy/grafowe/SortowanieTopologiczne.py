def SortTopology(G):
    def DFSvisit(G,u):
        nonlocal visted,sortedT
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                DFSvisit(G,v)
        sortedT.append(u)
        
        
    n=len(G)
    visted=[False for _  in range(n)]
    sortedT=[]
    for i in range(n):
        if not visted[i]:
            DFSvisit(G,i)
    sortedT.reverse()
    return sortedT


G=[[2],[],[4],[],[1,3]]
print(SortTopology(G))