from kol3testy import runtests
from math import inf

def orchard(T, m):
    total_sum=sum(T)
    if total_sum%m==0:
        return 0
    n=len(T)
    F=[[[False for _ in range(m)]for _ in range(n+1)]for _ in range(n)]
    start=T[0]%m
    F[0][0][start]=True
    
    for i in range(n):
        for k in range(n+1):
            if k==i:
                F[i][k][T[i]%m]=True
            if k>i:
                F[i][k][0]=True

    
    
    
    for i in range(1,n):
        for k in range(n+1):
            cur_mod=T[i]%m
            if k>i:
                continue
            for mod in range(m):
                if F[i][k][mod]==True:
                    continue
                if F[i-1][k][((m - cur_mod)%m+mod)%m]:
                    F[i][k][mod]=True
                if k-1>=0 and  F[i-1][k-1][mod]:
                    F[i][k][mod]=True

            
                    
   
    for k in range(n):
        if F[n-1][k][0]:
            return k
        

def orchard(T,m):
    n=len(T)
    dp=[-float('inf')]*m
    dp2=[-float('inf')]*m
    dp[0]=0
    dp[T[0]%m]=1
    for i in range(1,n):
        cur_mod=T[i]%m
        for mod in range(m):
            dp2[mod]=max(dp[mod],dp[((m - cur_mod)%m+mod)%m]+1)
        dp,dp2=dp2,dp
    return n-dp[0]



            
            
    
                
T=[2,2,7,5,1,14,7]  
m=7
print(orchard(T,m))     
        
        

    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
