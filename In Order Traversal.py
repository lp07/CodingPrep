class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # In - Order Traversal
    # Left -> Root -> Right

    # In-ordered function for binary tree
    def InOrderTraversal(self, root):
        # Initialize an empty list to store the result (order of visited nodes)
        res = []
        # Check if current node is not None
        if root:
            # recursively perform the inorder traversal on the left subtree
            res = self.InOrderTraversal(root.left)
            # append the value of current node to the result list
            res.append(root.data)
            # recursively perform the inorder traversal on the right subtree
            res = res + self.InOrderTraversal(root.right)
        return res

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.InOrderTraversal(root))

# o/p : [3, 6, 12, 14, 19, 31, 42]







