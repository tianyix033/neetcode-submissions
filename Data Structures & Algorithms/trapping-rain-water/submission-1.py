class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        res = 0
        curr_lake = 0
        while right < len(height):
            if (height[right] < height[left]):
                curr_lake += height[left] - height[right]
                right += 1
            else:
                res += curr_lake
                curr_lake = 0
                left = right
                right += 1
        # at this point, left is at heighest point
        # now we reverse the traversal until that point
        right = len(height) - 1
        target = left
        left = right - 1
        curr_lake = 0
        while (left >= target):
            if (height[left] < height[right]):
                curr_lake += height[right] - height[left]
                left -= 1
            else:
                res += curr_lake
                curr_lake = 0
                right = left
                left -= 1
        return res

