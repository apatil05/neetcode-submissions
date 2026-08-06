# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pt1 = head
        pt2 = head

        while pt2 and pt2.next:
            pt1 = pt1.next
            if pt2.next.next:
                pt2 = pt2.next.next
            else:
                pt2 = pt2.next
        
        second = pt1.next
        pt1.next = None
        #Now pt1 and pt2 should be at the half and end respectively
        prev = None
        pt1 = second
        while pt1 and pt1.next:
            temp = pt1.next
            pt1.next = prev
            prev = pt1
            pt1 = temp
        if pt1:
            pt1.next = prev

        
        curr = head
        while pt1:
            temp = curr.next 
            curr.next = pt1
            temp2 = pt1.next
            pt1.next = temp
            curr = temp
            pt1 = temp2
        
        return None
            


        
