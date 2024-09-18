#Wojciech Pawlina
# algorytm kopiuje i sortuje tablice rosnaca po wartosciach
# nastepnie dla kazdego elementu sprawdza ile elementow znajduje sie przed nim w tablcy robi to w czasie stałym wykorzystujac indeksowanie
# nastepnie za pomoca binary-search wyszkuje ile emelemntów w tablicy jest wiekszych od elementu sprawdzanego 
# aby obliczyc range danego elementu algorytm od liczby elementow znajdujaych sie przednim w tablicy odejmuje ilosc elementów wiekszych lub równych jemu
# algortym jest poprawny i działa w kazdym przypadku poniewaz jesli w tablicy po sprawdzanym elemencie nie znajduja sie juz elementy wieksze od niego to odejmowanie daje poprawny wynik
# a jesli znajduja sie po nim elementy wieksze to wynik obliczania rangi dlatego konkretnego elementu bedzie nie poprawny ale oznacza to ze znajduja sie w tablicy elementy o wyzszej randze
# i ich ranga bedzie obliczona poprawnie
# złozonosc obliczeniowa algorytmu to O(nlogn) poniewaz dla kazdego elementu wyszukuje go w drugiej tablicy przy pomocy binary-search który ma złozonsc obliczeniowa O(logn) oraz do sortowania uzywa quicksort ktory ma zlozonosc O(nlogn)
# zlozonsc pamieciowa to O(n) poniewa algorytm wykorzystuje dwie tablice o rozmiarze n

 

from kol1testy import runtests

def quickSort(tab,L,P):
    pivot=tab[(L+P)//2]
    i=L
    j=P
    while i <= j:
        while tab[i]<pivot:
            i+=1
        while tab[j]>pivot:
            j-=1
        if i<=j:
            tab[i],tab[j]=tab[j],tab[i]
            i+=1
            j-=1
    if j>L:
        quickSort(tab,L,j)
    if i<P:
        quickSort(tab,i,P)
  
   
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

        


def maxrank(T):
    n=len(T)
    Tvalues=[0]*n
    for i in range(n):
        Tvalues[i]=T[i]
    quickSort(Tvalues,0,n-1)# tworzenie i sortowanie tablicy po wartosciach
    maxrank=-1
    for i in range(1,n):
        curank=i
        bigger=findBinFirst(Tvalues,T[i])# wyszukiwanie sprawdzanego elementu w drugiej tablicy 
        bigger=n-bigger-1 # obliczanie ilosci elementow wiekszych lub rownych elementowi sprawdzanemu
        curank-=bigger
        if curank>maxrank:
            maxrank=curank
    return maxrank
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )


