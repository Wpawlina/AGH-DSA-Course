from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    F=[[float('inf') for _ in range(E+1)]for _ in range(n)]
    for i in range(E+1):
        F[0][i]=i*C[0]
    for i in range(n):
        for e in range(E+1):
            for j in range(i+1,n):
                dist=D[j]-D[i]
                if dist>E:
                    break
                for t in range(E-dist+1):
                    if dist>e:
                        F[j][t]=min(F[j][t],F[i][e]+(dist-e+t)*C[i])
                    else:
                       if e-dist<=t:
                        F[j][t]=min(F[j][t],F[i][e]+(t-(e-dist))*C[i])
                        
            if e==0:
                F[T[i][0]][0]=min(F[T[i][0]][0],F[i][0]+T[i][1])
    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
