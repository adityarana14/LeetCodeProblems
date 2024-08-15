class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict_bills = {}

        dict_bills[5] = 0 
        dict_bills[10] = 0 
        dict_bills[15] = 0 

        for bill in bills: 
            if bill == 5:
                dict_bills[5] += 1 
            elif bill == 10: 
                if dict_bills[5] >= 1:
                    dict_bills[5] -= 1 
                    dict_bills[10] += 1 
                else: 
                    return False 
            else: 
                if dict_bills[10] >= 1: 
                    if dict_bills[5] >= 1: 
                        dict_bills[10] -= 1 
                        dict_bills[5] -= 1 
                    else: 
                        return False 
                else: 
                    if dict_bills[5] >= 3: 
                        dict_bills[5] -= 3 
                    else: 
                        return False 

        return True 
