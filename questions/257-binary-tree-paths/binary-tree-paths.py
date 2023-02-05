# -*- coding:utf-8 -*-

# <SUBID:313782451,UPDATE:20230205>
# English:
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
# Example 1:
# Input: root = [1,2,3,null,5] Output: ["1->2->5","1->3"]
# Example 2:
# Input: root = [1] Output: ["1"]
# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
#
# 中文:
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [1,2,3,null,5] 输出：["1->2->5","1->3"]
# 示例 2：
# 输入：root = [1] 输出：["1"]
# 提示：
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SolutionA:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        dfs
        """

        ans = []
        def dfs(node, path=None):
            if path is None:
                path = []
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(path))
                return
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()

        if not root:
            return
        dfs(root)
        return ans

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(node: TreeNode):
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append('->'.join(path))
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            path.pop()

        path = []
        res = []
        traverse(root)
        return res

