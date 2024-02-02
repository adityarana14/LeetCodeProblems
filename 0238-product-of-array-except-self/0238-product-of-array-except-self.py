class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1 
        # flag = 0 
        # for i in nums:
        #     if flag == 1 and i == 0 :
        #         product = 0 
        #         continue 

        #     if i == 0: 
        #         flag = 1  
        #         continue 
            
        #     product = product * i 
        
        # temp_answer = []

        # for j in nums: 
        #     if flag == 1 and j != 0: 
        #         temp_answer.append(0)
        #         continue 
        #     if j == 0: 
        #         temp_answer.append(int(product))
        #     else: 
        #         temp_answer.append(int(product/j))

        
        # return temp_answer

        prefix_sum = [0] * len(nums)
        postfix_sum = [0] * len(nums)

        result = [0] * len(nums)

        for i, val in enumerate(nums):
            if i == 0: 
                prefix_sum[i] = nums[i]
            else: 
                prefix_sum[i] = nums[i] * prefix_sum[i-1]

        for j in range(len(nums) -1, -1, -1):
            if j == len(nums) -1: 
                postfix_sum[j] = nums[j]
            else: 
                postfix_sum[j] = nums[j] * postfix_sum[j+1]

        print(prefix_sum)
        print(postfix_sum)

        for i, val in enumerate(result): 
            if i == 0: 
                result[i] = postfix_sum[i+1]
            elif i == len(result) - 1:
                result[i] = prefix_sum[i-1]
            else: 
                result[i] = prefix_sum[i-1] * postfix_sum[i+1]

        return result 


        