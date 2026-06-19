class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = []
        res = [0] * len(temperatures)
        for i, val in enumerate(reversed(temperatures)):
            while my_stack:
                if my_stack[-1][0] <= val:
                    dummy, size = my_stack.pop()
                    if my_stack:
                        my_stack[-1][1] += size 
                else:
                    break  
            if my_stack:  # there are warmer days later
                res[i] = my_stack[-1][1]
            else:
                res[i] = 0
            my_stack.append([val, 1])
        res.reverse()
        return res

        