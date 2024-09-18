


def DFS(G):
    def DFSvisit(G,u):
        nonlocal visted,parent,times,time
        time+=1
        times[u]=time
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                parent[v]=u
                DFSvisit(G,v)
        


    n=len(G)
    visted=[False for _  in range(n)]
    parent=[None for _  in range(n)]
    time=0
    times=[0 for _ in range(n)]
    for i in range(n):
        if not visted[i]:
            DFSvisit(G,i)
    return visted,parent,times


G=[[2,4],[2,3],[0,1],[1,4],[0,3]]
print(DFS(G))

