# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [(False, root)]
        while stack:
            read, node = stack.pop()
            if read:
                result.append(node.val)
            else:
                stack.append((True, node))
                if node.right:
                    stack.append((False, node.right))
                if node.left:
                    stack.append((False, node.left))
        return result
