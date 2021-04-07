# Pre-order traversal of a binary tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            print(f'Traversal type {str(traversal_type)} is not supported')
            return False

    def preorder_print(self, start, traversal):
        """ Right -> Left -> Right """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal   


def printPreOrder(root):
    if root:
        print(root.value),
        printPreOrder(root.left)
        printPreOrder(root.right)


# Set up tree: 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.preorder_print('preorder'))

# # Driver code
# root = Node(1)
# root.left      = Node(2)
# root.right     = Node(3)
# root.left.left  = Node(4)
# root.left.right  = Node(5)
# print ("Preorder traversal of binary tree is")
# print (printPreOrder(root), sep='-')