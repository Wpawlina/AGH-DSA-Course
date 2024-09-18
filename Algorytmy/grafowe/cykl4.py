def cycleC4(A):
    n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            cnt=0
            for k in range(n):
                if A[i][k]==1 and A[j][k]==1:
                        cnt+=1
                        if cnt==2:
                            return True
    return False

                