# Wojciech Pawlina
# Algorytm wykorzystuje funkcje rekurencyjna z zapsiywaniem wartosci do tablicy F. funkcja rekurencyjna zapsiuje 3 liczby odwiedzonych komnat dla kazdej komnaty w zaleznosci z której strony weszlismy do danej komnaty.
# Aby uniknac petli w rekurencji dla kazdego wywolania zapisujemy strone wejscia do danej komórki aby uniknac poruszania sie góra-dół co powodowło by nieskonczone wywołania rekurencyjne.
# Tablica F jest zainicjalizowana z wartosciami -1 dla kazdje sprawdzone komórki zapisujemy w Tablicy ilosc odwiedzonych dla niej komnat w zaleznosci z której strony weszlismy. Jesli z danej strony nie da się wejsc to zapisuejmy wartosc -flaot('inf')
# funkcja rekurnecyjna wykorzystuje zapsiane wartosci  z tablicy  F dopiero wtedy kiedy wszytkie 3 wartosci sa juz ustawione to znaczy kiedy w danej komórce F nie ma wartosci -1
# na koniec algorytm zwraca maksymlalna ilosc kolumn odwiedzonych dla ostatniej komnaty, jeśli nie da sie dotrzeć do ostaniej komnaty to algorytm zwraca liczbe -1 


from zad7testy import runtests

def maze( L ):

    n=len(L)
    F=[[[-1,-1,-1]for _ in range(n)]for _ in range(n)]
    if L[0][0]=='#':
        return -1
    if L[n-1][n-1]=='#':
        return -1
    F[0][0]=[0,0,0]
    def f(i,j,prev):
        nonlocal F
        if -1 not in F[i][j]:
            return F[i][j] 
        if j>0 and L[i][j-1]!='#':
            cntk=f(i,j-1,'P')
            F[i][j][0]=max(cntk)+1
        else:
            F[i][j][0]=-float('inf')
        if prev!='D':
            if i>0  and L[i-1][j]!='#':
                cntk=f(i-1,j,'G')
                F[i][j][1]=max(cntk[0],cntk[1])+1
            else:
                F[i][j][1]=-float('inf')
        if prev!='G':
            if i<n-1  and L[i+1][j]!='#':
                cntk=f(i+1,j,'D')
                F[i][j][2]=max(cntk[0],cntk[2])+1
            else:
                F[i][j][2]=-float('inf')
        return F[i][j]
    res=f(n-1,n-1,'')
    print(F)
    return -1 if max(res)<0 else max(res)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
