# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [(False, root)]
        while stack:
            read, node = stack.pop()
            if read:
                result.append(node.val)
            else:
                if node.right:
                    stack.append((False, node.right))
                stack.append((True, node))
                if node.left:
                    stack.append((False, node.left))
        return result
        
