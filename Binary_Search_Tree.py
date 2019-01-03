# Initialize the Node class to create new node
class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
# Initialise the BST class to make the tree

class BinarySearchTree(object):
    def __init__(self):
        self.root = None    # instantiate the root node as NULL initially
    def insert(self,data):
        if not self.root:           # if the data is not root node yet then make it the root node
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)  # two attributes because first to insert the data and second to compare the data with... acc to BST principle

    # O(logn) time complexity if the tree is balanced
    def insertNode(self,data,node):
        #checking the principle of BST
        if data < node.data:
            if node.leftChild:  # leftChild is not empty so we call the method recursively to insert node as principle
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild: # rightChild is not empty so we call the method recursively to insert node as principle
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)
    # O(log N) complexity
    def removeNode(self,data,node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing leaf node .....")
                del node
                return None
            if not node.leftChild:
                print("Removing node with single right child .....")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing node with single left child .....")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children ..... ")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node
            

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    # O(log N) complexity
    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)
    # O(N) complexity
    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
    def getRoot(self):
        if self.root:
            return self.root.data
