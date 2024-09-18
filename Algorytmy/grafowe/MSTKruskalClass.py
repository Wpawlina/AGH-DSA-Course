class Node:
    def __init__(self,value):
        self.val=value
        self.parent=self
        self.rank=0

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent


def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def Kruksal(E):
  
    n=len(E)
    m=max(E,key=lambda x:x[1])[1]+1
    Nodes=[]
    for i in range(m):
        v=Node(i)
        Nodes.append(v)
    EN=[]
    for e in E:
        EN.append([Nodes[e[0]],Nodes[e[1]],e[2]])
    EN.sort(key=lambda x:x[2])
    A=[]
    for e in EN:
        x=find(e[0])
        y=find(e[1])
        if x!=y:
            A.append([e[0].val,e[1].val,e[2]])
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

        