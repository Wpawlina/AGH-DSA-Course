from zad3testy import runtests


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

def find_node(root, num):  
    path = []
    while num > 1:
        path.append(num)
        num //= 2
    path.reverse()
    node = root
    for p in path:
        if node is None:
            return -float('inf')
        if p % 2 == 0:
            node = node.left
        else:
            node = node.right
    return node.key if node is not None else -float('inf')

def maxim(T, X):
    max_key = float('-inf')
    for num in X:
        key= find_node(T, num)
        if key > max_key:
            max_key = key
    return max_key

if __name__ == "__main__":
    # Tworzenie przykładowego drzewa
    root = Node(5)
    root.left = Node(2)
    root.left.parent = root
    root.right = Node(3)
    root.right.parent = root
    root.left.left = Node(1)
    root.left.left.parent = root.left
    root.left.right = Node(0)
    root.left.right.parent = root.left
    root.right.left = Node(8)
    root.right.left.parent = root.right
    root.right.right = Node(15)
    root.right.right.parent = root.right

    X = [3, 6, 4]
    print("Maksymalny klucz:", maxim(root, X))  
    
runtests(maxim)