from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left/right))
                continue
            if token == "+":
                stack.append(stack.pop()+stack.pop())
                continue
            if token == "*":
                stack.append(stack.pop() * stack.pop())
                continue
            if token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
                continue
            stack.append(int(token))
        return stack.pop()

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))