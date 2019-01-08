# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def count_nodes(self, root):
        if root is None:
            return 0
        
        lcnt = self.count_nodes(root.left)
        rcnt = self.count_nodes(root.right)
        self.num_of_nodes[root.val] = lcnt + rcnt + 1
        return lcnt + rcnt + 1
    
    def match(self, root, voyage):
        if root is None:
            return [] if len(voyage) == 0 else None
        if root.val != voyage[0]:
            return None
        
        lcnt = 0 if root.left is None else self.num_of_nodes[root.left.val]
        rcnt = 0 if root.right is None else self.num_of_nodes[root.right.val]
        
        l_result = self.match(root.left, voyage[1:1 + lcnt])
        r_result = self.match(root.right, voyage[1 + lcnt:1 + lcnt + rcnt])
        if l_result is not None and r_result is not None:
            return l_result + r_result
        
        l_result = self.match(root.left, voyage[1 + rcnt:1 + rcnt + lcnt])
        r_result = self.match(root.right, voyage[1:1 + rcnt])
        if l_result is not None and r_result is not None:
            return [root.val] + l_result + r_result
        
        return None
    
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.num_of_nodes = {}
        self.count_nodes(root)

        ans = self.match(root, voyage)
        return [-1] if ans is None else ans
