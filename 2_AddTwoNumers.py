# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        result = current = ListNode(0)
        carry = 0
        while True:
            value = carry + l1.val + l2.val
            carry = value / 10
            current.val = value % 10
            if (not l1.next) and (not l2.next):
                if carry > 0:
                    current.next = ListNode(carry)
                break
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode(0)
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            current.next = ListNode(carry)
            current = current.next
        return result
