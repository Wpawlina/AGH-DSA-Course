from zad1testy import runtests

def floyd_warshall(M): #znalezc odleglosci miedzy kazdymi dwoma wierzcholkami
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
from queue import Queue
def keep_distance(M,x,y,d): 
    def restore_path(start,end):
        path = []
        i = end
        while i != start:
            path.append(vertices[i])
            i = parent[i]
        path.append(vertices[start])
        path.reverse()
        return path
    #utworzyc graf gdzie wierzcholek to para wierzcholkow o dist < d, a krawedz miedzy u = (a,b), a v = (c,d) istnieje wtw. M[a][c] != -1 i M[b][d] != -1 
    #znalezc sciezke z (x,y) do (y,x): BFSem nawet
    dist = floyd_warshall(M)
    #print(dist)
    N = len(M)
    vertices = []
    for i in range (len(M)):
        M[i][i] = 1 #zeby nie zero, bo potrzebujemy zeby polaczenie z (x,y) do (x,b) moglo istniec
    for a in range (len(M) - 1):
        for b in range (a + 1,len(M)):
            if dist[a][b] >= d:
                vertices.append((a,b))
                vertices.append((b,a)) #trzeba bedzie uwazac, bo nie mozna isc z (x,y) do (y,x) bo wtedy sie mijają na krawedzi
    G = [[] for _ in range (len(vertices))]
    for i1,v1 in enumerate(vertices):
        for i2,v2 in enumerate(vertices):
            if M[v1[0]][v2[0]] != 0 and M[v1[1]][v2[1]] != 0 and not (v1[0] == v2[1] and v2[0] == v1[1]):
                G[i1].append(i2)
                G[i2].append(i1)
    parent = [None]*(len(vertices))
    visited = [False]*(len(vertices))
    q = Queue()
    start_i = vertices.index((x,y))
    q.put(start_i)
    while not q.empty():
        u_i = q.get()
        for v_i in G[u_i]:
            if not visited[v_i]:
                q.put(v_i) 
                visited[v_i] = True
                parent[v_i] = u_i
                if vertices[v_i] == (y,x):
                    end_i = v_i
                    break
    return restore_path(start_i,end_i)

runtests( keep_distance )