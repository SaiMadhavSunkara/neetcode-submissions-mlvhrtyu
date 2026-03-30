# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        flag = 0

        while l1 or l2 or flag:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            final = v1 + v2 + flag

            if final >= 10:
                flag = 1
                final -= 10
            else:
                flag = 0
            node.next = ListNode(final)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if flag == 1:
            node.next = ListNode(1)
        return dummy.next



        