# Define Node class for binary Search tree
class Node:
    def __init__(self, data):
        # Initialize the node with left and right children set to None and then provide data
        self.left = None
        self.right = None
        self.data = data

        # Method to insert a new node into the binary search tree
    def insert(self, data):
            # Compare new value with current node's data
        if self.data:
                # if data is less than current node data
            if data < self.data:
                    # if there is no left child, create one
                if self.left is None:
                    self.left = Node(data)
                    # if there is a left child, insert a data
                else:
                    self.left.insert(data)
                # if new value is greater than a node data
            elif data > self.data:
                    # if there is no right child, create one
                if self.right is None:
                    self.right = Node(data)
                    # if there is a right child, insert a data
                else:
                    self.right.insert(data)
            # If current node has no data, insert one
        else:
            self.data = data

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

# create a root node with data 12
root = Node(12)
# insert a node with data 6, 14 and 3 into the binary search tree
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()












