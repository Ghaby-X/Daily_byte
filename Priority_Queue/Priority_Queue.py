import math

# priority value is the minimum value
# must obey tree completeness
# parent of a tree
class Heap:
    def __init__(self) -> None:
        self.queue = []
        
    def insert(self, num: int):
        if self.isEmpty():
            self.queue.append(num)
            return
        
        self.queue.append(num)
        
        last_idx = len(self.queue) - 1
        self._upheap(last_idx)
    
        pass
    
    def remove(self):
        if self.isEmpty():
            print('Heap is empty, cannot remove element')
            return
        
        rmv = self.queue[0]
        last_idx = len(self.queue) - 1
        self.__swap(0, last_idx)
        self.queue = self.queue[:-1]
        
        self._downheap()
        
        print("removed: ",rmv)
        return rmv
    
    def to_list(self):
        print(self.queue)
        return self.queue.copy()
    
    def peek(self):
        if self.isEmpty():
            print('Heap is empty')
        
        print(self.queue[0])
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def __swap(self, idx1, idx2):
        temp = self.queue[idx1]
        self.queue[idx1] = self.queue[idx2]
        self.queue[idx2] = temp
    
    def __parent(self, idx: int):
        # returns the index of the parent of any node assuming a complete binary tree
        if idx == 0:
            raise IndexError('base index does not have a parent')
        
        return math.floor(((idx + 1)/ 2) - 1)
        
    def __left(self, idx: int):
        # returns the index of the left child of the provided index for a complete binary tree
        return (2*idx + 1)
    
    def __right(self, idx: int):
        # returns the index of the right child of the provided index for a complete binary tree
        return (2*idx + 2)
    
    def _upheap(self, idx):
        while idx > 0:
            parent_idx = self.__parent(idx)
        
            if self.queue[idx] <= self.queue[parent_idx]:
                break
                
            self.__swap(idx, parent_idx)
            idx = parent_idx
    
    def _downheap(self, idx = 0):
        length = len(self.queue)
        left = self.__left(idx)
        right = self.__right(idx)
        
        while left < length or right < length:
            left = self.__left(idx)
            right = self.__right(idx)
            
            if left > length - 1:
                break
            
            if self.queue[right] > self.queue[left] and right < length:
                min_index = right
            else:
                min_index = left
                
            self.__swap(idx, min_index)
            idx = min_index

    

# implemetation of max heap
class maxHeap(Heap):
    pass

# implementation of min heap
class minHeap(Heap):
    def heapify(self, array: list):
        last_idx = len(array) - 1
        self.queue = array
        
        for i in range(last_idx, -1, -1):
            self._downheap(i)
            pass
        pass
    
    def _downheap(self, idx=0):
        length = len(self.queue)
        left = self._Heap__left(idx)
        right = self._Heap__right(idx)
        
        while left < length or right < length:
            left = self._Heap__left(idx)
            right = self._Heap__right(idx)
            
            if left > length - 1:
                break
            
            if right < length and self.queue[right] > self.queue[left]:
                min_index = left
            else:
                min_index = right
                
            self._Heap__swap(idx, min_index)
            idx = min_index
    
    def _upheap(self, idx):
        while idx > 0:
            parent_idx = self._Heap__parent(idx)
        
            if self.queue[idx] >= self.queue[parent_idx]:
                break
                
            self._Heap__swap(idx, parent_idx)
            idx = parent_idx

# heap = minHeap()
# heap.insert(3)
# heap.insert(10)
# heap.insert(8)
# heap.insert(14)
# heap.insert(5)
# heap.insert(25)
# heap.remove()
# heap.insert(0)
# heap.peek() # removes max which is 25
# heap.to_list()

heap =minHeap()

heap.heapify([1,2,3,4,5,6])
heap.to_list()