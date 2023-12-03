class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True 
        number = x 
        reverse_number = 0 
        if x < 0: 
            x = -x 

        while x != 0:
            last = x % 10
            reverse_number = reverse_number * 10 + last 
            x = x // 10 
        

        if number == reverse_number: 
            return True 
        else: 
            return False
        