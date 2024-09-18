from egz2btesty import runtests

def magic( C ):
    n=len(C)
    F=[-float('inf') for _ in range(n)]
    F[0]=0
    for i in range(n-1):
        if F[i]>=0:
            cur_gold=F[i]
            for j in range(1,4):
                if C[i][j][1]>i:
                    new_gold=C[i][0]-C[i][j][0] 
                    if new_gold>10:
                        continue
                    new_gold+=cur_gold
                    if  new_gold>F[C[i][j][1]]:
                        F[C[i][j][1]]=new_gold
    return F[-1] if F[-1]!=-float('inf') else -1 


    

   
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)
