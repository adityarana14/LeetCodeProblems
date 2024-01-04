from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = deque()

        for val in asteroids: 
            if len(stack) == 0: 
                stack.append(val)
            else:
                top = stack[-1]
                if top > 0 and val < 0:
                    if abs(top) < abs(val):  
                        stack.pop()
                        stack.append(val)
                    elif abs(top) == abs(val):
                        stack.pop()
                else:
                    stack.append(val)
                    
                

                flag = 1 
                while flag == 1 and len(stack) > 1 : 
                    top = stack.pop()
                   
                    if top < 0 and stack[-1] > 0:
                        if abs(top) > abs(stack[-1]):
                            stack.pop()
                            stack.append(top)
                        elif abs(top) == abs(stack[-1]):
                            stack.pop()                                      
                    else:
                        stack.append(top)    
                        flag = 0         


        answer = []
        while len(stack) != 0:
            top = stack.pop()
            answer.append(top)
        
        print(answer)
        return reversed(answer)





            

        