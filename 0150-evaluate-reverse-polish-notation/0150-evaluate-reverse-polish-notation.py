from collections import deque 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        answer = 0 
        symbols = ['+', '-', '*', '/']
        for val in tokens: 
            if val not in symbols: 
                stack.append(int(val))
            else: 
                val1 = stack.pop()
                val2 = stack.pop()
                if val == "+":
                    answer =  val1 + val2
                if val == '-':
                    answer =  val2 - val1 
                if val == '*':
                    answer = (val1 * val2)
                if val == '/':
                    answer =  int(val2 / val1)
                stack.append(answer)
                print(answer)

        if stack: 
            return stack.pop()
        return answer
        