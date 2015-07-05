# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if node.left or node.right:
                node.left, node.right = node.right, node.left
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
