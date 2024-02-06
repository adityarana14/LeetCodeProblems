class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = [0] * len(height) 
        right_max = [0] * len(height)
        maxl = height[0] 

        for i in range(1, len(height)):            
            left_max[i] = maxl
            if height[i] > maxl: 
                maxl = height[i]
        maxr = height[len(height)-1]
        for j in range(len(height) - 2, -1, -1):
            right_max[j] = maxr 
            if height[j] > maxr:
                maxr = height[j]
        answer = 0 
        for i in range(len(left_max)):
            trap_water = min(left_max[i], right_max[i]) - height[i]
            if trap_water > 0: 
                answer = answer + trap_water


        return answer


