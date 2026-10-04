import bisect
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.data, num)

    def findMedian(self) -> float:
        if len(self.data) % 2 == 1:
            return self.data[len(self.data) // 2]
        else:
            return (self.data[len(self.data) // 2 - 1] + self.data[len(self.data) // 2]) / 2
        