# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return list()
        result = []
        next_level = [root]
        
        while len(next_level):
            level = []
            new = []
            for node in next_level:
                level.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            result.append(level)
            next_level = new
        return result

# 60ms
