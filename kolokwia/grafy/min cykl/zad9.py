from copy import deepcopy
from queue import PriorityQueue


def Dijkstra(G,s):
    n=len(G)
    distance=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    visted=[False for _ in range(n)]
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        if not visted[u[1]]:
            visted[u[1]]=True
            for v in range(n):
                if G[u[1]][v]!=-1:
                    if distance[v]> distance[u[1]]+G[u[1]][v]:
                        distance[v]=distance[u[1]]+G[u[1]][v]
                        parent[v]=u[1]
                        Q.put((distance[v],v))
    return parent,distance


def restoreCycle(parent,k):
    cycle=[]
    cycle.append(k)
    u=parent[k]
    while u is not None:
        cycle.append(u)
        u=parent[u]
    return cycle

def min_cycle(G):
    n=len(G)
    mind=float('inf')
    minc=[]
    for i in range(n):
        for j in range(i+1,n):
            if G[i][j]!=-1:
                temp=G[i][j]
                G[i][j]=-1
                G[j][i]=-1
                parent,dist=Dijkstra(G,i)
                if mind> dist[j]+temp:
                    mind=dist[j]+temp
                    minc=restoreCycle(parent,j)
                G[i][j]=temp
                G[j][i]=temp
    return minc
            
            

   

   
#end procedure min_cycle()


G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7


GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)


if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")


G = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]

LEN = 5
print( min_cycle(G) )

G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
     [4, -1, 8, -1, -1, -1, -1, 11, -1],
     [-1, 8, -1, 7, -1, 4, -1, -1, 2],
     [-1, -1, 7, -1, 9, 14, -1, -1, -1],
     [-1, -1, -1, 9, -1, 10, -1, -1, -1],
     [-1, -1, 4, 14, 10, -1, 2, -1, -1],
     [-1, -1, -1, -1, -1, 2, -1, 1, 6],
     [8, 11, -1, -1, -1, -1, 1, -1, 7],
     [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
LEN = 14

print( min_cycle(G) )


def undirected_weighted_graph_matrix(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[-1] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
        G[e[1]][e[0]] = e[2]
    return G
	
	
E = [(0, 1, 3), (1, 2, 2), (0, 6, 2), (6, 7, 1), (6, 5, 3), (5, 7, 1),
    (5, 4, 8), (3, 4, 20), (8, 7, 7), (8, 1, 1), (2, 3, 5), (3, 8, 1),
    (7, 4, 2)]
LEN = 5
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )

E = [(0, 1, 9), (1, 2, 18), (2, 3, 15), (3, 4, 20), (4, 5, 5), (5, 6, 5), (6, 7, 7), (7, 8, 10), (8, 9, 8),
     (0, 15, 10), (1, 15, 4), (1, 14, 5), (15, 14, 4), (14, 3, 10), (15, 13, 6), (13, 14, 5), (16, 15, 6),
     (16, 13, 2), (18, 17, 2), (17, 16, 3), (16, 12, 5), (12, 13, 4), (13, 11, 10), (11, 10, 4),
     (12, 10, 12), (10, 5, 10), (11, 4, 6)]
LEN = 11
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )

E = [(0, 1, 17), (1, 2, 30), (2, 3, 2), (3, 4, 47), (4, 5, 88), (5, 6, 0), (7, 6, 3), (7, 8, 7), (8, 9, 0), (9, 10, 12),
     (10, 11, 40), (11, 0, 13), (11, 14, 1), (14, 12, 7), (12, 13, 18), (13, 1, 120), (3, 16, 81), (16, 15, 63),
     (15, 17, 90), (17, 5, 37), (11, 23, 0), (23, 22, 67), (22, 21, 73), (21, 24, 11), (24, 23, 2), (21, 20, 18),
     (20, 19, 96), (19, 18, 50), (18, 29, 4), (29, 20, 22), (18, 5, 1), (21, 25, 97), (25, 26, 26), (26, 27, 30),
     (27, 28, 8), (28, 20, 11), (26, 30, 100), (30, 27, 52), (30, 31, 1), (31, 32, 20), (31, 33, 0), (34, 26, 4),
     (35, 26, 3), (36, 26, 2), (27, 37, 10), (27, 38, 8), (27, 39, 1)]
LEN = 120
G =  undirected_weighted_graph_matrix(E)
print( min_cycle(G) )