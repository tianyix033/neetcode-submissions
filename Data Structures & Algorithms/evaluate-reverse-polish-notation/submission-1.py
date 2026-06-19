class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operate(stack, operator):
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            match operator:
                case '+':
                    stack.append(operand1 + operand2)
                case '-':
                    stack.append(operand1 - operand2)
                case '*':
                    stack.append(operand1 * operand2)
                case '/':
                    stack.append(operand1 / operand2)
                case _:
                    raise Exception('This should not happen.')

        my_stack = []
        OPERATOR = {'+', '-', '*', '/'}
        for token in tokens:
            if token in OPERATOR:
                operate(my_stack, token)
            else:
                my_stack.append(token)
        return int(my_stack[0])
