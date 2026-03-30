# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = node = ListNode()
        node.next = head
        exchange = right - left + 1


        for i in range(left - 1):
            node = node.next

        tail = node.next
        prev, curr = None, tail

        while exchange > 0 and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            exchange -= 1

        node.next.next = curr
        node.next = prev


        return dummy.next

        
        

            