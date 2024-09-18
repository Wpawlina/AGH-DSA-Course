#Wojciech Pawlina 
# algorytm dla kazdego parkingu sprawdza jaka jest najmnejsza suma odleglosci parkingow od biurowców jesli i-ty biurowiec jest przypisany do j-tego parkingu
#wiemy ze jesli rozwazamy i biurowców oraz i parkingów to jest tylko jeden sposób przypsiania parkingów do biurowców zatem dodajac kolejny parking daje nam to jedna nowa mozliwosc przypisania parkingów, 
# sprawdzamy które przypisanie daje mniejsza sume odległosci poprzednie najlepsze  czy jesli przypiszemy poprzedni biurowiec do ostaniego przed dodanym parkigiem
# powtarzamy te operacje aż do ostaniego parkingu
#Skoro trzymamy informacje o  najlepszym pprzypsianiu parkingów dla jednego mniej parkingu to złożonść wynosi O(n*m)


from zad8testy import runtests


def parking(X,Y):
  n=len(X)
  m=len(Y)
  F=[[float('inf')for _ in range(m) ] for _ in range(n) ]
  for i in range(m):
    F[0][i]=abs(X[0]-Y[i])

  for i in range(1,n):
    F[i][i]=F[i-1][i-1]+abs(X[i]-Y[i])
    best=F[i-1][i-1]
    for j in range(i+1,m):
      best=min(best,F[i-1][j-1])
      F[i][j]=best+abs(X[i]-Y[j])
      
  
  return min(F[n-1])
    

     
    



  # tu prosze wpisac wlasna implementacje
X = [3,6,10,14]
Y = [1,4,5,10,11,13,17]
parking(X,Y)
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)
