class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def spiralorder(root):
    if root is None:
        return
    stack1=[]
    stack2=[]
    stack1.append(root)
    while len(stack1)!=0 or len(stack2)!=0:
        while len(stack1)!=0:
            temp=stack1.pop()
            print(temp.key,end=" ")
            if temp.left:
                stack2.append(temp.left)
            if temp.right:
                stack2.append(temp.right)
        print()
        while len(stack2)!=0:
            temp=stack2.pop()
            print(temp.key,end=" ")
            if temp.right:
                stack1.append(temp.right)
            if temp.left:
                stack1.append(temp.left)
        print()
#driver code
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
root.right.left=Tree(6)
root.right.right=Tree(7)
spiralorder(root)