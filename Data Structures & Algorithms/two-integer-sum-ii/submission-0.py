class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #! remember 1 indexed!
        pos = len(numbers)
        my_dict = {}
        while numbers:
            num = numbers.pop()
            if num in my_dict:
                return [pos, my_dict[num]]
            my_dict[target - num] = pos
            pos -= 1

        return [-1, -1]
            