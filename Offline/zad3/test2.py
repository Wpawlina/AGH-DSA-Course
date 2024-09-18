from zad3testy import runtests


def dominance(P):
    maxX=max(P,key=lambda x:x[0])
    maxY=max(P,key=lambda x:x[1])
    maxX=maxX[0]
    maxY=maxY[1]
    X=[0]*(maxX+1)
    Y=[0]*(maxY+1)
    for el in P:
        X[el[0]]+=1
        Y[el[1]]+=1
    for i in range(maxX-1,-1,-1):
        X[i]+=X[i+1]
    for i in range(1,maxY+1):
        Y[i]+=Y[i-1]
    curD=0
    maxD=0
    for el in P:
        curD=Y[el[1]-1]-X[el[0]]+1
        if curD>maxD:
            maxD=curD
    return maxD
            
   
    

        
    

    
  



  # tu prosze wpisac wlasna implementacje
 








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )