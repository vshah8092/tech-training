# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Solution 1 - Recursive
        #if root == None:
        #    return []
        #return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        #Solution 2 - Iterative
        traversal = []
        order = [root]
        if root == None:
            return []
        while len(order) != 0:
            a = order[-1]
            order = order[:-1]
            traversal.append(a.val)
            if a.right:
                order.append(a.right)
            if a.left:
                order.append(a.left)
        return traversal