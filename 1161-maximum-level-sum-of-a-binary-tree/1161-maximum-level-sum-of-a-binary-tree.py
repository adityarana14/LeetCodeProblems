# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 1

        if not root.left and not root.right: 
            return 1 

        max_sum = root.val 
        level = 1
        final_level = 1  

        queue1 = deque()
        queue1.append(root)
        
        while queue1: 
            queue2 = deque()
            temp_sum = 0
            flag = 0 
            level = level + 1 
            while queue1: 
                temp = queue1[0]

                if temp.left: 
                    temp_sum = temp_sum + temp.left.val
                    flag = 1
                    queue2.append(temp.left)
                if temp.right: 
                    temp_sum = temp_sum + temp.right.val 
                    flag = 1
                    queue2.append(temp.right)

                queue1.popleft()
            
            queue1 = queue2
            print(temp_sum)
            if temp_sum > max_sum and flag == 1: 
                max_sum = temp_sum 
                final_level = level 

        return final_level 

