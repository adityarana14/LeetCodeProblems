# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: 
            return []

        queue1 = deque()

        queue1.append(root)
        result = []
        while queue1: 
            
            queue2 = deque()
            prev = -1 
            while queue1: 
                temp = queue1[0]

                if temp.left: 
                    queue2.append(temp.left)
                if temp.right: 
                    queue2.append(temp.right)
                
                prev = temp

                queue1.popleft()
            
            queue1 = queue2 
            result.append(temp.val)   

            
        return result



        

        