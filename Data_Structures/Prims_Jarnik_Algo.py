import heapq

class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.predecessor = None
        self.visited = False

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,weight,startVertex,targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
    def __cmp__(self,otherEdge):
        return self.cmp(self.weight, otherEdge.weight)
    def __lt__(self,other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority

class PrimJarnikAlgo(object):
    def __init__(self,unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.fullCost = 0
        self.edgeHeap = []

    def calculateSpanningTree(self,vertex):
        self.unvisitedList.remove(vertex)

        while self.unvisitedList:
            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)

            minEdge = heapq.heappop(self.edgeHeap)

            self.spanningTree.append(minEdge)
            print(" Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name,minEdge.targetVertex.name))
            self.fullCost = self.fullCost + minEdge.weight

            vertex = minEdge.vertex
            self.unvisitedList.remove(vertex)

    def getSpanningTree(self):
        return self.spanningTree
