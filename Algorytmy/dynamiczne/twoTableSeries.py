def twoTableSeries(A,B):
    n=len(A)
    F=[[0 for _ in range(n)]for _ in range(n)]
    if A[0]==B[0]:
        F[0][0]=1
    cntA=0
    cntB=0
    for i in range(n):
        if A[i]==B[0]:
            cntA=1
        F[i][0]=cntA
        if A[0]==B[i]:
            cntB=1
        F[0][i]=cntB

    for i in range(1,n):
        for j in range(1,n):
            best=0
            if A[i]==B[j]:
                best=F[i-1][j-1]+1
            best=max(best,F[i-1][j],F[i][j-1])
            F[i][j]=best
    return F[n-1][n-1]


def twoTableSeries2(A,B):
    n=len(A)
    F=[[-1 for _ in range(n)]for _ in range(n)]
    if A[0]==B[0]:
        F[0][0]=1
    else:
        F[0][0]=0
    cntA=0
    cntB=0
    for i in range(n):
        if A[i]==B[0]:
            cntA=1
        F[i][0]=cntA
        if A[0]==B[i]:
            cntB=1
        F[0][i]=cntB
    def f(A,B,i,j):
        if F[i][j]!=-1:
            return F[i][j]
        best=0
        if A[i]==B[j]:
            best=f(A,B,i-1,j-1)+1
        best=max(best,f(A,B,i-1,j),f(A,B,i,j-1))
        F[i][j]=best
        return F[i][j]
    return f(A,B,n-1,n-1)



def test_twoTableSeries2():
    

    # Test cases
    tests = [
        (["A", "B", "C", "D", "E"], ["A", "C", "B", "D", "E"], 4), # LCS: "ACDE"
        (["A", "B", "C", "D"], ["B", "D", "C", "A"], 2), # LCS: "BD" or "BA"
        (["A", "B", "C"], ["D", "E", "F"], 0), # No common subsequence
        (["A", "B", "C", "B", "D", "A"], ["B", "D", "C", "A", "B", "A"], 4), # LCS: "BCBA"
        (["A"], ["A"], 1), # Single element common
        (["A"], ["B"], 0), # Single element not common
        (["A", "B", "A", "B"], ["B", "A", "B", "A"], 3), # LCS: "BAB"
        (["A", "B", "C", "D", "E"], ["A", "B", "C", "D", "E"], 5), # LCS: "ABCDE"
        (["A", "B", "C"], ["A", "B", "C"], 3), # LCS: "ABC"
        (["A", "A", "A"], ["A", "A", "A"], 3) # LCS: "AAA"
    ]

    for i, (A, B, expected) in enumerate(tests):
        result = twoTableSeries2(A, B)
        assert result == expected, f"Test case {i+1} failed: twoTableSeries2({A}, {B}) = {result}, expected {expected}"
        print(f"Test case {i+1} passed!")
    for i, (A, B, expected) in enumerate(tests):
        result = twoTableSeries(A, B)
        assert result == expected, f"Test case {i+1} failed: twoTableSeries2({A}, {B}) = {result}, expected {expected}"
        print(f"Test case {i+1} passed!")


test_twoTableSeries2()