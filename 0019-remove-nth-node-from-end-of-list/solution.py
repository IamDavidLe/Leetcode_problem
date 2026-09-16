# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        pos = 0
        pnt1 = dummy

        while curr:
            curr = curr.next
            pos += 1
        
        for _ in range(pos - n):
            pnt1 = pnt1.next
        pnt1.next = pnt1.next.next
        return dummy.next