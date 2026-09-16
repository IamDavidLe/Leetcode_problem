# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = head
        curr = head.next
        next_node = curr.next

        first = -1
        pos = 1
        prev_critical = -1
        min_dis = float('inf')

        while next_node:
            if (curr.val > prev_node.val and curr.val > next_node.val) or (curr.val < prev_node.val and curr.val < next_node.val):
                    if first == -1:
                        first = pos 
                    else:
                        min_dis = min(min_dis, pos - prev_critical)
                    
                    prev_critical = pos
            
            prev_node = curr
            curr = next_node
            next_node = next_node.next

            pos += 1

        if first == -1 or first == prev_critical :
            return [-1,-1]

        max_dis = prev_critical - first

        return [min_dis, max_dis]          
