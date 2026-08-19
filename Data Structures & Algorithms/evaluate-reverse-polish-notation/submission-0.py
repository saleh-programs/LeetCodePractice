class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {'+','-','*','/'}
        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                match ch:
                    case '+':
                        result = operand1 + operand2
                    case '-':
                        result = operand1 - operand2
                    case '*':
                        result = operand1 * operand2
                    case '/':
                        result = int(operand1 / operand2)
                stack.append(result)
        return stack[-1]