# -*- coding:utf-8 -*-

# <SUBID:19459157,UPDATE:20230205>
# English:
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
# Example 1:
# Input: root = [3,9,20,null,null,15,7] Output: 24 Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:
# Input: root = [1] Output: 0
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
#
# 中文:
# 给定二叉树的根节点 root ，返回所有左叶子之和。
# 示例 1：
# 输入: root = [3,9,20,null,null,15,7] 输出: 24 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 示例 2:
# 输入: root = [1] 输出: 0
# 提示:
# 节点数在 [1, 1000] 范围内
# -1000 <= Node.val <= 1000


#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root, is_left=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if is_left else 0

        return self.sumOfLeftLeaves(root.left, is_left=True) + self.sumOfLeftLeaves(root.right)




