# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return True
        if head and not head.next:
            return True
        first = head
        second = head.next
        while second.next and second.next.next:
            first = first.next
            second = second.next.next

        # reverse second halve
        second = self.reverseList(first.next)
        first = head
        while first and second:
            print first.val, second.val
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
        
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
