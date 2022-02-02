# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Solution 1 - Recursive
        #if root == None:
        #    return []
        #return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        #Solution 2 - Iterative
        if root == None:
            return []
        currNode = root
        traversal = []
        order = []
        while len(order) != 0 or currNode != None:
            if currNode != None:
                order.append(currNode)
                currNode = currNode.left
            else:
                if len(order) != 0:
                    currNode = order[-1]
                    order = order[:-1]
                    traversal.append(currNode.val)
                    currNode = currNode.right
        return traversal