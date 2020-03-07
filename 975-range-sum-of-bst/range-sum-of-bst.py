# -*- coding:utf-8 -*-


# English:
# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.
# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15 Output: 32
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10 Output: 23
# Note:
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
#
# 中文:
# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
# 二叉搜索树保证具有唯一的值。
# 示例 1：
# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15 输出：32
# 示例 2：
# 输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10 输出：23
# 提示：
# 树中的结点数量最多为 10000 个。
# 最终的答案保证小于 2^31。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0 
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        return res
