# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.candidates = []
        if not root:
            return
        ptr = root
        self.candidates.append(ptr)
        while ptr.left:
            self.candidates.append(ptr.left)
            ptr = ptr.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.candidates) > 0
        

    # @return an integer, the next smallest number
    def next(self):
        if not self.hasNext():
            return None
        result = self.candidates.pop()
        if result.right:
            ptr = result.right
            self.candidates.append(ptr)
            while ptr.left:
                self.candidates.append(ptr.left)
                ptr = ptr.left
        return result.val
            
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
