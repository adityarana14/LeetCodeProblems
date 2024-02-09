from collections import defaultdict 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False 
            
        s1_dict = defaultdict(int) 
        s2_dict = defaultdict(int)

        for val in s1:
            s1_dict[val] += 1

        for i in range(len(s1)):
            s2_dict[s2[i]] += 1  
        
        print(f"Initial s2 String {s2_dict}")

        left = 0 
        right = len(s1) - 1
         

        while right < len(s2):
            flag = 1

            print(f"left: {left}. right {right}")
            for key, val in s1_dict.items():
                if s1_dict[key] != s2_dict[key]:
                    flag = 0
                    break
            if flag == 1:
                print(f"left : {left}. right: {right}.  s1_dict: {s1_dict}. s2_dict:  {s2_dict}. ")
                return True 
            else: 
                right = right + 1
                if right < len(s2):
                    s2_dict[s2[right]] += 1
                    s2_dict[s2[left]] -= 1
                    left = left + 1
                else: 
                    return False

        return False


        