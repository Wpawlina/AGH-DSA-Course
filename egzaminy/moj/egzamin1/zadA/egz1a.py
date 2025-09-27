#Wojciech Pawlina 
#Algorytm najpierw konwertuje graf do postaci listy sasiedztwa nastepnie wykorzystujac algorytm disjkstry puszczony z wierchołka s znajduje najkrótsze siciezki
# do kazdego z rowerów o raz wierchołka t. Poczatkowo zapisuje dlugosci najkrótszej sciezki t jako minimalna odległośc
# nastepnie puszcza ponownie dijkstre tym razem z wierchołka t aby znalesc najkrótsze sciezki od rowerów do t
# nastepnie wykorzytujac tablice dystansów uzyskne z uzycia dwukrotnie algorytmu dijkstry ( jedna z s druga t) dla kazdego wierzcholka z rowerem
#obliczam suma czasu potrzebnego do dostanie sie do roweru z wiercholka s i sume czasu do dostanie sie od roweru do wierchołka t przemnozonej prze p/q odpowiednie dla danego roweru
# wynikiem jest minimum z wziecia któregos roweru i nie brania roweru
# algorytm dwukrotnie uzywa algorytmu dijkstry o złozonosci O(ElogV) i raz liniowo przechodzi po wszytkich rowerach O(V)
# zatem zlozonosc calego algorytmu to O(ElogV)




from egz1atesty import runtests
from queue import PriorityQueue
from math import floor



def EdgeListToNlistNDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append([e[1],e[2]])
        G[e[1]].append([e[0],e[2]])
    return G

def Dijkstra(G,s):
  
    n=len(G)
    distance=[float('inf') for _ in range(n)]
    visted=[False for _ in range(n)]
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        if not visted[u[1]]:
            visted[u[1]]=True
            for v in G[u[1]]:
                if distance[v[0]]> distance[u[1]]+v[1]:
                    distance[v[0]]=distance[u[1]]+v[1]
                    Q.put((distance[v[0]],v[0]))
    return distance

def armstrong( B, G, s, t):
  G=EdgeListToNlistNDW(G)
  distInit=Dijkstra(G,s)
  res=distInit[t]
  distBike=Dijkstra(G,t)

  for b in B:
    suma=distInit[b[0]]+(b[1]/b[2])*distBike[b[0]]
    if suma < float('inf'):
      res=min(res,floor(suma))
  return res
  
  
  


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True)
