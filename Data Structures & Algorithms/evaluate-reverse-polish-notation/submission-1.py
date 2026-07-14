class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):

            if tokens[i] == "+":
                first = stack.pop()
                second = stack.pop()
                total = second + first
                stack.append(int(total))
            elif tokens[i] == "-":
                first = stack.pop()
                second = stack.pop()
                total = second - first
                stack.append(int(total))
            elif tokens[i] == "*":
                first = stack.pop()
                second = stack.pop()
                total = second * first
                stack.append(int(total))
            elif tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()
                total = second / first
                stack.append(int(total))
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()


        