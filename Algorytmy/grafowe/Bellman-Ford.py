def BF(G,s):
    n=len(G)
    dist=[float("inf") for _ in range(n)]
    parent=[None for _ in range(n) ]
    dist[s]=0
    for i in range(n-1):
        for u in range(n):
            for v in G[u]:
                if dist[v[0]]>dist[u]+v[1]:
                    dist[v[0]]=dist[u]+v[1]
                    parent[v[0]]=u
        for u in range(n):
            for v in G[u]:
                if dist[v[0]]>dist[u]+v[1]:
                    return False,dist,parent
    return True,dist,parent
G=[[[1,10],[2,1],[3,-1],[4,3]],[[6,5]],[[4,-8]],[[5,2]],[[6,9],[1,4]],[[6,20]],[]]
print(BF(G,0))   