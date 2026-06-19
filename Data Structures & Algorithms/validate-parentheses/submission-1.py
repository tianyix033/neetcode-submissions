class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lst = list(s)
        for char in lst:
            match char:
                case '(' | '[' | '{':
                    stack.append(char)
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
        return len(stack) == 0