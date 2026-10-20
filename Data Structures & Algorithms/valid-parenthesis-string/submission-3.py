class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        for i, c in enumerate(s):
            match c:
                case '(':
                    leftStack.append(i)
                case '*':
                    starStack.append(i)
                case ')':
                    if leftStack:
                        leftStack.pop()
                    elif starStack:
                        starStack.pop()
                    else:
                        return False

        while starStack and leftStack:
            right = leftStack.pop()
            rightStar = starStack.pop()
            if right > rightStar:
                return False
        
        return len(leftStack) == 0