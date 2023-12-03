class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            
            negative = True 
            x = -x

        answer = 0 
        while x != 0:
            rem = x % 10 
            answer = answer * 10 + rem 
            x = x // 10 
 
        if negative == True: 
            answer = -1 * answer


        if answer > 2 ** 31 - 1 or answer < -2 ** 31:
            return 0 
        
        return answer
        