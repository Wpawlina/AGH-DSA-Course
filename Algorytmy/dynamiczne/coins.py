import math

def coins(C,S):
    n=len(C)
    F=[[float('inf')for _ in range(S+1) ] for _ in range(n)]
    for i in range(n):
        F[i][0]=0
    for s in range(1,S+1):
        if s%C[0]==0:
            F[0][s]=s/C[0]
    for s in range(1,S+1): 
        for i in range(1,n):
            factor=math.floor(s/C[i])
            best=F[i-1][s]
            for k in range(1,factor+1):
                best=min(best,F[i-1][s-k*C[i]]+k)
            F[i][s]=best
    return F[n-1][S]
            

            

def coins2(C,S):
    n=len(C)
    F=[[float('inf') for _ in range(S+1)] for _ in range(n)]
    for i in range(n):
        F[i][0]=0
    def f(C,i,s):
        if F[i][s]!=float('inf'):
            return F[i][s]
        factor=math.floor(s/C[i])
        if i==0:
            if s%C[i]==0:
                F[i][s]=s/C[i]
                return F[i][s]
            else:
                return float('inf')
        best=f(C,i-1,s)
        for k in range(1,factor+1):
            best=min(best,f(C,i-1,s-k*C[i])+k)
        F[i][s]=best
        return F[i][s]
    return f(C,n-1,S)




def test_coins2():

    # Test cases
    tests = [
        # Simple test cases
        ([1, 2, 5], 11, 3),  # 11 = 5 + 5 + 1
        ([1, 2, 5], 0, 0),   # 0 = no coins needed
        ([2], 3, float('inf')),  # 3 cannot be formed with only 2s
        
        # Edge cases
        ([1], 100, 100),     # 100 = 1*100
        ([1, 2, 5], 1, 1),   # 1 = 1
        ([5, 10], 28, float('inf')),  # 28 cannot be formed with 5 and 10
        
        # Larger sum and coin sets
        ([1, 3, 4], 6, 2),   # 6 = 3 + 3
        ([2, 5, 10], 27, 4),  # 27 = 10 + 10 + 5 + 2
        
        # No possible combination
        ([7, 13], 10, float('inf')), # 10 cannot be formed with 7 and 13
    ]

    for i, (C, S, expected) in enumerate(tests):
        result = coins(C, S)
        assert result == expected, f"Test case {i+1} failed: coins2({C}, {S}) = {result}, expected {expected}"
        print(f"Test case {i+1} passed!")

# Run the test function
test_coins2()
            
            
      
           
            
    