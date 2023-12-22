class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the Tree
    def printTree(self):
        print(self.data)

root = Node(10)
root.printTree()