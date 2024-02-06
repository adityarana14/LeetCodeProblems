from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_str = defaultdict(int)

        left = 0 
        right = 0 
        result = 0 

        while right < len(s): 
            dict_str[s[right]] += 1

            while ((right - left + 1 ) - max(dict_str.values())) > k: 
                dict_str[s[left]] -= 1
                left = left + 1 
            
            result = max(result, right-left+1)
            right = right + 1 

        return result 


        

        