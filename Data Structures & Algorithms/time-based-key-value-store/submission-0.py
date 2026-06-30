class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or self.data[key][0][0] > timestamp:
            return ""
        history = self.data[key]
        left = 0
        right = len(history) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if history[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return history[left][1]
