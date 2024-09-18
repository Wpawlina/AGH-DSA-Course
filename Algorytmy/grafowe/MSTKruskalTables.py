

def Kruksal(E):
    E.sort(key=lambda x:x[2])
    n=len(E)
    m=max(E,key=lambda x:x[1])[1]+1
    parent=[i for i in range(m)]
    rank=[0 for i in range(m)]
    def find(x):
        nonlocal parent
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
            nonlocal parent,rank
            x=find(x)
            y=find(y)
            if x==y:
                return
            if rank[x]>rank[y]:
                parent[y]=x
            else:
                parent[x]=y
                if rank[x]==rank[y]:
                    rank[y]+=1

    A=[]
    for e in E:
        x=find(e[0])
        y=find(e[1])
        if x!=y:
            A.append(e)
            union(x,y)
    return A 


def NListToEdgeListNDW(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v[0]:
                E.append([i,v[0],v[1]])
    return E


G=[[[1,1],[5,3]],[[0,1],[2,2],[4,4]],[[1,2],[3,1],[5,1]],[[2,1],[4,3]],[[1,4],[3,3],[5,2]],[[0,3],[2,1],[4,2]]]
E=NListToEdgeListNDW(G)
print(Kruksal(E))