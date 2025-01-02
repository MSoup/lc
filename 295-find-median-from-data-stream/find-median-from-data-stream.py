import heapq

class MedianFinder:
    def __init__(self):
        self.smallNumList = []        
        self.largeNumList = []        

    def addNum(self, num: int) -> None:
        if not self.smallNumList or -self.smallNumList[0] >= num:
            heapq.heappush(self.smallNumList, -num)
        else:
            heapq.heappush(self.largeNumList, num)

        # balance bc smallNumList will have 1 more el or they will be equal in elements
        if len(self.smallNumList) > len(self.largeNumList) + 1:
            heapq.heappush(self.largeNumList, -heapq.heappop(self.smallNumList))
        elif len(self.smallNumList) < len(self.largeNumList):
            heapq.heappush(self.smallNumList, -heapq.heappop(self.largeNumList))
        
    def findMedian(self) -> float:
        if not (self.largeNumList and self.smallNumList):
            return -self.smallNumList[0]
        # The median of all the numbers will either be 
        # the largest number in the smallNumList 
        # or the smallest number in the largeNumList
        if (len(self.largeNumList) + len(self.smallNumList)) % 2 == 0:
            return (self.largeNumList[0] / 2 + -self.smallNumList[0] / 2)
        return -self.smallNumList[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()