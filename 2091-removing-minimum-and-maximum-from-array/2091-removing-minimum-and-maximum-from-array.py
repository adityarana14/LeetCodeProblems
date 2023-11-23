class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minEle , maxEle = nums[0], nums[0]
        indexMin = 0
        indexMax = 0
        for i in range(1, len(nums)):
            if nums[i] > maxEle:
                maxEle = nums[i]
                indexMax = i
            elif nums[i] < minEle:
                minEle = nums[i]
                indexMin = i
        # Deleting From Front 
        num1 = max(indexMin + 1 , indexMax + 1)
        # Deleting From Back 
        num2 = max(len(nums) - indexMin, len(nums) - indexMax)
        # Deleting One from Front and another From Back 
        num3 = min(indexMin + 1, indexMax + 1) + min(len(nums) - indexMin, len(nums) - indexMax)
        
        
        return min(min(num1, num2), num3)
        # count = 0
        # flagMin = 0
        # flagMax = 0
        # numsLen = len(nums)
        # minEleCount = indexMin if numsLen - indexMin > indexMin else numsLen - indexMin 
        # if minEleCount != indexMin: 
        #     flagMin = 1 
        # maxEleCount = indexMax + 1 if numsLen - indexMax > indexMax else numsLen - indexMax + 1 
        # if maxEleCount != indexMax:
        #     flagMax = 1

        # tempNums = []
        # if minEleCount <= maxEleCount:
        #     if flagMin == 0:
        #         tempNums = nums[minEleCount:]
        #     else: 
        #         tempNums = nums[:minEleCount]

        # else: 
        #     if flagMax == 0:
        #         tempNums = nums[maxEleCount:]
        #     else: 
        #         tempNums = nums[:maxEleCount]

        # print(tempNums)
        
            
        