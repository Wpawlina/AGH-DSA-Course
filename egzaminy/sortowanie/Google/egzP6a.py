from egzP6atesty import runtests 


def countingSort(T,k,kol):
    n=len(T)
    C=[0]*k
    B=[None]*n
    for element in T:
        C[element[kol]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[T[i][kol]]-1]=T[i]
        C[T[i][kol]]-=1
    for i in range(n):
        T[i]=B[i]



def countLetter(string):

    res=0
    for s in string:
        if 97<=ord(s)<=122:
            res+=1
    return res

    



def google ( H, s ):
    n=len(H)
    k=len(max(H,key=lambda x: len(x)))+1
    for i in range(n):
        H[i]=(H[i],len(H[i]),countLetter(H[i]))
    countingSort(H,k,2)
    countingSort(H,k,1)
    H.reverse()
    return H[s-1][0].strip()
  


runtests ( google, all_tests=False )