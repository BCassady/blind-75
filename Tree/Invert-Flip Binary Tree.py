# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if(root == None):
            return root
        
        
        if (root.left == None and root.right != None):
            root.left = Solution.invertTree(self, root.right)
            root.right = None
            return root
            
        if (root.right == None and root.left != None):
            root.right = Solution.invertTree(self, root.left)
            root.left = None
            return root
            
        temp = Solution.invertTree(self, root.left)
        root.left = Solution.invertTree(self, root.right)
        root.right = temp
        return root
        
        