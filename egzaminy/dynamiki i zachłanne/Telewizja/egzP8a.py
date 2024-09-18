from egzP8atesty import runtests 
from bisect import bisect_right

def overlap(T,i,j):
    return T[i][0]<=T[j][1] and T[j][0]<=T[i][1]
      


def reklamy ( T, S, o ):
    n=len(T)
    P=[(T[i][0],T[i][1],S[i]) for i in range(n)]
    P.sort()
    F=[-1 for i in range(n)]
    F[n-1]=P[n-1][2]
    for i in range(n-2,-1,-1):
        F[i]=max(P[i][2],F[i+1])
    I=[P[i][0] for i in range(n)]
    res=0
    
    for i in range(n):
        x=bisect_right(I,P[i][1],lo=i+1)
        second=0
        if x<n and I[x]!=P[i][1]:
            second=F[x]
        res=max(res,P[i][2]+second)
    return res


    
            
  



            

   

runtests ( reklamy, all_tests=True )