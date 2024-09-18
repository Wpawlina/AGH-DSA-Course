class Node:
    def __init__(self,key, value):
        self.value=value
        self.key=key
        self.parent = None
        self.left = None
        self.right = None


def search(root,key):
    while root is not None:
        if root.key==key:
            return root
        elif root.key<key:
            root=root.right
        else:
            root=root.left
    return None

def insert(root,key,value):
    node=Node(key,value)
    while root is not None:
        if root.key==key:
            root.value=value
            return
        elif root.key<key:
            if root.right is None:
                root.right=node
                node.parent=root
                return
            root=root.right
        else:
            if root.left is None:
                root.left=node
                node.parent=root
                return
            root=root.left
    return 

def maxValue(root):
    if root is None:
        return None
    while root.right is not None:
        root=root.right
    return root

def minValue(root):
    if root is None:
        return None
    while root.left is not None:
        root=root.left
    return root


def next(node):
    if node is None:
        return None
    if node.right is not None:
        return minValue(node.right)
    else:
        if node.parent is None:
            return None
        while node.parent is not None and node.parent.key<node.key:
            node=node.parent
        if node.parent is None:
            return None
        return node.parent
    
def prev(node):
    if node is None:
        return None
    if node.left is not None:
        return maxValue(node.left)
    else:
        if node.parent is None:
            return None
        while node.parent is not None and node.parent.key>node.key:
            node=node.parent
           
        if node.parent is None:
            return None
        return node.parent
    

def delete(node):
    if node is None:
        return 
    if node.left is None and node.right is None:
        if node.parent.left==node:
            node.parent.left=None
            return
        node.parent.right=None
        return
    if node.left is  None:
        if node.parent.left==node:
            node.parent.left,node.right.parent=node.right,node.parent
            return
        node.parent.right,node.right.parent=node.right,node.parent
        return
    if node.right is  None:
        if node.parent.left==node:
            node.parent.left,node.left.parent=node.left,node.parent
            return
        node.parent.right,node.left.parent=node.left,node.parent
        return
    nextNode=next(node)
    node.key,nextNode.key=nextNode.key,node.key
    node.value,nextNode.value=nextNode.value,node.value
    delete(nextNode)


root = Node(5,'Value 5')
'''
insert(root,7,'Value 7')
insert(root,10,'Value 10')  
insert(root,4,'Value 4')  
insert(root,20,'Value 20')  
insert(root,1,'Value 1')  
insert(root,3,'Value 3')  


print(search(root,20).value)
print(search(root,1).value)

print(prev(search(root,3)).value)
delete(search(root,1))
print(prev(search(root,3)).value)
insert(root,6,'value 6')
print(search(root,6).value)
insert(root,6,'value 6 test')
print(search(root,6).value)
print(next(search(root,7)).value)
delete(search(root,7))
print(search(root,7))

node=search(root,10)
print(node.parent.value,node.value,node.left.value,node.right.value)
print(prev(next((search(root,6)))).value)
'''

insert(root, 3, "Value 3")
insert(root, 7, "Value 7")
insert(root, 2, "Value 2")
insert(root, 4, "Value 4")
insert(root, 6, "Value 6")
insert(root, 8, "Value 8")

assert search(root, 5).value == "Value 5"
assert search(root, 3).value == "Value 3"
assert search(root, 7).value == "Value 7"
assert search(root, 2).value == "Value 2"
assert search(root, 4).value == "Value 4"
assert search(root, 6).value == "Value 6"
assert search(root, 8).value == "Value 8"
assert search(root, 9) is None

# Test 2: Minimum and Maximum Values
assert minValue(root).key == 2
assert maxValue(root).key == 8

# Test 3: Successor and Predecessor
node_3 = search(root, 3)
node_4 = search(root, 4)
node_5 = search(root, 5)
node_6 = search(root, 6)
node_7 = search(root, 7)
node_8 = search(root, 8)

assert next(node_3).key == 4
assert next(node_4).key == 5
assert next(node_5).key == 6
assert next(node_6).key == 7
assert next(node_7).key == 8
assert next(node_8) is None

assert prev(node_8).key == 7
assert prev(node_7).key == 6
assert prev(node_6).key == 5
assert prev(node_5).key == 4
assert prev(node_4).key == 3
assert prev(node_3).key == 2
assert prev(search(root, 2)) is None

# Test 4: Deletion
delete(node_5)  # Deleting node with key 5
print(next(search(root,4)).value)
assert search(root, 5) is None
assert next(search(root,4)).key == 6
assert prev(search(root,6)).key == 4

delete(search(root,7))  # Deleting node with key 7
assert search(root, 7) is None

assert next(search(root,6)).key == 8
assert prev(search(root,8)).key == 6

print("All tests passed!")        



