from egzP5btesty import runtests 


def EdgeListToNlistND(E):
    n=len(E)
    m=0
    for (start,end) in E:
        m=max(m,start,end)
    m+=1

    G=[[]for _ in range(m)]
    for e in E:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
    return G

def koleje (B):
    G=EdgeListToNlistND(B)
    def DFSvisit(G,u):
        nonlocal visted,lows,times,time,points
        time+=1
        times[u]=time
        lows[u]=time
        children=0
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                parent[v]=u
                DFSvisit(G,v)
                lows[u]=min(lows[u],lows[v])
                children+=1
                if lows[v]>=times[u]:
                    if parent[u] is not None or children>=2:
                        points[u]=True
            elif  v!=parent[u]:
                lows[u]=min(lows[u],times[v])
                

    n=len(G)
    visted=[False for _  in range(n)]
    lows=[0 for _  in range(n)]
    parent=[None for _  in range(n)]
    time=0
    times=[0 for _ in range(n)]
    points=[False for _ in range(n)]


    DFSvisit(G,0)


    return points.count(True)

    
   
    
#end procedure koleje()

runtests ( koleje, all_tests=True )
