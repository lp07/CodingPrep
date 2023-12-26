class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # Pre Order Traversal
    # Root -> Left -> Right

    def preOrderTraversal(self, root):
        # Initialize an empty list to store the result (visited nodes)
        res = []
        # Check if current node is not none
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.preOrderTraversal(root))

# o/p : [12, 6, 3, 14, 19, 31, 42]






