from collections import deque 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        answer = []
        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                stack.append(i)
                answer.append(0)
            else:
                while stack and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                if stack:
                    answer.append(stack[-1]-i)
                else: 
                    answer.append(0)
                stack.append(i) 

        
        answer = reversed(answer)
        return answer