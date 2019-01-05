# Recursive method of DFS


class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DepthFirstSearch(object):
    def dfs(self,node):
        node.visited = True
        print("%s" % node.name)

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)
