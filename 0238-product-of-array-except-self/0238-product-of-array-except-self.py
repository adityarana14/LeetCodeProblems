class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        flag = 0 
        for i in nums:
            if flag == 1 and i == 0 :
                product = 0 
                continue 

            if i == 0: 
                flag = 1  
                continue 
            
            product = product * i 
        
        temp_answer = []

        for j in nums: 
            if flag == 1 and j != 0: 
                temp_answer.append(0)
                continue 
            if j == 0: 
                temp_answer.append(int(product))
            else: 
                temp_answer.append(int(product/j))

        
        return temp_answer
        