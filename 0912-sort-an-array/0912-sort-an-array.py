class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # if len(nums) == 1:
        #     return nums
        # first = nums[0]
        # tempNums = nums[1:]
        # sortNums = self.sortArray(tempNums)
        # # print(f"First {first}.  tempNums = {tempNums}")
        # nums[:] = self.insertionInSortedArray(first, tempNums)
        # # print(nums)
        
        # return nums 

        return sorted(nums)

    

    def insertionInSortedArray(self, num, sorted_list):
        # if ele > sortedArray[len(sortedArray) - 1]:
        #     sortedArray.insert(len(sortedArray), ele )
        #     return sortedArray

        # if ele < sortedArray[0]:
        #     sortedArray.insert(0,ele)
        #     return sortedArray

        # left = 0 
        # right = len(sortedArray)
        # mid = 0
        # while(left<right):
        #     mid = (left + right) // 2
        #     if sortedArray[mid] == ele:
        #         sortedArray.insert(mid, ele)
        #         return sortedArray         
        #     elif sortedArray[mid] < ele:
        #         left = mid + 1
        #     else:
        #         right = mid - 1 

        # sortedArray.insert(left , ele)
        # # sortedArray.append(ele)
        # # sortedArray = sorted(sortedArray)
        # return sortedArray

        
        # left, right = 0, len(sorted_list) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if sorted_list[mid] < num:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # sorted_list.insert(left, num)
        return sorted_list
        
        