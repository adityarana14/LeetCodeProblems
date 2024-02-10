from collections import deque 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for val in s: 
            if not stack: 
                stack.append(val)
            else: 
                if val == ')':
                    rm = stack.pop()
                    if rm != '(':
                        return False
                elif val == ']':
                    rm = stack.pop()
                    if rm != '[':
                        return False
                elif val == '}':
                    rm = stack.pop()
                    if rm != '{':
                        return False
                elif val == '(':
                    stack.append(val)
                elif val == '[':
                    stack.append(val)
                elif val == '{':
                    stack.append(val)

        if stack: 
            return False 
        return True 



                
        