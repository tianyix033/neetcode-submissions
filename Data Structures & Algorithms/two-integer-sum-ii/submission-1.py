class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            match curr_sum:
                case x if x == target:
                    return [left + 1, right + 1]
                case x if x > target:
                    right -= 1
                case x if x < target:
                    left += 1
        
        return [-1, -1]