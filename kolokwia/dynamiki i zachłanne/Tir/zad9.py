import sys
from math import inf
from zad9testy import runtests

sys.setrecursionlimit(6000000)

def min_cost( O, C, T, L ):
    M=[(0,0),(L,0)]
    n=len(O)
    for i in range(n):
        M.append((O[i],C[i]))
    M.sort()
    m=len(M)
    F=[[-1,-1]for _ in range(m)]
    F[0][0]=0
    F[0][1]=0
    def f(i,flag):
        nonlocal F
        if F[i][flag]!=-1:
            return F[i][flag]
        pos=M[i][0]
        best=float('inf')
        if  flag==0:
            for j in range(i-1,-1,-1):
                dist=pos-M[j][0]
                if dist>T:
                    break
                best=min(best,f(j,0)+M[j][1])
            F[i][0]=best
            return best
        else:
            for j in range(i-1,-1,-1):
                dist=pos-M[j][0]
                if dist <=T:
                    best=min(best,f(j,1)+M[j][1])
                elif dist<=2*T:
                    best=min(best,f(j,0)+M[j][1])
                else:
                    break
            F[i][1]=best
            return best
    f(m-1,0)
    f(m-1,1)
    return min(F[m-1])

def min_cost2( O, C, T, L ):
    M=[(0,0),(L,0)]
    n=len(O)
    for i in range(n):
        M.append((O[i],C[i]))
    M.sort()
    m=len(M)
    F=[[float('inf'),float('inf')]for _ in range(m)]
    F[0][0]=0
    F[0][1]=0
    posT=0
    pos2T=0
    while pos2T<=m:
        minPosT=posT+1
        minPos2T=pos2T+1
        for i in range(posT+1,m):
            dist=M[i][0]-M[posT][0]
            if dist>T:
                break
            F[i][0]=min(F[i][0],F[posT][0]+M[i][1])
            if F[i][0]<F[minPosT][0]:
                minPosT=i
        for i in range(posT+1,m):
            dist=M[i][0]-M[posT][0]
            if dist>2*T:
                break
            F[i][1]=min(F[i][1],F[posT][0]+M[i][1])
        for i in range(pos2T+1,m):
            dist=M[i][0]-M[pos2T][0]
            if dist>T:
                break
            F[i][1]=min(F[i][1],F[pos2T][1]+M[i][1])
            if F[i][1]<F[minPos2T][1]:
                minPos2T=i
        posT=minPosT
        pos2T=minPos2T
                    
    return F[m-1][1]




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests =True)
