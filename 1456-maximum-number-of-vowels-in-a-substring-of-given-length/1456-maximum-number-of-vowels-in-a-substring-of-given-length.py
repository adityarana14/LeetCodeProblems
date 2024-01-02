class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        answer = 0
        count = 0 
        for i in range(0,k):
            if s[i] in vowels: 
                count = count + 1 
        
        answer = count 
        j = k 
        i = 0 
        while j != len(s):
            if s[j] in vowels: 
                count = count + 1
            if s[i] in vowels: 
                count = count - 1 
            if count > answer: 
                answer = count   
            i = i + 1 
            j = j + 1 


        return answer

            