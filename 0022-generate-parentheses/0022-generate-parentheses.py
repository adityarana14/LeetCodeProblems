class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answer = []
        
        def generate(close, open): 
            if close == open and close == n: 
                answer.append("".join(stack))
                return 
            
            if open < n: 
                stack.append('(')
                generate(close, open + 1)
                stack.pop()
            
            if close < open: 
                stack.append(')')
                generate(close + 1, open)
                stack.pop()
            
        generate(0,0)
        return answer

        