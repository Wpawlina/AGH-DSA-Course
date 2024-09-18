from egz2atesty import runtests
import heapq



def coal(A, T):
    n=len(A)
    for i in range(n):
        A[i]=(i,A[i])
    M=[(i,T) for i in range(n)]
    last=-1
  
    heapq.heapify(M)
    for weight in A:
        while M[0][2]<weight:
            heapq.heappop(M)
        indeks,capacity=heapq.heappop(M)
        print(indeks,capacity,weight)
        last=indeks
        heapq.heappush(M,(indeks,cnt,capacity-weight))
        cnt-=1
    return last




   
    
    
  
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
