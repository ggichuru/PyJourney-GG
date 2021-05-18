class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Preorder function 
def printPreorder(root):
    if root:
        #first print the data of the node, after which you recur on the left and right child respectively 
        print(root.value, end='')
        printPreorder(root.left)
        printPreorder(root.right)

# Inorder funtion
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value, end='')
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value, end='')

# Setup the tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

print('Preorder: ', end='')
printPreorder(root)
print()
print('Inorder: ', end='')
printInorder(root)
print()
print('Postorder: ', end='')
printPostorder(root)