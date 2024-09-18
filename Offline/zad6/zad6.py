#Wojciech Pawlina
#Algoytm wykorzytuje zmodyfikowny algorytm dijkstry. Dla kazdego wierzchołka zapisuje on 2 odleglosci od wierzchołka s piewrsza w przypadku kiedy do wierzchołka wszedł poprzez zwyczajny sposób i druga w przypadku uzycia dwu milowych butów.
#Przechodzac algorytmem dijkstry po grafie algorytm dla kazdego wierzchołka sprawdza wszytkie mozliwe przejscia do innych wierzchołkow w sposób zwyczajny i w dwumilowych butach o ile wszedl poprzednio do danego wierzcholka w sposób zwyczajny oraz zapisuje najkrotsza sciezke dla kazdego z tych wiercholków do których wejdzie dowonlny sposób poprzez relaksacje krawedzi
# na koncu zwraca najkrotsza odleglosc z dwoch sciezek wiadacych do koncowego wierchołka
# algorytm ma złozonsc gorsza niz algorytm dijkstry poniewaz do kazedego wierchołka wchodzi on co najmnje 2 razy.


from zad6testy import runtests
from queue import PriorityQueue

def jumper( G, s, w ):
    n=len(G)
    dist1=[ float('inf') for _ in range(n)]#odleglosc do wierchołka wchodzac do niego w normalny sposob 
    dist2=[ float('inf') for _ in range(n)]#odleglosc do wierchołka wchodzac do niego w dwumilowych butach
    visted1=[False for _ in range(n)]
    visted2=[False for _ in range(n)]
    dist1[s]=0
    dist2[s]=0
    Q=PriorityQueue()
    Q.put((0,[s,False]))# flaga false oznacza ze nie wszlismy do wierzchołka w dwumilowych butach
    while not Q.empty():
        u=Q.get()[1]
        flag=u[1]
        u=u[0]
        
        #przechodzenie w dwumilowych butach
        if not flag and not visted1[u]:
            visted1[u]=True
            for i in range(n):
                if G[u][i]!=0:
                    for j in range(n):
                        if G[i][j]!=0:
                            if  dist2[j]>dist1[u]+max(G[i][j],G[u][i]):
                                dist2[j]=dist1[u]+max(G[i][j],G[u][i])
                                Q.put((dist2[j],[j,True]))

            #przechodzenie w sposób zwyczajny
            for i in range(n):
                if G[u][i]!=0:
                    if dist1[i]> dist1[u]+ G[u][i]:
                        dist1[i]=dist1[u] + G[u][i]
                        Q.put((dist1[i],[i,False]))

        if flag and not visted2[u]:
            visted2[u]=True
            #przechodzenie w sposób zwyczajny
            for i in range(n):
                if G[u][i]!=0:
                    if dist1[i]> dist2[u]+ G[u][i]:
                        dist1[i]=dist2[u] + G[u][i]
                        Q.put((dist1[i],[i,False]))  

    return min(dist1[w],dist2[w])
    
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )