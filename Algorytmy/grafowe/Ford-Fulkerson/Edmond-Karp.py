from queue import Queue
def bfs(M,s,t,parent):
    n=len(M)
    visted=[False for _ in range(n)]
    Q=Queue()
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in range(n):
            if not visted[v]:
                if M[u][v]>=1:
                    Q.put(v)
                    visted[v]=True
                    parent[v]=u
    return  visted[t] 




def EK(M,s,t):
    n=len(M)
    parent=[-1]*n
    res=0
    while bfs(M,s,t,parent):
        flow=float('inf')
        v=t
        while v!=s:
            flow=min(flow,M[parent[v]][v])
           
            v=parent[v]
        res+=flow
        v=t
        while v!=s:
            u=parent[v]
            M[u][v]-=flow
            M[v][u]+=flow
            v=u
    return res

        
            
M=[ [0,4,3,0,0,0],
    [0,0,2,2,0,0],
    [0,0,0,2,2,0],
    [0,0,0,0,0,4],
    [0,0,0,0,0,5],
    [0,0,0,0,0,0]

   ]
print(EK(M,0,5))

    

