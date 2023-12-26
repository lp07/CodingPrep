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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # Post Order Traversal
    # Left -> Right -> Root

    def postOrderTraversal(self, root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postOrderTraversal(root))

# o/p : [3, 6, 42, 31, 19, 14, 12]



