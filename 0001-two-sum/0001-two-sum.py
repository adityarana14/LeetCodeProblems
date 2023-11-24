class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index_list = []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1 , len(nums)):
        #         if nums[i] + nums[j] == target:
        #             index_list.append(i)
        #             index_list.append(j)
        #             return index_list

        # return [0,0]
        cache_dict = {}

        for i, num  in enumerate(nums): 
            rest = target - num 
            if rest in cache_dict: 
                return [cache_dict[rest], i]
            cache_dict[num] = i 
        print(cache_dict)
        return [0,0]
