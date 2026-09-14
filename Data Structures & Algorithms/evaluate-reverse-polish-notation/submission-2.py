class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                match token:
                    case '+':
                        a = int(stack.pop())
                        b = int(stack.pop())
                        result = b + a
                        stack.append(result)
                    case '-':
                        a = stack.pop()
                        b = stack.pop()
                        result = b - a
                        stack.append(result)
                    case '*':
                        a = stack.pop()
                        b = stack.pop()
                        result = b * a
                        stack.append(result)
                    case '/':
                        a = stack.pop()
                        b = stack.pop()
                        result = int(b/a)
                        stack.append(result)
        return stack[0]