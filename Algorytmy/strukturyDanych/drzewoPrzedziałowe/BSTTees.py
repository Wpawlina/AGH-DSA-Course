class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

# Przykładowe użycie
tree = AVLTree()
root = None
numbers = [10, 20, 30, 40, 50, 25]

for number in numbers:
    root = tree.insert(root, number)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root

            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self.left_rotate(root.left)

            return self.right_rotate(root) if root.left is None else root

        else:
            if root.right is None:
                return root

            if key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)
            elif key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self.right_rotate(root.right)

            return self.left_rotate(root) if root.right is None else root

    def search(self, root, key):
        return self.splay(root, key)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        root = self.splay(root, key)
        if root.key == key:
            return root

        new_node = Node(key)
        if key < root.key:
            new_node.right = root
            new_node.left = root.left
            root.left = None
        else:
            new_node.left = root
            new_node.right = root.right
            root.right = None

        return new_node

# Przykładowe użycie
tree = SplayTree()
root = None
numbers = [10, 20, 30, 40, 50, 25]

for number in numbers:
    root = tree.insert(root, number)

root = tree.search(root, 30)  # Przesuwanie 30 do korzenia



class Node:
    def __init__(self, data, color='R'):
        self.data = data
        self.color = color  # 'R' for red, 'B' for black
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, color='B')
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fix(self, k):
        while k.parent.color == 'R':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'B'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'R'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'B'
            return

        if node.parent.parent == None:
            return

        self.insert_fix(node)

    def print_tree(self, node, indent, last):
        if node != self.TNULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "   "
            else:
                print("L----", end=' ')
                indent += "|  "
            s_color = "RED" if node.color == 'R' else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

# Przykładowe użycie
rbt = RedBlackTree()
rbt.insert(55)
rbt.insert(40)
rbt.insert(65)
rbt.insert(60)
rbt.insert(75)
rbt.insert(57)

rbt.print_tree(rbt.root, "", True)

