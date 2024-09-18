import random
import math
from functools import cache


def generate_cities(n, x_range=(0, 100), y_range=(0, 100)):
   
    cities = []
    for _ in range(n):
        x = math.ceil(random.uniform(x_range[0], x_range[1]))
        y = math.ceil(random.uniform(y_range[0], y_range[1]))
        cities.append((x, y))
    cities.sort(key=lambda x:x[0])
    n=len(cities)
    M=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            dist=math.ceil(math.sqrt(pow(cities[i][0]-cities[j][0],2)+pow(cities[i][1]-cities[j][1],2)))
            M[i][j]=dist
            M[j][i]=dist
    return cities,M






def TSPbitonic(M):

    n=len(M)
    F=[[float('inf') for _ in range(n)]for _ in range(n)]
    F[0][0]=0
    F[0][1]=M[0][1]
    F[0][2]=M[0][1]+M[1][2]
    F[1][2]=M[0][1]+M[0][2]
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


cities,M=generate_cities(10)
print(cities)
print(TSPbitonic(M))
print(TSPrekFaster(M))




