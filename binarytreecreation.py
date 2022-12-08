class Tree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
#a function to do Inordertraversal
def calcInorder(root):
    if root:
        calcInorder(root.left)
        print(root.key,end=" ")
        calcInorder(root.right)
#A function preorder traversal
def calcpreorder(root):
    if root:
        print(root.key,end=" ")
        calcpreorder(root.left)
        calcpreorder(root.right)
#A function to do Postordertraversal
def calcpostorder(root):
    if root:
        calcpostorder(root.left)
        calcpostorder(root.right)
        print(root.key,end=" ")
#driver code
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.right.left=Tree(5)
root.left.right=Tree(10)
root.right.right=Tree(11)
print("Postorder traversal: ")
calcpostorder(root)
print("\nPreorder Traversal:")
calcpreorder(root)
print("\nInorder Traversal:")
calcInorder(root)
print()
