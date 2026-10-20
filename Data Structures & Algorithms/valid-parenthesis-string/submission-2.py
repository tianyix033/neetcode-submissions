class Solution:
    def checkValidString(self, s: str) -> bool:
        maxLefts = 0
        minLefts = 0
        for c in s:
            match c:
                case '(':
                    maxLefts += 1
                    minLefts += 1
                case '*':
                    maxLefts += 1
                    minLefts = max(0, minLefts - 1)
                case ')':
                    maxLefts -= 1
                    minLefts = max(0, minLefts - 1)
                    if maxLefts < 0:
                        return False
        return minLefts == 0