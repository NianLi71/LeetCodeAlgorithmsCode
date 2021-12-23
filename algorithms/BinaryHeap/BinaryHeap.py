
class BinaryHeap:
    def __init__(self) -> None:
        self.heapList = [0] # reserve index 0
        self.currentSize = 0

    def buildHeap(alist):
        i = len(alist) // 2
        heap = BinaryHeap()
        heap.currentSize = len(alist)
        heap.heapList = [0] + alist[:]

        while i > 0:
            heap.percDown(i)
            i -= 1
        
        return heap

    def perUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                BinaryHeap.swap(self.heapList, i, i // 2)
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)

    def percDown(self, i):
        def getMinChildIndex(i):
            if i * 2 + 1 > self.currentSize:  # node i only has left child
                return i * 2
            else:
                if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                    return i * 2
                else:
                    return i * 2 + 1

        while i * 2 <= self.currentSize: # if i*2 > currentSize, that means i has no child any more
            minChildIndex = getMinChildIndex(i)
            if self.heapList[i] > self.heapList[minChildIndex]:
                BinaryHeap.swap(self.heapList, i, minChildIndex)
            i = minChildIndex


    def delMin(self):
        minValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return minValue

    def isEmpyt(self):
        return self.currentSize == 0


    def __str__(self) -> str:
        return str(self.heapList)

    def swap(a, i, j):
            a[i], a[j] = a[j], a[i]


if __name__ == '__main__':
    heap = BinaryHeap()

    for n in [9,5,4,2,3]:
        heap.insert(n)
        print(heap)
    
    while not heap.isEmpyt():
        print(f'min: {heap.delMin()}, current heap: {heap}')

    print('Build heap from list')
    heap2 = BinaryHeap.buildHeap([9,5,6,2,3])
    while not heap2.isEmpyt():
        print(f'min: {heap2.delMin()}, current heap: {heap2}')