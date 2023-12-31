class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = 0
        # len_nums = len(nums)
        # count = 0   
        # for i, num in enumerate(nums):  
        #     if num != 0: 
        #         nums[k] = num 
        #         k = k + 1 
        #         count = count + 1 
        # for j in range(count, len(nums)):
        #     nums[j] = 0 

        # print(nums)

        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j = j + 1 


        