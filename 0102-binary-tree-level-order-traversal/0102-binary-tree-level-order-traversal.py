# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        stack_ele = deque()
        answer = []
        stack_ele.append(root)

        while stack_ele: 
            leng = len(stack_ele)
            temp_ans = []

            while leng:
                top = stack_ele.popleft()
                if top: 
                    temp_ans.append(top.val)
                    stack_ele.append(top.left)
                    stack_ele.append(top.right)
                leng = leng - 1 

            if temp_ans: 
                answer.append(temp_ans)


        return answer