class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        i = 0 
        j = len(s) -1 
        while i<j: 
            while (not ((ord('a') <= ord(s[i]) and ord('z') >= ord(s[i])) or ord('0') <= ord(s[i]) and ord('9')>=ord(s[i]))) and i<j:
                i = i + 1 
            while (not ((ord('a') <= ord(s[j]) and ord('z') >= ord(s[j])) or ord('0') <= ord(s[j]) and ord('9')>=ord(s[j]))) and i<j:
                j = j - 1 

            if i < len(s) and j >= 0: 
                if s[i] != s[j]: 
                    return False
            i, j = i + 1 , j -1 



        return True 
        