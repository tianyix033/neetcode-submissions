class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helper(left, right):
            print(left, right)
            if left == right:
                return heights[left]
            mid_left = (left + right) // 2
            mid_right = mid_left + 1
            curr_max = 0
            curr_height = float('inf')
            while mid_left >= left or mid_right <= right:
                if mid_right > right:
                    curr_height = min(curr_height, heights[mid_left])
                    curr_max = max(curr_max, curr_height * (mid_right - mid_left))
                    mid_left -= 1
                elif mid_left < left:
                    curr_height = min(curr_height, heights[mid_right])
                    curr_max = max(curr_max, curr_height * (mid_right - mid_left))
                    mid_right += 1
                elif heights[mid_left] > heights[mid_right]:
                    curr_height = min(curr_height, heights[mid_left])
                    curr_max = max(curr_max, curr_height * (mid_right - mid_left))
                    mid_left -= 1
                else:
                    curr_height = min(curr_height, heights[mid_right])
                    curr_max = max(curr_max, curr_height * (mid_right - mid_left))
                    mid_right += 1
            
            mid_left = (left + right) // 2
            res = max(curr_max, helper(left, mid_left), helper(mid_left + 1, right))
            print(res)
            return res

        return helper(0, len(heights) - 1)

            
