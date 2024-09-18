
from queue import Queue


def brdidgeSR(G,s,f):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    dist1=[-1 for _ in range(n)]
    parent1=[None for _ in range(n)]
    visted[s]=True
    dist1[s]=0
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v]:
                Q.put(v)
                visted[v]=True
                parent1[v]=u
                dist1[v]=dist1[u]+1
    visted=[False for _ in range(n)]
    dist2=[-1 for _ in range(n)]
    parent2=[None for _ in range(n)]
    dist2[f]=0
    Q.put(f)
    visted[f]=True
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v]:
                Q.put(v)
                visted[v]=True
                parent2[v]=u
                dist2[v]=dist2[u]+1
    dist=dist1[f]
    edges=[]
    for i in range(n):
        for j in range(len(G[i])):
            curd=dist1[i]+dist2[G[i][j]]+1
            if curd==dist:
              edges.append((i,G[i][j]))
    
    de=[0 for _ in range(len(edges))]
    for i in range(len(edges)):
        de[i]=max(dist1[edges[i][1]],dist1[edges[i][0]])
    count=[0]*max(de)
    for e in de:
        count[e-1]+=1
    result=[]
    for i in range(len(edges)):
        if count[de[i]-1]==1:
            result.append(edges[i])
    if len(result)>0:
        return True,result
    return False


G=[[1,2,3],[0,4,2],[0,1,3,7],[0,2],[1,5],[4,6],[5,7,8],[2,9,6,8],[6,7,9],[7,8]]
G=[[1],[0,2,3],[1,4],[1,4],[2,3,5],[4,6,7],[5,8],[5,8],[6,7]]
print(brdidgeSR(G,0,8))



        
        
    
    








