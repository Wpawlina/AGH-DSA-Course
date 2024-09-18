def binSearch(T,val,L,P):# zmodyfikowane wyszukiwanie binarne które znajduje indeks na którym powinien być wstawiony element o wartosic val
    while L<=P:
        M=(L+P)//2
        if T[M]==val:
            return M+1
        elif T[M]<val:
            L=M+1
        else:
            P=M-1
    return L

def Lis(T):
    n=len(T)
    S=[float('inf') for _ in range(n)]

    for i in range(n):
        pos=binSearch(S,T[i],0,n-1)
      
        S[pos]=T[i]
    res=0
    for i in range(n):
        if S[i]==float('inf'):
            break
        res+=1
    return res
T=[2,1,4,3,4,8,5,7]
print(Lis(T))

def test_Lis():
    # Test case 1: Empty list
    assert Lis([]) == 0
    
    # Test case 2: Single element
    assert Lis([10]) == 1
    
    # Test case 3: Increasing order
    assert Lis([1, 2, 3, 4, 5]) == 5
    
    # Test case 4: Decreasing order
  
    assert Lis([5, 4, 3, 2, 1]) == 1
    
    # Test case 5: Random order
    assert Lis([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    
    # Test case 6: With repeated elements
    assert Lis([1, 3, 5, 3, 3, 4, 8, 6]) == 5

    print("All Lis tests passed.")

# Run the tests
test_Lis()