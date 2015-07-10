# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        height = self.countLeftHeight(root)
        node = root
        level = 1
        count = height
        while True:
            lh = self.countLeftHeight(node)
            rh = self.countRightHeight(node)
            if lh - rh == 1:
                # look at the right halve tree
                if rh == self.countLeftHeight(node.right):
                    count -= height / (2 ** level)
                    node = node.left
                else:
                    node = node.right
                level += 1
            else:
                # lh == rh
                break
        count += height * (height - 1) / 2
        return count
            

    def countLeftHeight(self, root):
        height = 1
        while root.left:
            height += 1
        return height
        
    def countRightHeight(self, root):
        height = 1
        while root.right:
            height += 1
        return height
