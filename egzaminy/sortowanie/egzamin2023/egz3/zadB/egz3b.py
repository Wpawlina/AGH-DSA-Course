from egz3btesty import runtests

def findBinFirst(tab,el,indeks):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s][indeks]<el:
            p=s+1
        else:
            k=s-1
    if p<len(tab) and el==tab[p][indeks]:
        return p
    return -1
def find(T,x):
    n=len(T)
    i=-1
    k=-1
    for j in range(n):
        if T[j]==x:
            i=j
        elif  (T[j][0]<x[0] and x[0]<T[j][1]<x[1]) or (x[1]>T[j][0]>x[0] and T[j][1]>x[1]):
            k=j
        if i>-1 and k>-1:
            return i,k
    return -1,-1
            

def uncool( P ):
    n=len(P)
    pa=sorted(P,key=lambda x:x[0])
    pb=sorted(P,key=lambda x:x[1])
    for i in range(n):
        start=findBinFirst(pa,pa[i][0]+1,0)
        end=findBinFirst(pa,pa[i][1],0)
        sa=end-start
        finA=findBinFirst(pb,pa[i][1]+1,1)
        startB=findBinFirst(pa,pa[i][0]+1,0)
        dom=finA-startB
        dom=dom if dom>=0 else 0
        if sa > dom : 
          #print(pa[i],'p')
          a,b=find(P,pa[i])
          if a>-1 and b>-1:
           return a,b
          
        start=findBinFirst(pa,pa[i][0]+1,1)
        end=findBinFirst(pa,pa[i][1],1)
        sa=end-start
        if sa > dom: 
            #print(pa[i],'k')
            a,b=find(P,pa[i])
            if a>-1 and b>-1:
             
              return a,b
            
    return -1,-1
        

        
  
#P =[ [1,3], [6,7], [2,6], [4,6], [1,8], [5,10] ]
#uncool(P)
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True)
