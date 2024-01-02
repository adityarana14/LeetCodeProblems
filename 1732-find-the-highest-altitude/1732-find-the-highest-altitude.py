class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]
        val = 0 
        for i in gain: 
            val = val + i 
            answer.append(val)
        
        return max(answer)