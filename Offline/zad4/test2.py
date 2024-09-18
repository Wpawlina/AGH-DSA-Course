#Wojciech Pawlina
#Algorytm porusza sie po grafie przy użyciu DFS zaczynajac od wierchołka x 
#flaga jest uzywana aby okreslic czy jest to pierwsza krawdz na trasie, jesli tak to ustaiane jest elmax oznaczajce najwyzszy optymalny półap na trasie oraz elmin odpoweidnio najniższy optymalny przelot na trasie
# sprawdzanie czy z wierchołka u jest mozliwy przelot do wierchołka v jest realizowane poprzez sprawdzenie czy dana krawedz nie była już wykorzystana na obecnej trasie oraz czy po dodaniu tego wierchołka do trasy napodstawie roznicy miedzy elmax i elmin  bedzie mozliwy do ustalenia półap lotu który spełni warunki 
# algorytm zwraca True kiedy znajdzie sie w odpowiednim wierchołku koncowym, jesli nie beda istniec krawedzie o odpoweidnim pułapie zwróći False

from zad4testy import runtests



def Flight(L,x,y,t):
  n=len(L)
  def DFSvisit(L,curV,end):
    nonlocal result
    n=len(L)
    #print(curV)
    if curV==end:
      result=True
    if result==True:
      return
    for e in range(n):
        if L[e][0]==curV and not visted[L[e][1]]:
            visted[L[e][1]]=True
            DFSvisit(L,L[e][1],y)
        if L[e][1]==curV and not visted[L[e][0]]:
            visted[L[e][0]]=True
            DFSvisit(L,L[e][0],y)
  
  m=max(L,key=lambda x: x[1])
  m=m[1]
  L2=sorted(L,key=lambda x : x[2])
  i=0
  j=0
  while j<n:
    dif=L2[j][2]-L2[i][2]
    visted=[False]*(m+1)
    visted[x]=True
    result=False
    if dif<=2*t:
      DFSvisit(L2[i:j+1],x,y)
      if result:
        return True
      j+=1
    else:
      i+=1  
  return False     

 
        
        
 



#L=[(0,1,2000),(0,2,2000),(1,3,2030),(2,3,2000),(3,4,2000),(4,5,2030),(4,6,2000),(5,6,2000),(5,7,2000),(7,8,1970)]
#print(Flight(L,0,8,20))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True)


