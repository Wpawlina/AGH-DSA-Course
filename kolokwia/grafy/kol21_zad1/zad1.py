from zad1testy import runtests
from queue import Queue

def FW(M): #znalezc odleglosci miedzy kazdymi dwoma wierzcholkami
    N = len(M)
    S = [[M[i][j] if M[i][j] != 0 else float('inf') for j in range (len(M))] for i in range (len(M))]
    for i in range (len(M)):
        S[i][i] = 0    
    #print(S)
    for k in range (N):
        for x in range (N):
            for y in range (N):
                S[x][y] = min(S[x][y], S[x][k] + S[k][y])
                S[y][x] = S[x][y]
    return S





def keep_distance(M,x,y,d):
    n=len(M)
    S=FW(M)
    lpair=[]
    for i in range(n):
        for j in range(n):
            if S[i][j]>=d:
                lpair.append((i,j))
    allpair=[]
    for i in range(n):
        for j in range(n):
                if i!=j:
                     allpair.append((i,j))
   

    GG=[[[]for _ in range(n)] for _ in range(n)]
    GB=[[[]for _ in range(n)] for _ in range(n)]
    for v in lpair:
         for u in range(n):
              if M[v[0]][u]!=0:
                   GG[v[0]][v[1]].append((u,v[1]))
    for v in allpair:
         for u in range(n):
              if M[v[1]][u]!=0:
                   GB[v[0]][v[1]].append((v[0],u))
    Q=Queue()
    parentG=[[None for _ in range(n)]for _ in range(n)]
    parentB=[[None for _ in range(n)]for _ in range(n)]
    visted=[[False for _ in range(n)]for _ in range(n)]
    Q.put((x,y,True))
    while not Q.empty():
         v,u,flag=Q.get()
         if flag:
              for w in GG[v][u]:
                   if not visted[w[0]][w[1]]:

                        Q.put((w[0],w[1],False))
                        visted[w[0]][w[1]]=True
                        parentB[w[0]][w[1]]=(v,u)
         else:
              for w in GB[v][u]:
                   if not visted[w[0]][w[1]]:
                        Q.put((w[0],w[1],True))
                        visted[w[0]][w[1]]=True
                        parentG[w[0]][w[1]]=(v,u)

    print(parentG,parentB)
    route=[]
    u,w=y,x
    flag=True
    while True:
         print(u,w)
         if flag:
              route.append((u,w))
              print(parentB[u][w])
              flag=False
         else:
              print(parentG[u][w])
              flag=True
         break
         if u==x and w==y and flag:
              break
    route.reverse()
    return route
         
         

    
    
    
                   
    

   
    
         
    


    
    

    

runtests( keep_distance )
    