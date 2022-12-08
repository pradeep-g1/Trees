class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def spiral_order_helper(root):
    left_to_right=True
    spiralorder(root,left_to_right)
def spiralorder(root,left_to_right):
    if root is None:
        return
    queue=[]
    stack=[]
    queue.append(root)
    while len(queue)>0:
        n=len(queue)
        for i in range(n):
            temp=queue[0]
            queue.pop(0)
            if left_to_right:
                print(temp.key,end=" ")
            else:
                stack.append(temp)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        if left_to_right == False:
            while len(stack)>0:
                print(stack.pop().key,end=" ")
        print()
        left_to_right=not left_to_right
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
spiral_order_helper(root)
