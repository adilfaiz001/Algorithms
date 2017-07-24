'''
Created on Feb 9, 2017

@author: Rahil
'''
#Building MaxHeap and maintaining MAX-HEAP property of heap

def Parent(i):
    return i>>1
def Left_Child(i):
    return i<<1
def Right_Child(i,size):
    if  ((i<<1)+1)>(size-1):
        return i<<1
    else:
        return (i<<1)+1

#MAX-HEAP
def Max_Heapify(A,i):
    heap_sizeA=len(A)
    l=Left_Child(i)
    r=Right_Child(i,heap_sizeA)
    print l,r
    largest=0
    if l<=heap_sizeA and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<=heap_sizeA and A[r]>A[largest]:
        largest=r
    if largest != i:
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        Max_Heapify(A, largest)
    
        
def Build_MaxHeap(A):
    heap_size=len(A)
    i=int(heap_size/2)
    while i>=1:
        print i
        Max_Heapify(A, i)
        i-=1

def Heapsort(A):
    Build_MaxHeap(A)
    print A
    i=len(A)-1
    while i>=1:
        print i
        temp=A[1]
        A[1]=A[i]
        A[i]=temp
        print A.pop()
        Max_Heapify(A, 1)
        i-=1
                
lst=[4,1,3,2,16,9,10,14,8,7]
lst.insert(0, 0)
Build_MaxHeap(lst)
Heapsort(lst)
print lst
    