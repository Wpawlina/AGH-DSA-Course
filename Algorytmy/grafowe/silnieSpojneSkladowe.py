def DFS(G):
    def DFSvisit(G,u):
        nonlocal visted,times,time
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                DFSvisit(G,v)
        time+=1
        times.append((u,time))
    def DFSvisitReversed(G,u):
        nonlocal visted,cycle
        visted[u]=True
        cycle.append(u)
        for v in G[u]:
            if not visted[v]:
                DFSvisitReversed(G,v)
    n=len(G)
    visted=[False for _  in range(n)]
    time=0
    times=[]
    for i in range(n):
        if not visted[i]:
            DFSvisit(G,i)
    visted=[False for _  in range(n)]
    times.sort(reverse=True,key=lambda x:x[1])
    G2=[[]for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            G2[G[i][j]].append(i)
    visted=[False for _  in range(n)]
    cycles=[]
    for i in range(n):
        if not visted[i]:
            cycle=[]
            DFSvisitReversed(G2,times[i][0])
            cycles.append(cycle)
    return cycles
    


        


G=[[1,7],[2],[0,3],[4],[6,8],[3],[5,9],[9],[7,10],[8],[9]]
print(DFS(G))