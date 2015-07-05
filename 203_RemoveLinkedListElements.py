# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

    def bremoveElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        current = head
        while current.next:
            if current.next.val == val:
                current.next= current.next.next
            else:
                current = current.next
        return head

    def aremoveElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        prev = head
        current = head.next
        while current:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head
