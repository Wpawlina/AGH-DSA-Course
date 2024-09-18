from kol1atesty import runtests



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

def findBinFirst(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s]<el:
            p=s+1
        else:
            k=s-1
    if p<len(tab) and el==tab[p]:
        return p
    return -1

def findBinLast(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s]>el:
            k=s-1
        else:
            p=s+1
    if k>=0 and tab[k]==el:
        return k
    return -1




    



def g(T):
    n=len(T)
    maxP=0
    radixSort(T)
    #print(T)
    i=0
    while i<n:
        f=findBinLast(T,T[i])
        rev=T[i][::-1]
        curP=f-i+1
        if rev!=T[i]:
            s=findBinFirst(T,rev)
            f2=findBinLast(T,rev)
            if s!=-1 and f2!=-1:
                curP+=f2-s+1
        if curP>maxP:
            print(T[i])
            maxP=curP
        i=f+1
    return maxP
       

    

    
#T=['pies', 'mysz', 'kot', 'kogut', 'tok', 'seip', 'kot']
#print(g(T))
   
  



#Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True)

