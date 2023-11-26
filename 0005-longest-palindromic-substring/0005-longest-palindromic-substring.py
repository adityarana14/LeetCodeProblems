class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # testing Odd length Palindrome 
        max_len = 1 
        final_string = s[0]
        for i in range(len(s)):
            j = i + 1 
            k = i - 1 
            leng = 1
            while k >= 0 and j < len(s):
                if s[j] == s[k]:
                    leng = leng + 2
                else: 
                    break
                
                k = k - 1 
                j = j + 1 
            
            if leng > max_len: 
                max_len = leng
                # print("I'm working 1")
                final_string = s[k+1 : j]
        
        for i in range(len(s)):
            j = i  
            k = i + 1 
            leng = 0 
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    j = j - 1 
                    k = k + 1 
                    leng = leng + 2
                else: 
                    break

             

            if leng > max_len: 
                max_len = leng 
                # print("I'm working 2 ")
                final_string = s[j + 1 : k]

        return final_string
                



        