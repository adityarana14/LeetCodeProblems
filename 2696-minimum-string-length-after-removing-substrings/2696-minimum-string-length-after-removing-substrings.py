class Solution:
    def minLength(self, s: str) -> int:
        
        dq = deque()

        for i in range(len(s)):
            dq.append(s[i])
            while len(dq) >= 2 and ((dq[-2] == "A" and dq[-1] == "B") or (dq[-2] == "C" and dq[-1] == "D")):
                dq.pop()
                dq.pop()

        return len(dq)
        
        
        