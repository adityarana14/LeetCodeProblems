# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0 
        right = n 
        mid = (left + right) // 2 
        flag = True 
        while True: 
            val = guess(mid)
            if val == 0: 
                return mid
            elif val == -1: 
                right = mid - 1  
                mid = (left + right) // 2      
            else:
                left = mid + 1  
                mid = (left + right) // 2 
                
            

         
        