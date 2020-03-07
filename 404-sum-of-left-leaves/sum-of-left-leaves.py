# -*- coding:utf-8 -*-


# English:
# Find the sum of all left leaves in a given binary tree.
# Example:
# 3 / \ 9 20 / \ 15 7 There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
# 中文:
# 计算给定二叉树的所有左叶子之和。
# 示例：
# 3 / \ 9 20 / \ 15 7 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


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




