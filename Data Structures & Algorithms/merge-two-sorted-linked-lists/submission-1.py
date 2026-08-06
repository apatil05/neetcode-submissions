# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            merged.val =  list1.val
            merged.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged.val = list2.val
            merged.next = self.mergeTwoLists(list2.next, list1)
        

        return merged