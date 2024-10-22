# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = []

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.level_order_traversal(root)
        heapq.heapify(self.answer)

        while self.answer and k-1: 
            heapq.heappop(self.answer)
            k = k - 1 

        return -1 * self.answer[0] if self.answer else -1

    def level_order_traversal(self, root):
        if not root: 
            return 

        dq = deque()
        dq.append(root)

        while dq: 
            len_dq = len(dq)
            temp_sum = 0

            for i in range(len_dq):
                top = dq.popleft()
                temp_sum += top.val

                if top.left: 
                    dq.append(top.left)
                if top.right: 
                    dq.append(top.right)

            self.answer.append(-1 * temp_sum)
            
