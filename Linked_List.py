# creating a node
class Node(object):
    def __init__(self, data):
        self.data = data   # data or value to store in node
        self.nextNode = None  # pointer pointing to next node but initiallizing with NULL

# creating the actual linked list
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    # Insert data at the start of list
    def insertStart(self,data):

        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode
    # Get the size of the list    
    def size1(self):
            return self.size
    # Insert data at the end of list
    def insertEnd(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
    # remove any available data from list
    def remove(self,data):
        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    # traverse through list and display the output
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print(" %d " % actualNode.data)
            actualNode = actualNode.nextNode
            
