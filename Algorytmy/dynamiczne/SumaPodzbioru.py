def subsetSum(A,T):
    n=len(A)
    if n==0:
        return False
    F=[[False for _ in range(T+1)]for _ in range(n)]
    if A[0]<=T:
        F[0][A[0]]=True
    F[0][0]=True
    for i in range(n):
        F[i][0]=True
    
    for i in range(1,n):
        for s in range(1,T+1):
            F[i][s]=F[i-1][s]
            if s>=A[i]:
                F[i][s]=F[i][s] or F[i-1][s-A[i]]
    return F[n-1][T]     
    

def test_subsetSum():
    tests = [
        ([3, 34, 4, 12, 5, 2], 9, True),
        ([3, 34, 4, 12, 5, 2], 30, False),
        ([1], 0, True),
        ([5], 5, True),
        ([5], 10, False),
        ([1, 2, 3, 7], 6, True),
        ([1, 2, 3, 7], 15, False),
    ]
    
    for i, (A, T, expected) in enumerate(tests):
        result = subsetSum(A, T)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    
    print("All tests passed!")

# Uruchomienie testów
test_subsetSum()

        