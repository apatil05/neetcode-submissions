# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            prev, curr, nxt = None, head, head.next
        elif head:
            return head
        else:
            return None

        
        while nxt != None:
            prev = curr
            curr = nxt
            nxt = curr.next
            curr.next = prev
        
        head.next = None
        return curr