# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pos = 0
        curr = head
        while curr:
            pos += 1
            curr = curr.next

        rotate = k % pos
        if rotate == 0:
            return head
            
        pnt1 = head
        for _ in range(pos - rotate - 1):
            pnt1 = pnt1.next

        branch = pnt1.next
        pnt1.next = None

        curr = branch
        while curr.next:
            curr = curr.next
        
        curr.next = head
        return branch
