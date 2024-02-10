from collections import defaultdict
class Solution:

    def checkValid(self, dict1, dict2):
        flag = 1 
        for key in dict2: 
            if key not in dict1:
                flag = 0  
                break 
            if dict1[key] < dict2[key]:
                flag = 0 
                break 

        if flag == 1: 
            return True
        else: 
            return False  
    
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        answer = ""

        for val in t: 
            t_dict[val] += 1 

        left = 0 
        right = len(t) - 1 

        for i in range(len(t)):
            s_dict[s[i]] += 1 

        
        while right < len(s):
            # print(f"First check left = {left} and right = {right} s_dict {s_dict}.  t_dict {t_dict} and answer {answer}")
            while self.checkValid(s_dict, t_dict):
                if len(answer) == 0: 
                    answer = s[left:right+1]
                    # print(f"len of answer = 0 and left is {left} and right is {right} and string is {s[left:right]}")
                if len(answer) > right - left + 1: 
                    answer = s[left:right+1]
                
                s_dict[s[left]] -= 1 
                left = left + 1
                
            
            right = right + 1 
            if right < len(s):
                s_dict[s[right]] += 1 

        return answer
