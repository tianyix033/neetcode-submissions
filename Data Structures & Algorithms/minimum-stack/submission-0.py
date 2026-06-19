class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        newMin = min(self.getMin(), val) if self.min_stack else val
        self.min_stack.append(newMin)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.data.pop()   

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
