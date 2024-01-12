# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxCount = 0

    def longestCount(self, root, status, count):

        count = count + 1 
        # print(f"root : {root.val}, status: {status}  count : {count}. maxCount : {self.maxCount}")

        if count > self.maxCount: 
            self.maxCount = count 

        if status == True: 
            if root.left: 
                status = False
                self.longestCount(root.left, status, count)
        else:
            if root.right: 
                status = True
                self.longestCount(root.right, status, count)
                

        # if status == True: 
        #     status = False
        #     if root.left:
        #         count = count + 1 
        #         self.longestCount(root.left, status, count)
        #     if root.right:
        #         count = count + 1 
        #         self.longestCount(root.right, status, count)
        # if status == False: 
        #     status = True
        #     if root.right:
        #         count = count + 1 
        #         self.longestCount(root.right, status, count)
        #     if root.left:
        #         count = count + 1 
        #         self.longestCount(root.left, status, count)

        #return count
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_co = 0 
        # self.longestCount(root, True, -1)
        # self.longestCount(root, False, -1)

        # self.longestZigZag(root.left)
        # self.longestZigZag(root.right)
        def dfs(root, left, right):

            if root == None: 
                return self.max_co
            
            self.max_co = max(self.max_co, left, right)

            dfs(root.left, right + 1, 0)
            dfs(root.right, 0, left + 1)

            return self.max_co

        return dfs(root, 0, 0)
        