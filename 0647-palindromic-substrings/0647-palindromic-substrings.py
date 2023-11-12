class Solution:

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1):
            print(s[i])
            count = count + 1
            for j in range(i+1, len(s)):
                
                check = self.isPalindrome(str(s[i:j+1]))
                if(check):
                    # print(s[i:j+1])
                    count = count + 1

        return count + 1 

    def isPalindrome(self, s : str):
        
        
        return s == s[::-1]