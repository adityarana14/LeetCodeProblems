from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        # it's a stack question that's an important hint for anyone to solve such problems 

        stack = deque()
        for val in s: 
            if val == "*":
                stack.pop()
            else: 
                stack.append(val)

        answer = []

        while len(stack) != 0:
            val = stack.pop()
            answer.append(val)

        answer = reversed(answer)

        return "".join(answer)


        