from egz1atesty import runtests



def snow( S ):
    n=len(S)
    result=0
    d=0
    C=[0]*(n+1)
    
    for element in S:
        if element>n:
            result=result+element-d
            d+=1
        else:
             C[element]+=1
    for i in range(1,n+1):
        C[i]+=C[i-1]
    B=[None]*(n-d)
    for i in range(n-1,-1,-1):
        if S[i]<=n:
            B[C[S[i]]-1]=S[i]
            C[S[i]]-=1
   
    for i in range(len(B)-1,-1,-1):
        if B[i]-d>0:
            result=result+B[i]-d
            d+=1
        else:
            break
    return result
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
