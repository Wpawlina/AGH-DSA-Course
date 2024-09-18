#Wojciech Pawlina
# algorytm przechodzi po kazdym elemencie tablicy T i dla kazdego zlicza ile elementów znajdujacych sie w tablicy przednim jest mniejsze od niego
# zlicza ile jest takich elementow dla kazdego elemntu i zwraca ile takcih elementow posiada element o najwyzszej randzę
# złozonosc obliczeniowa tego algorytmu to O(n^2) poniewaz dla kazdego elementu sprawdza wszytkie elementy które znajduja sie przed nim w tablicy
# zlozonsc pamiecowa to O(n) poniewaz uwzywa tylko tablicy która jst do funkcji przekazana

from kol1testy import runtests

def maxrank(T):
  n=len(T)
  maxrank=-1
  ranks=[0]*n
  for i in range(1,n):
    currank=0
    for j in range(i-1,-1,-1):# sprawdzanie elementów znajdujacych sie przed sprawdzanym elementem 
      if T[j]<T[i]:
        currank+=1
      if T[j]>T[i] and ranks[j]>=maxrank:
          break
    if currank>maxrank: #znajdowanie najwyzszej rangi
        maxrank=currank
        
  return maxrank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
