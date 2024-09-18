import unittest


def blackforest(T):
    n=len(T)
    if n == 0:
        return 0
    if n == 1:
        return T[0]
    if n == 2:
        return max(T[0], T[1])
    F=[-1 for _ in range(n)]
    F[0]=T[0]
    F[1]=T[1]
    F[2]=F[0]+T[2]
    for i in range(3,n):
        F[i]=max(F[i-2],F[i-3])+T[i]
    return max(F)
class TestBlackForest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(blackforest([]), 0)
    
    def test_single_element(self):
        self.assertEqual(blackforest([5]), 5)
        self.assertEqual(blackforest([-5]), -5)
    
    def test_two_elements(self):
        self.assertEqual(blackforest([1, 2]), 2)
        self.assertEqual(blackforest([5, 1]), 5)
    
    def test_general_case(self):
        self.assertEqual(blackforest([3, 2, 5, 10, 7]), 15)
        self.assertEqual(blackforest([3, 2, 7, 10]), 13)
        self.assertEqual(blackforest([5, 5, 10, 100, 10, 5]), 110)
        self.assertEqual(blackforest([3, 2, 5, 1, 1, 5, 10, 1]), 19)
    
    def test_all_negative_numbers(self):
        self.assertEqual(blackforest([-1, -2, -3, -4]), -1)
        self.assertEqual(blackforest([-5, -1, -1, -5]), -1)
    
    def test_mixed_numbers(self):
        self.assertEqual(blackforest([3, -2, 5, -1, 7]), 15)
        self.assertEqual(blackforest([5, 5, -10, 100, -10, 5]), 110)

if __name__ == '__main__':
    unittest.main()