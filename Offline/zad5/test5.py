#Wojciech Pawlina 
# algorytm wykorzystuje zmodyfikowany algorytm dijkstry, który dodatkowo łaczy wszytkie planety wokół który znajduja sie osobliwosci krawedzia o wadze 0
# w ten sposób wyszukjuje on najkrótszą scieżkę  z a do b w układzie i zwraca czas jej przebycia  
 

from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    m=len(E)
    sv=S[0]
    for i in range(m):
        E[i]=[E[i][0],E[i][1],E[i][2]]
        if E[i][0] in S:
            E[i][0]=sv
        if E[i][1] in S:
            E[i][1]=sv
    visted=[False for _ in range(n)]
    dist=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]

    if a in S:
        a=sv
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
    for v in S:
        dist[v]=dist[sv]  
    
    
    return dist[b] if dist[b]<float('inf') else None

                








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )