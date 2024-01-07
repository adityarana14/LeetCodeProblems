# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        if head.next == None: 
            newNode = ListNode( "", None)
            return newNode

        length = 0 
        p = head 
        while(p != None):
            length = length + 1 
            p = p.next

        print(length)

        p = head
        mid = length // 2 
        while mid != 1:
            p = p.next
            mid = mid - 1 
        
        nextEle = p.next.next
        p.next = nextEle

        return head 

