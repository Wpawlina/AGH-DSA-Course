from egzP3btesty import runtests 


def Kruksal(E):
    E.sort(reverse=True,key=lambda x:x[2])
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
    A=[False for _ in range(n)]
    for e in range(n):
        x=find(E[e][0])
        y=find(E[e][1])
        if x!=y:
            union(x,y)
            A[e]=True
    return A
            
    


def NListToEdgeListNDW(G):
    n=len(G)
    E=[]
    for i in range(n):
        for v in G[i]:
            if i<v[0]:
                E.append([i,v[0],v[1]])
    return E




def lufthansa ( G ):
    E=NListToEdgeListNDW(G)
    A=Kruksal(E)
    n=len(E)
    sum=0
    cnt=0
    for i in range(n):
        if not A[i]:
            cnt+=1
            if cnt>1:
                sum+=E[i][2]
    return sum

    


    #
#end procedure lusthansa()

runtests ( lufthansa, all_tests=True )