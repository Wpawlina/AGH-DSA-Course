def goodStart(G):
    def DFSvisit(G,u):
        nonlocal visted,parent,times,time
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                parent[v]=u
                DFSvisit(G,v)
        time+=1
        times[u]=time
    n=len(G)
    visted=[False for _  in range(n)]
    parent=[None for _  in range(n)]
    time=0
    times=[0 for _ in range(n)]
    for i in range(n):
        if not visted[i]:
            DFSvisit(G,i)
    for i in range(n):
        if times[i]==n:
            pot=i
    visted=[False for _  in range(n)]
    time=0
    DFSvisit(G,pot)
    return time==n
G=[[1,2],[],[1,3],[4],[0],[0],[],[6]]
print(goodStart(G))

    
