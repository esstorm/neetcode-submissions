from collections import deque
from functools import reduce
from operator import add, sub, mul, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        tokens = deque(tokens)
        stack = []

        operator = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }

        while tokens:
            token = tokens.popleft()

            if token not in "+-*/":
               stack.append(token) 
               continue

            right = stack.pop()
            left = stack.pop()
            stack.append(operator[token](int(left), int(right)))

        return int(stack.pop())


