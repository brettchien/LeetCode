# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def parse(self, l1, l2):
        ln1 = ListNode(None)
        ln2 = ListNode(None)
        curr1 = ln1
        curr2 = ln2
        for val in l1:
            curr1.next = ListNode(val)
            curr1 = curr1.next
        for val in l2:
            curr2.next = ListNode(val)
            curr2 = curr2.next
        return self.toList(self.mergeTwoLists(ln1.next, ln2.next))

    def toList(self, ln):
        result = []
        while ln:
            result.append(ln.val)
            ln = ln.next
        return result

    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        current = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    current = current.next
                    l1 = l1.next
                elif l1.val > l2.val:
                    current.next = l2
                    current = current.next
                    l2 = l2.next
            elif l1:
                current.next = l1
                break
            elif l2:
                current.next = l2
                break
            else:
                pass
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    print sol.parse([1], [1])        
