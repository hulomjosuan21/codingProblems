class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_traversal(self, traversal_type):
        if traversal_type == 'pre order':
            return self.preOrder_traversal(self.root,'')
        elif traversal_type == 'in order':
            return self.inOrder_traversal(self.root,'')
        elif traversal_type == 'post order':
            return self.postOrder_traversal(self.root,'')
        else:
            return f"Invalid traversal type {traversal_type}"

    def preOrder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preOrder_traversal(start.left, traversal)
            traversal = self.preOrder_traversal(start.right, traversal)
        return traversal

    def inOrder_traversal(self, start, traversal):
        if start:
            traversal = self.inOrder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inOrder_traversal(start.right, traversal)
        return traversal

    def postOrder_traversal(self, start, traversal):
        if start:
            traversal = self.postOrder_traversal(start.left, traversal)
            traversal = self.postOrder_traversal(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

binaryTree = BinaryTree('F')
binaryTree.root.left = TreeNode('B')
binaryTree.root.right = TreeNode('G')
binaryTree.root.left.left = TreeNode('A')
binaryTree.root.left.right = TreeNode('D')
binaryTree.root.right.right = TreeNode('I')
binaryTree.root.right.right.left = TreeNode('H')

binaryTree.root.left.right.left = TreeNode('C')
binaryTree.root.left.right.right = TreeNode('E')

print(binaryTree.print_traversal('in order'))