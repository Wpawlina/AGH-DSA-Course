def szachownica(A):
    n=len(A)
    F=[[float('inf') for _ in range(n)] for _ in range(n)]
    F[0][0]=A[0][0]
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                continue
            best=float('inf')
            if j-1>=0:
                best=F[i][j-1]+A[i][j]
            if i-1>=0:
                best=min(best,F[i-1][j]+A[i][j])
            F[i][j]=best
    return F[n-1][n-1]

def test_szachownica():

    # Test cases
    tests = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),  # Expected path: 1→3→1→1→1, total cost: 7
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21), # Expected path: 1→2→3→6→9, total cost: 21
        ([[1, 2], [1, 1]], 3),                   # Expected path: 1→1→1, total cost: 3
        ([[1]], 1),                              # Single cell, total cost: 1
        ([[5, 9], [8, 7]], 20),                  # Expected path: 5→9→7, total cost: 20
        ([[1, 2, 5], [3, 2, 1], [4, 2, 1]], 7),  # Expected path: 1→2→2→1→1, total cost: 8
        ([[1, 99], [1, 1]], 3),                  # Expected path: 1→1→1, total cost: 3
        ([[1, 2, 3, 4], [2, 2, 3, 4], [3, 3, 3, 4], [4, 4, 4, 4]], 19)  # Complex path with multiple same cost
    ]

    for i, (A, expected) in enumerate(tests):
        result = szachownica(A)
        assert result == expected, f"Test case {i+1} failed: szachownica({A}) = {result}, expected {expected}"
        print(f"Test case {i+1} passed!")

# Run the test function
test_szachownica()


