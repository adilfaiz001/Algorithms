'''
Created on Feb 17, 2017

@author: Rahil
'''

'''
Minimum Heap Structure 
'''
class MinHeap(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.currentSize=0
        self.HeapList=[0]
        
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    
    def percUp(self,pos):
        i=int(pos/2)
        while i>0:
            if self.heapList[2*i] < self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[2*i]
                self.heapList[i] = tmp
            i = int(i / 2)
            
    def percDown(self,pos):
        i=pos
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,pos):
        i=pos
        if (i<<1 + 1) > self.currentSize:
            return i<<1
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i<<1
            else:
                return i<<1 + 1  
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = int(len(alist)/ 2)
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
     
    def HeapSort(self,alist):
        heapsort=[]
        self.buildHeap(alist)
        i=self.currentSize-1
        while i>0:
            top=self.delMin()
            print top
            heapsort.append(top)
            i-=1
        alist=[x for x in heapsort]
            
bh=MinHeap()
lst=[0,4,1,2,4,6,7,3]
bh.HeapSort(lst)
print lst       
