def countingSortLength(T,k):
    n=len(T)
    C=[0]*k
    B=[None]*n
    for element in T:
        C[len(element)]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[len(T[i])]-1]=T[i]
        C[len(T[i])]-=1
    for i in range(n):
        T[i]=B[i]
def countingSortLetters(T,k,L,P,kol):
    C=[0]*k
    B=[None]*(P-L+1)
    for element in T[L:P+1]:
        C[ord(element[kol])-97]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(P,L-1,-1):
        B[C[ord(T[i][kol])-97]-1]=T[i]
        C[ord(T[i][kol])-97]-=1
    for i in range(0,P-L+1):
        T[i+L]=B[i]



def radixSort(T):
    n=len(T)
    maxl=0
    for word in T:
        if maxl<len(word):
            maxl=len(word)
    countingSortLength(T,maxl+1)
    flag=True
    for i in range(maxl-1,-1,-1):
        L=0
        if flag:
            for j in range(n-1,-1,-1):
                if len(T[j])-1<i:
                    L=j+1
                    break
        if L==0:
            flag=False
        countingSortLetters(T,26,L,n-1,i)
       
    






T=['krak','kasza','basia','masia','dupa','dlugie','najdluzsze','kk','ara']
radixSort(T)
print(T)