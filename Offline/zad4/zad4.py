#Wojciech Pawlina
#Algorytm porusza sie po grafie przy użyciu DFS zaczynajac od wierchołka x 
#flaga jest uzywana aby okreslic czy jest to pierwsza krawdz na trasie, jesli tak to ustaiane jest elmax oznaczajce najwyzszy optymalny półap na trasie oraz elmin odpoweidnio najniższy optymalny przelot na trasie
# sprawdzanie czy z wierchołka u jest mozliwy przelot do wierchołka v jest realizowane poprzez sprawdzenie czy dana krawedz nie była już wykorzystana na obecnej trasie oraz czy po dodaniu tego wierchołka do trasy napodstawie roznicy miedzy elmax i elmin  bedzie mozliwy do ustalenia półap lotu który spełni warunki 
# algorytm zwraca True kiedy znajdzie sie w odpowiednim wierchołku koncowym, jesli nie beda istniec krawedzie o odpoweidnim pułapie zwróći False

from zad4testy import runtests

def Flight(L,x,y,t):
  n=len(L)
  route=[]
  result=False
  flag=True
  def DFSvisit(L,curV,end,elmin,elmax,flag):
    nonlocal result
    #print(curV)
    if curV==end:
      result=True
    if result==True:
      return
    
    for e in range(n):
      if e not in route and (L[e][0]==curV or L[e][1]==curV): 
        if flag:
          elmax=L[e][2]
          elmin=L[e][2] 
        else:
          if L[e][2]>elmax:
            if(L[e][2]-elmin>2*t):
              continue
          if L[e][2]<elmin:
            if(elmax-L[e][2]>2*t):
              continue
        route.append(e)
        if L[e][0]==curV:
          if L[e][2]>elmax:
              DFSvisit(L,L[e][1],end,elmin,L[e][2],False)
          elif L[e][2]<elmin:
              DFSvisit(L,L[e][1],end,L[e][2],elmax,False)
          else:
              DFSvisit(L,L[e][1],end,elmin,elmax,False)
        else:
          if L[e][2]>elmax:
            DFSvisit(L,L[e][0],end,elmin,L[e][2],False)
          elif L[e][2]<elmin:
            DFSvisit(L,L[e][0],end,L[e][2],elmax,False)
          else:
            DFSvisit(L,L[e][0],end,elmin,elmax,False)
        del route[-1]
          
    
  DFSvisit(L,x,y,None,None,flag)  
  return result
        
 



L=[(0,1,2000),(0,2,2000),(1,3,2030),(2,3,2000),(3,4,2000),(4,5,2030),(4,6,2000),(5,6,2000),(5,7,2000),(7,8,1970)]
#print(Flight(L,0,8,20))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True)


