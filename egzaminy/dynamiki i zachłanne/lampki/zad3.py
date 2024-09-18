from zad3testy import runtests
from math import inf

# zielony 0  czerwony 1 niebieski 2

def lamps( n,T ):
    maxV=-1
    cnt=0
    L=[0]*n
    for a,b in T:
        for i in range(a,b+1):
            if L[i]==2:
                cnt-=1
            L[i]=(L[i]+1)%3
            if L[i]==2:
                cnt+=1
        maxV=max(maxV,cnt)
    return maxV
            


    

    
runtests( lamps )