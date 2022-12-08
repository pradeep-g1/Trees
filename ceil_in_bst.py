import sys
class Tree:
    def __init__(self,key):
        self.key=key
        self.left = None
        self.right = None
def insertion(root,i):
    if root.key == i:
        return 
    if root.key > i:
        if root.left:
            return insertion(root.left,i)
        else:
            root.left = Tree(i)
    else:
        if root.right:
            return insertion(root.right,i)
        else:
            root.right = Tree(i)
def inordertraversal(root):
    if root is None:
        return 
    else:
        inordertraversal(root.left)
        print(root.key,end=" ")
        inordertraversal(root.right)
def ceil(root,i):
    if root is None:
        return -1
    if root.key == i:
        return root.key
    if root.key < i:
        return ceil(root.right,i)
    val = ceil(root.left,i)
    return val if val >= i else root.key
#driver code
elements = [50,70,30,20,40,60,80,55,65]
root = Tree(elements[0])
elements.pop(0)
for i in elements:
    insertion(root,i)
inordertraversal(root)
print()
print(ceil(root,51))
