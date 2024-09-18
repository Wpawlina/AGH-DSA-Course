from kolutesty import runtests

def countingSort(T,k):
    n=len(T)
    C=[0]*k
    B=[None]*n
    for element in T:
        C[element]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[T[i]]-1]=T[i]
        C[T[i]]-=1
    for i in range(n):
        T[i]=B[i]




def ice_cream( T ):
    n=len(T)
    result=0
    d=0
    C=[0]*(n+1)
    
    for element in T:
        if element>n:
            result=result+element-d
            d+=1
        else:
             C[element]+=1
    for i in range(1,n+1):
        C[i]+=C[i-1]
    B=[None]*(n-d)
    for i in range(n-1,-1,-1):
        if T[i]<=n:
            B[C[T[i]]-1]=T[i]
            C[T[i]]-=1
   
    for i in range(len(B)-1,-1,-1):
        if B[i]-d>0:
            result=result+B[i]-d
            d+=1
        else:
            break
    return result


    

       


    



    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
