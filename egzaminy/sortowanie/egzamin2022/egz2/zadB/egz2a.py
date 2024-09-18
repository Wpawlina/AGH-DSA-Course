from egz2atesty import runtests

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    n=len(A)
    mag=[T]*n
    last=-1
    for a in A:
        for i in range(n):
            if mag[i]>=a:
                mag[i]-=a
                last=i
                break
    return last


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
