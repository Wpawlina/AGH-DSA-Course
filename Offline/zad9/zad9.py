from zad9testy import runtests
from queue import Queue

def BFS(G,s):
    Q=Queue()
    n=len(G)
    visted=[False for _ in range(n)]
    dist=[-float('inf') for _ in range(n)]
    visted[s]=True
    dist[s]=0
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
                if dist[v]<dist[u]+1:
                    dist[v]=dist[u]+1
                    Q.put(v)
    return max(dist)+1

def trip2(M):
  n=len(M)
  m=len(M[0])
  G=[[]for _ in range(n*m)]
  for i in range(n):
      for j in range(m):
          t=i*m+j
          if i-1>=0 and M[i-1][j]>M[i][j]:
              t2=(i-1)*m+j
              G[t].append(t2)
          if i+1<n and M[i+1][j]>M[i][j]:
              t2=(i+1)*m+j
              G[t].append(t2)
          if j-1>=0 and M[i][j-1]>M[i][j]:
              t2=i*m+j-1
              G[t].append(t2)
          if j+1<m  and M[i][j+1]>M[i][j]:
              t2=i*m+j+1
              G[t].append(t2)
  res=-float('inf')
  for i in range(n):
      for j in range(m):
          t=i*m+j
          res=max(res,BFS(G,t))
  return res
          

def trip(M):
  n=len(M)
  m=len(M[0])
  F=[[-float('inf')for _ in range(m)] for _ in range(n) ]

  def f(i,j):
      nonlocal F,n,m
      if F[i][j]!=-float('inf'):
          return F[i][j]
      best=-float('inf')
      if i-1>=0 and M[i-1][j]>M[i][j]:
        best=max(best,f(i-1,j)+1) 
      if i+1<n and M[i+1][j]>M[i][j]:
        best=max(best,f(i+1,j)+1)  
          
      if j-1>=0 and M[i][j-1]>M[i][j]:
        best=max(best,f(i,j-1)+1)  
      if j+1<m  and M[i][j+1]>M[i][j]:
        best=max(best,f(i,j+1)+1)
      best=max(best,1)
      F[i][j]=best
      return F[i][j]
          
            
  res=-float('inf') 

  for i in range(n):
      for j in range(m):
          res=max(res,f(i,j))
  
  return res
          
          
          
    
  


              
               
              







# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
