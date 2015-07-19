class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def toList(ln):
    result = []
    while ln:
        result.append(ln.val)
        ln = ln.next
    return result

def toLinkedList(aList):
    ln = ListNode(None)
    curr = ln
    for val in aList:
        curr.next = ListNode(val)
        curr = curr.next
    return ln.next
