import math


def generate_cities(C):
    n=len(C)
    C.sort(key=lambda x: x[1])
    M=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            dist=math.sqrt(pow(C[i][1]-C[j][1],2)+pow(C[i][2]-C[j][2],2))
            M[i][j]=dist
            M[j][i]=dist
    return M


def bitonicTSP(C):
    M=generate_cities(C)
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





C = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2],["Kraków", 2, 1], ["Szczecin", 7, 3], ["Rzeszów", 0.5, 4]]
print(bitonicTSP(C))

C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
print(bitonicTSP(C))

C = [['A', 0, 2],['B', 1, 1],['C', 3, 2],['D', 6, 0],['E', 9, 0],['F', 8, 5],['G', 5, 5],['H', 2, 4],['I', 7, 0]]
print(bitonicTSP(C))

C = [['A', 0, 6],['B', 1, 0],['C', 6, 1],['D', 8, 2],['E', 7, 5],['F', 5, 4],['G', 2, 3]]
print(bitonicTSP(C))

C = [["Paprykarz-Szczeciński", 1, 3], ["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
print(bitonicTSP(C))

C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],['I', 0.5, 2.5], ['J', 1.5, 3.5]]
print(bitonicTSP(C))

C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
print(bitonicTSP(C))

C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
print(bitonicTSP(C))
