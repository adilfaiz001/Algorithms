'''
Created on Jul 2, 2018

@author: adil
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
            for v in G.vertList(u).getAdjList():
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier=next 
        i+1
      