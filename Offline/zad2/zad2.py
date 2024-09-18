#Wojciech Pawlina
#Algorytm korzysta z tablicy pomocniczej o dlugosci p w której przechowuje elementy z poprzedniego przedziału (i-1,i+p-2) w posortowanej malejaco kolejnosci , 
#najpierw usuwam z tablicy pomocniczej element poczatkowy poprzedniego przedziału wyszukujac jego indeks poprzez wyszukiwanie binarne 
# i nastepnie rowniez uzywajac wyszukiwania binarnego znajduje indeks na którym powinien sie znalesc ostatni element z bierzacego przedziału aby tablica dalej byla posortowana malejaco i wstawiam go na to miejsce przesuwjac elementy za nim w tablicy w prawo 
# nastepnie wyciagam z tablicy pomocniczej element o indeksie k-1( k-ty najwiekszy ) i dodaje go do wynikowej sumy
# złozonosc czasowa tego algorytmu wynosi O(np)





from zad2testy import runtests

def binSearch(T,val,L,P):# zmodyfikowane wyszukiwanie binarne które znajduje indeks na którym powinien być wstawiony element o wartosic val
    while L<=P:
        M=(L+P)//2
        if T[M]==val:
            return M+1
        elif T[M]>val:
            L=M+1
        else:
            P=M-1
    return L

def ksum(T, k, p):
    n=len(T)
    result=0 
    pomT=[T[0]] # inicjalizacja tablicy pomoczej 
    for i in range(1,p): # wypełnienie tablicy pomocniczej elementami z pierwszego przedziału tak aby były w posortowanej malejaco kolejności
        j=binSearch(pomT,T[i],0,i-1)
        pomT.insert(j,T[i])
    result+=pomT[k-1]
    for i in range(1,n-p+1):
        prev=binSearch(pomT,T[i-1],0,p-1)#wyszukanie pierwszego elemntu z poprzedniego przedzialu w tablicy pomocnieczej 
        del pomT[prev-1]#usuniecie tego elementu co powoduje przesuniecie pozostalych elementow w lewo
        j=binSearch(pomT,T[i+p-1],0,p-2) # wyszukanie indeksu do wstawienia ostatniego elementu z bierzacego przedziału
        pomT.insert(j,T[i+p-1]) # wstawienie tego elementu i przesuniecie pozostalych elementów w prawo
        result+=pomT[k-1]
    return result


   


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )




