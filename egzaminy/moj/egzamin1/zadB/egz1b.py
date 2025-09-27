#Wojciech Pawlina 
#algorytm sprawdza kazdy mozliwy podzbiór tablicy T poprzez wyznaczenie jego poczatku i konca dwoma petlami
#poczatkowa maksymalna suma to suma calego T
#kazdy podzbiór jest sortowany rosnaca i sprawdzana jest jego suma po usunieciu maksymalnie k najmniejszych elementów (usuwanie ma sens tylko jesli elementy sa ujemne) i zapisywane jest maksimum z tych sum
# na koncu algorytm zwraca sume maksymalnego podzbioru po usunieciu do k elementów
# Zlozonsc obliczeniowa tego algorytmu to O(N^3*logN)
from egz1btesty import runtests

def kstrong( T, k):
  n=len(T)
  maxSum=sum(T)
  for i in range(n):
    for j in range(i+1,n):
      curT=T[i:j+1]
      curT.sort()
      cur_sum=sum(curT)
      maxSum=max(maxSum,cur_sum)
      for z in range(min(k,len(curT))):
        if curT[z]>=0:
          break
        cur_sum-=curT[z]
        maxSum=max(maxSum,cur_sum)
  return maxSum

def kstrong(T, k):
    n = len(T)
    if n == 0:
        return 0

    F = [[-float('inf') for _ in range(k+1)] for _ in range(n)]
    F[0][0] = max(0, T[0])  # Initialize with max(0, T[0]) to handle empty subarray case
    if T[0] < 0 and k > 0:
        F[0][1] = 0  # If we remove the first element, the sum is 0

    for i in range(1, n):
        for j in range(k+1):
            F[i][j] = F[i-1][j] + T[i] if T[i] >= 0 else F[i-1][j] + T[i]
            if j > 0 and T[i] < 0:
                F[i][j] = max(F[i][j], F[i-1][j-1])

    maxSum = max(max(row) for row in F)
    return maxSum




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests =True)

