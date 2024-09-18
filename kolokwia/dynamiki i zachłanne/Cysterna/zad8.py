from zad8testy import runtests
from queue import PriorityQueue

def oil(T,i,O,n,m):
    if T[0][i]==0:
        return 0
    res=0
 
    def f(T,O,k,j):
        nonlocal res
        if  j>m-1 or j<0 or k<0 or k>n-1 or  T[k][j]==0 or O[k][j]==True:
            return 
        O[k][j]=True
        res+=T[k][j]
        f(T,O,k,j-1)
        f(T,O,k,j+1)
        f(T,O,k-1,j)
        f(T,O,k+1,j)
    f(T,O,0,i)
    return res
         
    
   


    
def plan(T):
    n=len(T)
    m=len(T[0])
    O=[[False for _ in range(m)] for _ in range(n)]
    i=0
    cur_oil=0
    res=0
    Q=PriorityQueue()
    while i<m-1:
        Q.put(-1*oil(T,i,O,n,m))
        if cur_oil==0:
            cur_oil=-1*Q.get()
            res+=1
        i+=1
        cur_oil-=1
    return res

        

        


   


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests =True )
