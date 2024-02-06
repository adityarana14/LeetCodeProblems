class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        a = set()
        
        answer = 0 
        max_answer = 0 

        left = 0 


        for char in s: 
            if char not in a: 
                a.add(char)
                answer = answer + 1 
                if answer > max_answer: 
                    max_answer = answer
            else: 
                while char in a: 
                    a.remove(s[left])
                    left = left + 1 
                    answer = answer - 1 
                
                a.add(char)
                answer = answer + 1 
                if answer > max_answer: 
                    max_answer = answer 

        return max_answer 


        
        
        