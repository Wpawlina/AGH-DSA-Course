from zad8testy import runtests
from math import ceil,sqrt

def Kruksal(E):
   
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

def bulidGraph(A):
    n=len(A)
    E=[]
    for i in range(n):
        for j in range(i+1,n):
            dist=ceil(sqrt(pow(A[i][0]-A[j][0],2)+pow(A[i][1]-A[j][1],2)))
            E.append([i,j,dist])
    return E



def highway( A ):
    E=bulidGraph(A)
    E.sort(key=lambda x:x[2])
    m=len(A)
    n=len(E)
    MST=Kruksal(E)
    
    mind=MST[-1][2]-MST[0][2]
    for i in range(1,n):
        MST=Kruksal(E[i:])
        if len(MST)<m-1:
            break
        mind=min(mind,MST[-1][2]-MST[0][2])
    return mind


    
runtests( highway, all_tests = True)
    