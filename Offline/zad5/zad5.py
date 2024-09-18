#Wojciech Pawlina 
# algorytm wykorzystuje zmodyfikowany algorytm dijkstry, który dodatkowo łaczy wszytkie planety wokół który znajduja sie osobliwosci krawedzia o wadze 0
# w ten sposób wyszukjuje on najkrótszą scieżkę  z a do b w układzie i zwraca czas jej przebycia  
 

from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    m=len(E)



    visted=[False for _ in range(n)]
    dist=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    dist[a]=0
    parent[a]=a
    Q=PriorityQueue()
    Q.put((0,a))
    while not Q.empty():
        u=Q.get()[1]
        if not visted[u]:
            visted[u]=True
            for i in range(m):
                if u==E[i][0]:
                    v=E[i][1]
                    if dist[v]> dist[u]+E[i][2]:
                        dist[v]=dist[u]+E[i][2]
                        parent[v]=u
                        Q.put((dist[v],v))
                if u==E[i][1]:
                    v=E[i][0]
                    if dist[v] > dist[u]+E[i][2]:
                        dist[v]=dist[u]+E[i][2]
                        parent[v]=u
                        Q.put((dist[v],v))
            if u in S:
                for v in S:
                    if dist[v]>dist[u]:
                        dist[v]=dist[u]
                        parent[v]=u
                        Q.put((dist[v],v))
        
   
    return dist[b] if dist[b]<float('inf') else None

                








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )