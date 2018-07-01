'''
Created on Jun 21, 2017

@author: Adil
'''
class Vertex(object):
    '''
    vertex class for marking the adjacency of each vertex,
    id = key,(node)
    connectedTo={<obj>:value},adjacency list of node
    
    '''


    def __init__(self, key):
        '''
        Here id shows current node or vertex and connectedTo dictionary is showing its adj list.
        id-->connectedTo[vertices]
        '''
        self.id=key          #id=node
        self.connectedTo={}  
        '''
        dictionary = {<object.vertex>:value},obj.vertex is showing that these objects are from vertex class 
        itself which are connected to parent vertex object that is self.id
        '''
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    
    def __str__(self):
        return str(self.id)+ 'connectedTo :' + str([x.id for x in self.connectedTo])  # x.id referring to iterating vertex object id in self.connectedTo 
                                                                                         
    
    def getAdjList(self):
        return [x.id for x in self.connectedTo]
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getValues(self):
        return self.connectedTo.values()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    

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
        
    def getVertWeight(self,n):
        if n in self.vertList:
            return self.vertList[n].getValues()
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

        