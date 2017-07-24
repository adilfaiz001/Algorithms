'''
Created on Jul 8, 2017

@author: Adil
'''
from graphs import graph
def BFS(G,s):
    level={s:0}
    parent={s:None}
    
    i=1
    frontier=[s]
    while frontier:
        next=[]
        for u in frontier:
            for v in G.getVertexAdj(u):
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier=next 
        i+1
      
        