class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0 
        negative = False
        flag = 0 
        start = False 
        for _ in s: 
            if _ == ' ' and start == False and flag == 0:
                continue
            elif ord(_) >= ord('0') and ord(_) <= ord('9'):
                answer = answer * 10 + int(_)
                start = True
            elif ord(_) == ord('-') and answer == 0 and flag == 0 and start == False:
                negative = True
                flag = 1 
            elif ord(_) == ord('+') and negative == False and flag == 0 and start == False:
                flag = 1
                continue
            else: 
                break
        
        if negative == True: 
            answer  = -answer
        
        if answer > 2 ** 31 - 1: 
            return 2 ** 31 -1
        if answer < - 2 ** 31: 
            return -2 ** 31
        

        
        return answer 