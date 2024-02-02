class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_count = {}
        c = [[] for i in range(len(nums) + 1)]

        for val in nums: 
            if val in dict_count: 
                dict_count[val] += 1 
            else: 
                dict_count[val] = 1 

        for key, val in dict_count.items():
            c[val].append(key)

        answer = []
        
        for i in range(len(nums), -1, -1):
            if c[i]:
                for val in c[i]:
                    answer.append(val)
                if len(answer) == k: 
                    return answer
        

        
        