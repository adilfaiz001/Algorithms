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