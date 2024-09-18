from zad1testy import runtests

def lisF(T):
    n=len(T)
    F=[1]*n
    P=[-1]*n
    for k in range(1,n):
        for t in range(k):
            if T[t]>T[k] and F[k]<F[t]+1:
                F[k]=F[t]+1
                P[k]=t
    return F,P

def lisB(T):
    n=len(T)
    F=[1]*n
    P=[-1]*n
    for k in range(n-2,-1,-1):
        for t in range(n-1,k,-1):
            if T[t]>T[k] and F[k]<F[t]+1:
                F[k]=F[t]+1
                P[k]=t
    return F,P

def get_sol1(T,P,k,res):
    if k==-1:return
    if P[k]!=-1:
        get_sol1(T,P,P[k],res)
    res.append(T[k])

def get_sol2(T,P,k,res):
    if k==-1:return
    res.append(T[k])
    if P[k]!=-1:
        get_sol2(T,P,P[k],res)
   

    

def mr( X ):
    LFF,LFP=lisF(X)
    LBF,LBP=lisB(X)
    n=len(X)
    index=-1
    maxV=0
    for i in range(n):
        if maxV<LFF[i]+LBF[i]-1:
            maxV=LFF[i]+LBF[i]-1
            index=i
    res=[]
    get_sol1(X,LFP,LFP[index],res)

    res.append(X[index])
    get_sol2(X,LBP,LBP[index],res)
    
    return res




    
   
 






runtests( mr )