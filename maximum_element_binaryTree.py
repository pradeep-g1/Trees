import sys
class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def max_element(root):
    if root is None:
        return -sys.maxsize+1
    else:
        return max(root.key,max(max_element(root.left),max_element(root.right)))
root=Tree(20)
root.left=Tree(70)
root.right=Tree(90)
root.left.left=Tree(30)
root.left.right=Tree(40)
root.right.right=Tree(60)
print("maximum element in binary Tree is: ",max_element(root))