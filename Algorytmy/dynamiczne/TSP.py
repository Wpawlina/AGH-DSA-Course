
import random
from functools import cache
import time
from queue import Queue


def genMatrixFullGraph(n):

    # Inicjalizacja macierzy sąsiedztwa o wymiarach 15x15 z zerami
    graf_pelny = [[0 for _ in range(n)]for _ in range(n)]

    # Wypełnienie macierzy wagami od 1 do 10 dla krawędzi
    for i in range(n):
        for j in range(i + 1, n):
            waga = random.randint(1, 10)
            graf_pelny[i][j] = waga
            graf_pelny[j][i] = waga
    return graf_pelny







def permutacje(lista):
    # Funkcja pomocnicza do generowania permutacji
    def permutacje_helper(aktualna_permutacja, pozostale_elementy):
        # Jeśli nie ma więcej elementów do przetwarzania, zwróć aktualną permutację
        if not pozostale_elementy:
            aktualna_permutacja.append(0)
            wynik.append(aktualna_permutacja)
            return
        
        # Iteruj przez pozostałe elementy i rekurencyjnie generuj permutacje
        for i in range(len(pozostale_elementy)):
            nowa_permutacja = aktualna_permutacja + [pozostale_elementy[i]]
            nowa_pozostale_elementy = pozostale_elementy[:i] + pozostale_elementy[i+1:]
            permutacje_helper(nowa_permutacja, nowa_pozostale_elementy)
    
    wynik = []
    permutacje_helper([0], lista)
    return wynik

def TSPrekslow(M):
    n=len(M)
    elemnts=[i for i in range(1,n)]
    permutations=permutacje(elemnts)
   # print(permutations)
    mind=float('inf')
    minroute=None
    for perm in permutations:
        curd=0
        for i in range(1,len(perm)):
            curd+=M[perm[i-1]][perm[i]]
        if curd<mind:
            mind=curd
            minroute=perm
    return minroute,mind

def genSubSets(list):
    n=len(list)
    res=[[] for _ in range(n+1) ]
    res[0].append([])
    res[1].append([0])
    res[-1].append(list)
    for i in range(2,n):
        for set in res[i-1]:
            maxI=max(set)+1
            for j in range(maxI,n):
                newset=set[:]
                newset.append(list[j])
                res[i].append(newset)
    return res


def TSPrekFaster(M):
    n = len(M)
    @cache
    def f(S, t):
        if True not in S[1:]:
            return M[0][t]
        mind = float('inf')
        for i in range(1, len(S)):
            if S[i] == True:
                new_S = S[:i] + (False,) + S[i+1:]
                mind = min(mind, f(new_S, i) + M[i][t])
        return mind
    route = tuple(True for _ in range(n))
    mind = float('inf')
    for i in range(1, n):
        new_route = route[:i] + (False,) + route[i+1:]
        mind = min(mind, f(new_route, i) + M[i][0])  
    return mind





def MatrixToNListW(M):
    n=len(M)
    G=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] not in (float('inf'),0):
                G[i].append([j,M[i][j]])
    return G


def TSPbitonic(M):

    n=len(M)
    F=[[float('inf') for _ in range(n)]for _ in range(n)]
    def tspf(i,j):
        nonlocal F,M
        if F[i][j]!=float('inf'):
            return F[i][j]
        if i == j-1:
            best=float('inf')
            for k in range(j-1):
                best=min(best,tspf(k,j-1)+M[k][j])
            F[i][j]=best
        else:
            F[i][j]=tspf(i,j-1)+M[j-1][j]
        return F[i][j]
    best=float('inf')
    for i in range(n-1):
        best=min(best,tspf(i,n-1)+M[i][n-1])
    return best





        
        


             
        
    


            


    
M=[[ 0,  3,  7, 5 , 2 , 9],
 [ 3, 0  ,4 , 8 , 6,  7],
 [ 7,  4  ,0 , 1 , 3,  6],
 [ 5 , 8  ,1 , 0  ,5 , 2],
 [ 2 , 6  ,3  ,5 , 0 , 4],
 [ 9 , 7  ,6,  2,  4,  0]]


M=[[0,7,4,3],
   [7,0,2,9],
   [4,2,0,5],
   [3,9,5,0]]
M=genMatrixFullGraph(10)
M=[[ 0 , 7 , 4 , 3 , 6  ,9, 1 , 8 ,5 , 2],
 [ 7 , 0,  2 , 9,  4 , 6  ,8  ,3  ,1 , 5],
 [ 4 , 2  ,0 , 5 , 8 , 7  ,3  ,6,  9,  1],
 [ 3  ,9  ,5  ,0  ,1  ,4 , 7  ,2  ,6 , 8],
 [ 6 , 4 , 8 , 1  ,0,  3 , 5 , 9 , 7 , 2],
 [ 9 , 6 , 7,  4 , 3,  0,  2,  1 , 8,  5],
 [ 1 , 8 , 3 , 7 , 5 , 2  ,0 , 4,  6 , 9],
 [ 8,  3 , 6 , 2,  9  ,1 , 4 , 0,  5 , 7],
 [ 5 , 1  ,9 , 6  ,7  ,8 , 6,  5  ,0 , 4],
 [ 2 , 5 , 1  ,8  ,2,  5,  9  ,7 , 4 , 0]]


for i in range(len(M)):
    M[i]=tuple(M[i])


M=tuple(M)



start_time = time.time()

print(TSPrekFaster(M))

# Pobranie czasu po wykonaniu kodu
end_time = time.time()

# Obliczenie czasu wykonania
execution_time = end_time - start_time

print("Czas wykonania Faster: ", execution_time, "sekundy")




start_time = time.time()

print(TSPrekslow(M))

# Pobranie czasu po wykonaniu kodu
end_time = time.time()

# Obliczenie czasu wykonania
execution_time = end_time - start_time

print("Czas wykonania Slow: ", execution_time, "sekundy")







