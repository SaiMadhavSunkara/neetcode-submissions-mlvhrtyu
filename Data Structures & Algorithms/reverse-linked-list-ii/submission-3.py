# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = node = ListNode(0, head)
        node, node2 = head, dummy

        for i in range(left - 1):
            node2, node = node2.next, node.next

        prev, curr = None, node

        for i in range(right- left+1) :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        node2.next.next = curr
        node2.next = prev



        return dummy.next

        
        

            