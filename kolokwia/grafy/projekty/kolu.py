from kolutesty import runtests
def SortTopology(G):
    def DFSvisit(G,u):
        nonlocal visted,sortedT
        visted[u]=True
        for v in G[u]:
            if not visted[v]:
                DFSvisit(G,v)
        sortedT.append(u)
        
        
    n=len(G)
    visted=[False for _  in range(n)]
    sortedT=[]
    for i in range(n):
        if not visted[i]:
            DFSvisit(G,i)
    sortedT.reverse()
    return sortedT

def projects(n, L):
    G=[[] for _ in range(n)]
    for edge in L:
        G[edge[1]].append(edge[0])
    lista=SortTopology(G)
    
   
    cycle=[1 for _ in range(n)]
    for i in range(n):
        for v in G[lista[i]]:
            cycle[v]=max(cycle[v],cycle[lista[i]]+1)
    return max(cycle)
        
      
            
            
        
        
        

    
 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
