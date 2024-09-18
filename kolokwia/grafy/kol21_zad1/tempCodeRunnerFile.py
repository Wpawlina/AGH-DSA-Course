ef floyd_warshall(M): #znalezc odleglosci miedzy kazdymi dwoma wierzcholkami
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