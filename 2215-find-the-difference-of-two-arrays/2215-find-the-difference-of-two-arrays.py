class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # first_answer = []
        # second_answer = []
        
        # for num in nums1: 
        #     if num not in nums2 and num not in first_answer: 
        #         first_answer.append(num)
                
        # for num in nums2: 
        #     if num not in nums1 and num not in second_answer: 
        #         second_answer.append(num)

        # final_answer= []
        # final_answer.append(first_answer)
        # final_answer.append(second_answer)
        final_answer = []

        set1 = set(nums1) - set(nums2)
        set2 = set(nums2) - set(nums1)

        final_answer.append(set1)
        final_answer.append(set2)
        
        return final_answer