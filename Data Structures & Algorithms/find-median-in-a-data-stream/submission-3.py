import heapq
class MedianFinder:

    def __init__(self):
        self.lower = []     # max heap
        self.higher = []    # min heap

    def addNum(self, num: int) -> None:
        # if (not self.lower and not self.higher) or (self.lower and num < self.lower[0]) or (self.higher and num < self.higher[0]):
        if self.lower and num < self.lower[0]:
            heapq.heappush_max(self.lower, num)
            if len(self.lower) - len(self.higher) > 1:
                val = heapq.heappop_max(self.lower)
                heapq.heappush(self.higher, val)
        else:
            heapq.heappush(self.higher, num)
            if len(self.higher) > len(self.lower):
                val = heapq.heappop(self.higher)
                heapq.heappush_max(self.lower, val)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return self.lower[0]
        else:
            return (self.lower[0] + self.higher[0]) / 2
        