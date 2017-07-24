'''
Created on Jun 21, 2017

@author: Adil
'''
from vertex import Vertex
class Graph:
    def __init__(self):
        self.vertList = {}   #node list where each indexed number is an object of vertex class.
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertexAdj(self,n):
        if n in self.vertList:
            return self.vertList[n].getAdjList()
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
g=Graph()
for i in xrange(5):
    g.addVertex(i)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(5, 3)
g.addEdge(5, 4)
l=g.getVertexAdj(1)
if 2 in l:
    print 'yes'
else:
    print 'No'
print l
        