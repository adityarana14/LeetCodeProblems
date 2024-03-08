# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = ListNode()
        final = final_list

        while list1 != None and list2 != None:
            if list1.val >= list2.val: 
                final_list.next = list2
                list2 = list2.next
            else: 
                final_list.next = list1 
                list1 = list1.next

            final_list = final_list.next

        if list1 != None:   
            final_list.next = list1              
        else: 
            final_list.next = list2
                
        return final.next