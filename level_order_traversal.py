class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def levelordertraversal(root):
    size=0  #for finding the size of binary Tree
    if root is None:
        return 
    queue=[]
    queue.append(root)
    while len(queue)>0:
        print(queue[0].key,end=" ")
        size+=1
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print("\nsize of the binary is: ",size)

root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
root.right.left=Tree(6)
root.right.left.left=Tree(7)
root.right.left.right=Tree(8)
levelordertraversal(root)