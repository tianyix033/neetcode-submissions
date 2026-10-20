class Solution:
    def checkValidString(self, s: str) -> bool:
        numLefts, numStars = 0, 0
        for c in s:
            if c == '(':
                numLefts += 1
            elif c == '*':
                numStars += 1
            else:   # c == ')'
                if numLefts > 0:
                    numLefts -= 1
                elif numStars > 0:
                    numStars -= 1
                else:
                    return False
        numRights, numStars = 0, 0
        for c in s[::-1]:
            if c == ')':
                numRights += 1
            elif c == '*':
                numStars += 1
            else:
                if numRights > 0:
                    numRights -= 1
                elif numStars > 0:
                    numStars -= 1
                else:
                    return False
                    
        return True
