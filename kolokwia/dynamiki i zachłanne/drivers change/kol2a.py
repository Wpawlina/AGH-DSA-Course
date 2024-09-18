from kol2atesty import runtests
#jacek 0 marian 1 
def drivers( P, B ):
    n=len(P)
    for i in range(n):
        P[i]=(P[i][0],P[i][1],i)
    P.append((0,True,-1))
    P.sort()
    n=len(P)
  
    for i in range(n-1,-1,-1):
        if P[i][0]>B:
            P.pop()
    P.append((B,True,-1))
    n=len(P)
    F=[[float('inf ')for _ in range(2)]for _ in range(n)]
    Parent=[[ None for _ in range(2)]for _ in range(n)]
    F[0][0]=0
    k=1
    dist=0
    while k<n and dist < 3:
        if P[k][1]:
            dist+=1
            if F[k][1]>0:
                F[k][1]=0
                Parent[k][1]=None
        k+=1


    for i in range(1,n):
        for driver in range(2):
                if P[i][1] and  F[i][driver]!=float('inf'):
                    new_driver=(driver+1)%2
                    k=i+1
                    dist=0
                    cnt=F[i][driver]
                    while k<n and dist < 3:
                        if P[k][0]==B:
                            if F[k][driver]>cnt:
                                    F[k][driver]=cnt
                                    Parent[k][driver]=(i,driver)
                            break
                        else:
                            if P[k][1]:
                                dist+=1
                                if F[k][new_driver]>cnt:
                                    F[k][new_driver]=cnt
                                    Parent[k][new_driver]=(i,driver)
                            if not P[k][1] and driver==1:
                                cnt+=1
                        k+=1
    minv=float('inf')
    mini=-1
    for i in range(2):
            if F[n-1][i]<minv:
                minv=F[n-1][i]
                mini=(n-1,i)
    res=[]
   
    p=Parent[mini[0]][mini[1]]
    while p is not None:
        
        res.append(P[p[0]][2])
        p=Parent[p[0]][p[1]]
    res.reverse()
    return res

c=False
p=True
P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
(2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]
B = 20
print(drivers(P,B))


    
  
    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True)