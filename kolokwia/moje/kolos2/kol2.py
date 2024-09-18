# Wojciech Pawlina
# Algorytm wykorzystuje zmodyfikowany algorytm bfs oparty o kolejke queue. Kazdy wierzcholek posiada swoja tablice dystansów w której kazdy indeks odpowiada najkrótszemu czasowi dotarcia do wierzchołka z pozostalym czsem do wypoczynku.
# Po dotarciu do  wiercholka poprzez relaksacje krawędzi sprawdza czy da sie dotrzec w krótszym czasie i okreslonych pozostalych godzinach do wypoczynku do innego wierzchołka.
# Algorytm sprawdza obie mozliwe opcje jesli magiczny wojownik spi w danym schronisku i jeśli nie spi.
# Na koncu zwraca minimalny czas dotarcia do wierzchołka t z dowolna pozostała do wypoczynku ilościa godzin.
# Algorytm jest poprawny ponieważ sprawdza wszytkie możliwości dotarcia do poszczególnych wierzcholków z określona iloscia godzin do wypoczynku i w tablicy dystansow zapisuje najkrótszy czas.
# Algorytm wykorzystuje algorytm bfs a nie algorytm dijkstry dlatego ze itak musimy wielokrotnie wchodzić do wierchołków z powodu 17 mozliwych godzin pozostalych do wypoczynku (od 0 do 16) 
# Zatem skoro rozwiazanie wykorzytuje bfs to jego złożonść to O(V+E)



from kol2testy import runtests
from queue import Queue



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

def warrior( G, s, t):
  G=EdgeListToNlistNDW(G)
  n=len(G)
  dist=[[float('inf') for _ in range(17)] for _ in range(n)]
  Q=Queue()
  value=16
  dist[s][value]=0
  Q.put((s,value))
  while not Q.empty():
      u,value=Q.get()
      for v in G[u]:
          if v[1]<=value:
              if dist[v[0]][value-v[1]]>dist[u][value]+v[1]:
                  dist[v[0]][value-v[1]]=dist[u][value]+v[1]
                  Q.put((v[0],value-v[1]))
      if u!=s:
        prevValue=value
        value = 16
        for v in G[u]:
            if dist[v[0]][value-v[1]]>dist[u][prevValue]+v[1]+8:
                dist[v[0]][value-v[1]]=dist[u][prevValue]+v[1]+8
                Q.put((v[0],value-v[1]))
  return min(dist[t])
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests =True )
