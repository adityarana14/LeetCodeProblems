class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = (sorted(nums))
        print(nums)
        for i, val in enumerate(nums): 
            if i != 0: 
                if nums[i] == nums[i-1]:
                    i = i + 1
                    continue
            j = i + 1 
            k = len(nums) - 1
            sum_cal = 0
            while j<k:
                sum_cal = val + nums[j] + nums[k]
                # print(f"{sum_cal} {i} {j} {k}")
                if sum_cal == 0: 
                    answer.append([val, nums[j], nums[k]])
                    j = j + 1       
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j = j + 1 

                elif sum_cal > 0: 
                    k = k - 1 
                else: 
                    j = j + 1 

        return answer
                    





        