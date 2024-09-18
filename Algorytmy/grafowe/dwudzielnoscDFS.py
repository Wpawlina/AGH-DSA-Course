


def dwudzielnosc(G):
    def DFSvisit(G,u):
        nonlocal visted,colors,res
        if res==False:
            return
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                colors[v]=(colors[u]+1)%2
                DFSvisit(G,v)
            elif colors[v]==colors[u]:
                res=False
    res=True
    n=len(G)
    visted=[False for _  in range(n)]
    colors=[-1 for _ in range(n)]
    colors[0]=0
    DFSvisit(G,0)
    return res

G=[[2,4],[2,3],[0,1],[1],[0]]
print(dwudzielnosc(G))

