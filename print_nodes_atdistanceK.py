class Tree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def postordertraversal(root):
    if root:
        postordertraversal(root.left)
        postordertraversal(root.right)
        print(root.key,end=" ")
def printnode(root,k):
    if root is None:
        return
    elif k==0:
        print(root.key,end=" ")
    else:
        printnode(root.left,k-1)
        printnode(root.right,k-1)
root=Tree(10)
root.left=Tree(9)
root.left.left=Tree(8)
root.left.right=Tree(7)
root.left.left.left=Tree(5)
root.right=Tree(11)
root.right.left=Tree(12)
postordertraversal(root)
print("\nPrinting nodes at distance K: ")
printnode(root,2)
print()