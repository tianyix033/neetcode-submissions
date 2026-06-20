class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                pos, height = stack.pop()
                res = max(res, height * (i - pos))
                start = pos
            stack.append((start, h))
        while stack:
            pos, height = stack.pop()
            res = max(res, height * (len(heights) - pos))
        return res
            