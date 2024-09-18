def findBridges(G):
    def DFSvisit(G,u):
        nonlocal visted,lows,times,time
        time+=1
        times[u]=time
        lows[u]=time
        
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                parent[v]=u
                DFSvisit(G,v)
                lows[u]=min(lows[u],lows[v])
            elif v!=parent[u]:
                lows[u]=min(lows[u],times[v])

    n=len(G)
    visted=[False for _  in range(n)]
    lows=[0 for _  in range(n)]
    parent=[None for _  in range(n)]
    time=0
    times=[0 for _ in range(n)]
    DFSvisit(G,5)
    bridges=[]
    for i in range(n):
        if times[i]==lows[i] and parent[i] is not None:
            bridges.append((i,parent[i]))
    return bridges,times,lows,parent

G=[[1,2,3],[0,2],[0,1],[0,4,5],[3,5],[3,4]]
G=[[1,2],[0,2],[0,1,3],[2,4,5],[3,5],[3,4]]
G=[[1,2],[0,2],[0,1,3],[2,4,5],[3,5,7],[3,6,7],[5],[4,5,8,9],[7,9],[7,8]]
print(findBridges(G))





