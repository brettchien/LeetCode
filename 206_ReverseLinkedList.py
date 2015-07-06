# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current.next:
            prev = dummy.next
            tmp = current.next
            current.next = current.next.next
            tmp.next = prev
            dummy.next = tmp
        return dummy.next
