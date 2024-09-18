from egz3atesty import runtests


def snow( T, I ):
    A=[]
    for a,b in I:
        A.append((a,0))
        A.append((b,1))
    A.sort()
    n=len(A)
    cnt=0
    res=-1
    for i in range(n):
        if A[i][1]==0:
            cnt+=1
        else:
            cnt-=1
        res=max(res,cnt)
    return res

        
   
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True)
