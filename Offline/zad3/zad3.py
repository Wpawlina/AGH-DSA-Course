#Wojciech Pawlina
#Algorytm wykorzystuje 2 kopie tablicy P, jedna jest posortowana rosnaca po współrzędnej x ,druga rosnąco po współrzędnej y do sortowanie wykorzystuje algorytm quciksort o złozoności obliczeniowej O(nlogn).
#Nastepnie dla kazdego elementu w tablicy P za pomoca binsearch'a wyszukuje jego pozycje w obu posrtowanych tablicach i nastepnie na tej podstawie wylicza ile elementów ma wspołrzedna x mniejsza od sprawdzanego elementu oraz ile ma wspołrzedna y wieksza lub równa od sprawdzanego elementu
#odejmujac te wyniki otrzymuje ile elementów jest zdominowanych przez sprawdzany element
#jedynym mozliwym przypadkiem kiedy liczba elemntów dominowancyh bedzie błedna jest sytułacja kiedy istnieje taki elemnent który ma obie współrzedne wieksze od elementu sprawdzanego wówczas zostanie on błednie odjety
#jednak nie wpływa to na poprawoność algorytmu poniewaz jesli instnieje taki element to napewno dominuje on element sprawdzany zatem itak zostanie uwzgledniony 
# złozonśc obliczeniowa tego algorytmu wynosi O(nlogn)





from zad3testy import runtests




def findBinFirst(tab,el,indeks):
    p=0
    k=len(tab)-1
    while p<=k:
        s=(p+k)//2
        if tab[s][indeks]<el[indeks]:
            p=s+1
        else:
            k=s-1
    if p<len(tab) and el[indeks]==tab[p][indeks]:
        return p
    return -1
def partition(T,L,P,indeks):
    pivot=T[(L+P)//2][indeks]
    i=L
    j=P
    while i<=j:
        while T[i][indeks]<pivot:
            i+=1
        while T[j][indeks]>pivot:
            j-=1
        if i<=j:
            T[i],T[j]=T[j],T[i]
            i+=1
            j-=1
    return i,j
def quickSort(T,L,P,indeks):
    stos=[]
    stos.insert(0,(L,P))
    while len(stos)>0:
        L,P=stos.pop(0)
        if L<P:
            i,j=partition(T,L,P,indeks)
            if j-L>P-i:
                stos.insert(0,(i,P))
                stos.insert(0,(L,j))  
            else:
                stos.insert(0,(L,j))
                stos.insert(0,(i,P))

def dominance(P):
  n=len(P)
  Pa=P.copy()
  Pb=P.copy()
  quickSort(Pa,0,n-1,0)
  quickSort(Pb,0,n-1,1)# tworzenie kopi tablicy i odpowiednie sortowanie ich
  maxDom=0
  curDom=0
  for i in range(n):
       A=findBinFirst(Pa,P[i],0)#znajdowanie ile elementów ma wspólrzedna x mniejsza od elementu sprawdzanego
       B=n-1-findBinFirst(Pb,P[i],1)#znajdowanie ile elementów ma wspołrzedna y wieksza lub równa elementowi sprawdzanemu
       curDom=A-B# obliczanie ilosci elementow dominowanych przez element sprawdzany
       if curDom>maxDom:#znajdowanie elementu który dominuje najwiecej innych elementów
            maxDom=curDom      
  return maxDom 
       
  

   



 








# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
