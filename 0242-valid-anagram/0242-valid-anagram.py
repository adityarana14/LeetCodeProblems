class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_anagram = {}

        for val in s: 
            if val in dict_anagram: 
                dict_anagram[val] += 1 
            else: 
                dict_anagram[val] = 1 
        
        for val in t: 
            if val in dict_anagram: 
                dict_anagram[val] -= 1 
            else: 
                return False 

        for key in dict_anagram: 
            if dict_anagram[key] != 0: 
                return False 

        return True 
        