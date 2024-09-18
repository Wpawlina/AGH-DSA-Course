# Wojciech Pawlina 
# ALgorytm przechodzi liniowo po liscie i dla kazdego elementu wyszukuje elemnent minimalny podlisty elementow znajdujacych sie co najwyzej o k od elementu sprawdzanego, jeśli element minimalny jest mniejszy od elementu sprawdzanego to przepinam go przed element sprawdzany i kontynułuje sprawdzanie ponownie sprawdzajac element sprawdzany,
# w przeciwnym wypadku pozostawiam element na swoim miejscu i przchodze do nastepnego 
# Algorytm stanowi modyfikacje algorytmu selection sort z tą rożnicą ze dla kazdej pozycji w liscie elementu minmalnego szuka tylko w czesci listy o dlugości k a nie w całej pozostałej do konca liscie, można tak zrobic ponieważ wiemy że kazdy element znajduje sie w odległosci co najwyzej k od swojej docelowej pozycji.
# dla k = Θ(1) złozoność jest liniowa  Θ(n)  ,dla k = Θ(log n) złozoność wynosi Θ(nlog n)  oraz dla k = Θ(n) złozonść jest kwadratowa i wynosi Θ(n^2) zatem złożonośc dla dowolnego k wynosi Θ(nk) .

from zad1testy import Node, runtests
def SortH(p,k):
    L=Node()
    L.next=p # stworzenie wartowanika dla listy początkowej 
    result=L   # wskaznik na poczatek listy
    while L.next is not None:
        minP=L
        i=0
        q=L.next
        while q.next is not None and i<k:   # wyszukiwanie elementu minimalnego w podliscie o dlugosic k znajdujacej sie po elemencie sprawdzanym
            if q.next.val<minP.next.val:
                minP=q
            q=q.next
            i+=1
        if minP.next.val<L.next.val: # jesli element minmalny jest mniejszy od elementu sprawdzanego, przepinam element minimalny przed element sprawdzany i ponownie sprawdzamy element sprawdzany
            element=minP.next
            minP.next=element.next
            temp=L.next
            L.next=element
            element.next=temp
        L=L.next
    return result.next # zwracam liste wynikową bez wartownika








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )